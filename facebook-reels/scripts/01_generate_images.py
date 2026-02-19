#!/usr/bin/env python3
"""
Facebook Reels - Stage 1: Generate Portrait Images
Generates 1080x1920 portrait images using Flux 2 Klein 9B for Facebook Reels content.

Usage:
    python 01_generate_images.py <content_type>/<story>
    python 01_generate_images.py ghibli_mythology/01_norse_ragnarok
    python 01_generate_images.py realistic_mythology/01_greek_prometheus
    python 01_generate_images.py nature_ambient/moonlit_forest   (for single ambient prompt)
"""

import json
import sys
import time
import requests
from pathlib import Path
from typing import List


class ImageGenerator:
    def __init__(self, comfyui_url: str = "http://127.0.0.1:8000"):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.base_path = Path(__file__).parent.parent

    def load_prompts(self, story_path: Path) -> List[str]:
        """Load image prompts from file."""
        prompts_file = story_path / "image_prompts.txt"

        if not prompts_file.exists():
            raise FileNotFoundError(f"Image prompts file not found: {prompts_file}")

        with open(prompts_file, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        return prompts

    def queue_image(self, prompt: str, scene_number: int, output_prefix: str) -> str:
        """Queue a single image generation."""
        # Matches flux2_portrait_1080x1920.json:
        # KSampler with 4 steps, cfg=1, ConditioningZeroOut for negative
        workflow = {
            "1": {
                "inputs": {
                    "unet_name": "flux-2-klein-base-9b-fp8.safetensors",
                    "weight_dtype": "default"
                },
                "class_type": "UNETLoader"
            },
            "2": {
                "inputs": {
                    "clip_name": "qwen_3_8b_fp8mixed.safetensors",
                    "type": "flux2",
                    "device": "default"
                },
                "class_type": "CLIPLoader"
            },
            "3": {
                "inputs": {
                    "vae_name": "flux2-vae.safetensors"
                },
                "class_type": "VAELoader"
            },
            "4": {
                "inputs": {
                    "text": prompt,
                    "clip": ["2", 0]
                },
                "class_type": "CLIPTextEncode"
            },
            "5": {
                "inputs": {
                    "conditioning": ["4", 0]
                },
                "class_type": "ConditioningZeroOut"
            },
            "6": {
                "inputs": {
                    "width": 1080,
                    "height": 1920,
                    "batch_size": 1
                },
                "class_type": "EmptyFlux2LatentImage"
            },
            "7": {
                "inputs": {
                    "seed": int(time.time() * 1000) % (2**32) + scene_number,
                    "steps": 4,
                    "cfg": 1,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "denoise": 1,
                    "model": ["1", 0],
                    "positive": ["4", 0],
                    "negative": ["5", 0],
                    "latent_image": ["6", 0]
                },
                "class_type": "KSampler"
            },
            "8": {
                "inputs": {
                    "samples": ["7", 0],
                    "vae": ["3", 0]
                },
                "class_type": "VAEDecode"
            },
            "9": {
                "inputs": {
                    "filename_prefix": f"{output_prefix}_scene_{scene_number:03d}",
                    "images": ["8", 0]
                },
                "class_type": "SaveImage"
            }
        }

        payload = {
            "prompt": workflow,
            "client_id": f"reel_image_gen_{scene_number}"
        }

        try:
            response = requests.post(f"{self.comfyui_url}/prompt", json=payload, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result.get('prompt_id', '')
            else:
                print(f"     HTTP {response.status_code}: {response.text[:200]}")
            return None
        except requests.exceptions.ConnectionError:
            print(f"     Error: Could not connect to ComfyUI at {self.comfyui_url}")
            return None
        except Exception as e:
            print(f"     Error: {e}")
            return None

    def generate(self, content_type: str, story_folder: str):
        """Generate all images for a content type / story."""
        story_path = self.base_path / "content" / content_type / story_folder

        if not story_path.exists():
            print(f"Story path not found: {story_path}")
            print(f"   Expected: content/{content_type}/{story_folder}/")
            return

        print(f"\nProcessing: {content_type}/{story_folder}")
        print(f"   Path: {story_path}")

        try:
            prompts = self.load_prompts(story_path)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        print(f"   Found {len(prompts)} image prompts\n")

        output_prefix = f"reel_{content_type}_{story_folder}"
        successful = 0
        failed = 0

        print("=" * 70)
        print(f"Stage 1: Image Generation - {content_type}/{story_folder}")
        print("=" * 70)

        for i, prompt in enumerate(prompts, start=1):
            display_prompt = prompt[:65] + "..." if len(prompt) > 65 else prompt
            print(f"[{i:03d}/{len(prompts):03d}] {display_prompt}")

            prompt_id = self.queue_image(prompt, i, output_prefix)

            if prompt_id:
                print(f"          Queued (ID: {prompt_id[:8]}...)")
                successful += 1
            else:
                print(f"          Failed")
                failed += 1

            time.sleep(0.3)

        print("\n" + "=" * 70)
        print(f"Complete - {content_type}/{story_folder}")
        print("=" * 70)
        print(f"   Queued:  {successful}")
        print(f"   Failed:  {failed}")
        print(f"   Prefix:  {output_prefix}_scene_NNN")
        print(f"   Output:  C:/ComfyUI/output/")
        print("=" * 70 + "\n")

    def generate_nature_ambient(self, prompt_file: Path):
        """Generate a single image for a nature_ambient prompt file."""
        scene_name = prompt_file.stem
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read().strip()

        if not prompt:
            print(f"   Skipping empty file: {prompt_file.name}")
            return 0, 0

        output_prefix = f"reel_nature_ambient_{scene_name}"
        print("=" * 70)
        print(f"Stage 1: Image Generation - nature_ambient/{scene_name}")
        print("=" * 70)
        display_prompt = prompt[:65] + "..." if len(prompt) > 65 else prompt
        print(f"[001/001] {display_prompt}")

        prompt_id = self.queue_image(prompt, 1, output_prefix)
        if prompt_id:
            print(f"          Queued (ID: {prompt_id[:8]}...)")
            print(f"   Output prefix: {output_prefix}_scene_001")
            return 1, 0
        else:
            print(f"          Failed")
            return 0, 1

    def generate_all(self):
        """Generate images for all content types and stories."""
        content_path = self.base_path / "content"
        total_queued = 0
        total_failed = 0

        print("\n" + "=" * 70)
        print("  Generating ALL reels content")
        print("=" * 70)

        # ghibli_mythology and realistic_mythology
        for content_type in ["ghibli_mythology", "realistic_mythology"]:
            type_path = content_path / content_type
            if not type_path.exists():
                continue
            stories = sorted([d for d in type_path.iterdir() if d.is_dir()])
            for story_path in stories:
                story_folder = story_path.name
                self.generate(content_type, story_folder)

        # nature_ambient — each .txt in prompts/ is a single scene
        nature_prompts_path = content_path / "nature_ambient" / "prompts"
        if nature_prompts_path.exists():
            prompt_files = sorted(nature_prompts_path.glob("*.txt"))
            for pf in prompt_files:
                q, f = self.generate_nature_ambient(pf)
                total_queued += q
                total_failed += f
                time.sleep(0.3)

        print("\n" + "=" * 70)
        print("  All content queued!")
        print("=" * 70 + "\n")


def main():
    """Main entry point."""
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "=" * 70)
    print("  Stage 1: Image Generation (Flux 2 Klein - 1080x1920 Portrait)")
    print("=" * 70 + "\n")

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python 01_generate_images.py all")
        print("  python 01_generate_images.py <content_type>/<story_folder>")
        print("\nExamples:")
        print("  python 01_generate_images.py all")
        print("  python 01_generate_images.py ghibli_mythology/01_norse_ragnarok")
        print("  python 01_generate_images.py realistic_mythology/01_greek_prometheus")
        print("  python 01_generate_images.py realistic_mythology/02_egyptian_ra_and_apep")
        print("\nContent types:")
        print("  - ghibli_mythology")
        print("  - realistic_mythology")
        print("  - nature_ambient  (use 'all' to generate these)")
        print()
        sys.exit(1)

    arg = sys.argv[1]
    generator = ImageGenerator()

    if arg == "all":
        generator.generate_all()
        return

    if '/' not in arg:
        print(f"Error: argument must be 'all' or <content_type>/<story_folder>")
        print(f"   Got: {arg}")
        print(f"   Example: ghibli_mythology/01_norse_ragnarok")
        sys.exit(1)

    parts = arg.split('/', 1)
    content_type = parts[0]
    story_folder = parts[1]

    generator.generate(content_type, story_folder)


if __name__ == "__main__":
    main()

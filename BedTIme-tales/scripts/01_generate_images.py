#!/usr/bin/env python3
"""
Stage 1: Generate Images from Text Prompts
Reads image prompts and generates static images using Flux 2 Klein.
These images become the first frame for video generation.

Usage:
    python 01_generate_images.py <story_name>
    python 01_generate_images.py lumi_bunny
    python 01_generate_images.py all
"""

import json
import sys
import time
import requests
from pathlib import Path
from typing import List, Dict


class ImageGenerator:
    def __init__(self, comfyui_url: str = "http://127.0.0.1:8001"):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.base_path = Path(__file__).parent.parent

    def get_story_path(self, story_name: str) -> Path:
        """Get the path for a story folder."""
        story_mapping = {
            'lumi': '01_lumi_bunny',
            'lumi_bunny': '01_lumi_bunny',
            'bruno': '02_bruno_bear',
            'bruno_bear': '02_bruno_bear',
            'gatita': '03_gatita_nube',
            'gatita_nube': '03_gatita_nube',
            'cierva': '04_cierva_rio',
            'cierva_rio': '04_cierva_rio',
            'zorro': '05_zorro_luna',
            'zorro_luna': '05_zorro_luna',
            'tortuga': '06_tortuga_serena',
            'tortuga_serena': '06_tortuga_serena',
            'elefante': '07_elefante_nube',
            'elefante_nube': '07_elefante_nube',
            'panda': '08_panda_mochi',
            'panda_mochi': '08_panda_mochi',
            'pinguino': '09_pinguino_polo',
            'pinguino_polo': '09_pinguino_polo',
            'dragon': '10_dragoncito_chispa',
            'dragoncito_chispa': '10_dragoncito_chispa',
        }

        folder = story_mapping.get(story_name.lower(), story_name)
        return self.base_path / 'stories' / folder

    def load_prompts(self, story_path: Path) -> List[str]:
        """Load image prompts from file."""
        prompts_file = story_path / '01_image_prompts.txt'

        if not prompts_file.exists():
            raise FileNotFoundError(f"Image prompts file not found: {prompts_file}")

        with open(prompts_file, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        return prompts

    def queue_image(self, prompt: str, scene_number: int, output_prefix: str) -> str:
        """Queue a single image generation."""
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
                    "weight_dtype": "default"
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
                    "text": "",
                    "clip": ["2", 0]
                },
                "class_type": "CLIPTextEncode"
            },
            "6": {
                "inputs": {
                    "width": 1920,
                    "height": 1088,
                    "batch_size": 1
                },
                "class_type": "EmptyFlux2LatentImage"
            },
            "7": {
                "inputs": {
                    "sampler_name": "euler"
                },
                "class_type": "KSamplerSelect"
            },
            "8": {
                "inputs": {
                    "steps": 20,
                    "width": 1024,
                    "height": 1024
                },
                "class_type": "Flux2Scheduler"
            },
            "9": {
                "inputs": {
                    "cfg": 5.0,
                    "model": ["1", 0],
                    "positive": ["4", 0],
                    "negative": ["5", 0]
                },
                "class_type": "CFGGuider"
            },
            "10": {
                "inputs": {
                    "noise_seed": int(time.time() * 1000) % (2**32) + scene_number,
                },
                "class_type": "RandomNoise"
            },
            "11": {
                "inputs": {
                    "noise": ["10", 0],
                    "guider": ["9", 0],
                    "sampler": ["7", 0],
                    "sigmas": ["8", 0],
                    "latent_image": ["6", 0]
                },
                "class_type": "SamplerCustomAdvanced"
            },
            "12": {
                "inputs": {
                    "samples": ["11", 0],
                    "vae": ["3", 0]
                },
                "class_type": "VAEDecode"
            },
            "13": {
                "inputs": {
                    "filename_prefix": f"{output_prefix}_scene_{scene_number:03d}",
                    "images": ["12", 0]
                },
                "class_type": "SaveImage"
            }
        }

        payload = {
            "prompt": workflow,
            "client_id": f"image_gen_{scene_number}"
        }

        try:
            response = requests.post(f"{self.comfyui_url}/prompt", json=payload, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result.get('prompt_id', '')
            return None
        except Exception as e:
            print(f"     Error: {e}")
            return None

    def generate_story(self, story_name: str):
        """Generate all images for a story."""
        # Get story path
        story_path = self.get_story_path(story_name)

        if not story_path.exists():
            print(f"❌ Story not found: {story_name}")
            print(f"   Path: {story_path}")
            return

        # Load prompts
        print(f"\n📖 Processing: {story_path.name}")
        print(f"   Path: {story_path}")

        try:
            prompts = self.load_prompts(story_path)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            return

        print(f"   Found {len(prompts)} image prompts\n")

        # Generate images
        output_prefix = story_path.name
        successful = 0
        failed = 0

        print("="*70)
        print(f"🎨 Generating Images for {story_path.name}")
        print("="*70)

        for i, prompt in enumerate(prompts, start=1):
            display_prompt = prompt[:65] + "..." if len(prompt) > 65 else prompt
            print(f"[{i:03d}/{len(prompts):03d}] {display_prompt}")

            prompt_id = self.queue_image(prompt, i, output_prefix)

            if prompt_id:
                print(f"          ✅ Queued (ID: {prompt_id[:8]}...)")
                successful += 1
            else:
                print(f"          ❌ Failed")
                failed += 1

            time.sleep(0.3)

        print("\n" + "="*70)
        print(f"✨ Complete - {story_path.name}")
        print("="*70)
        print(f"   ✅ Queued: {successful}")
        print(f"   ❌ Failed: {failed}")
        print(f"   📁 Output: {story_path / 'outputs' / 'images'}/")
        print("="*70 + "\n")


def main():
    """Main entry point."""
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*70)
    print("  🎨 Stage 1: Image Generation (Flux 2 Klein)")
    print("="*70 + "\n")

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python 01_generate_images.py <story_name>")
        print("\nExamples:")
        print("  python 01_generate_images.py lumi_bunny")
        print("  python 01_generate_images.py bruno_bear")
        print("  python 01_generate_images.py all")
        print("\nAvailable stories:")
        print("  - lumi_bunny (or: lumi)")
        print("  - bruno_bear (or: bruno)")
        print("  - gatita_nube (or: gatita)")
        print("  - cierva_rio (or: cierva)")
        print("  - zorro_luna (or: zorro)")
        print()
        sys.exit(1)

    story_name = sys.argv[1]

    generator = ImageGenerator()

    if story_name.lower() == 'all':
        stories = ['lumi_bunny', 'bruno_bear', 'gatita_nube', 'cierva_rio', 'zorro_luna',
                   'tortuga_serena', 'elefante_nube', 'panda_mochi', 'pinguino_polo', 'dragoncito_chispa']
        for story in stories:
            generator.generate_story(story)
    else:
        generator.generate_story(story_name)


if __name__ == "__main__":
    main()

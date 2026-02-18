#!/usr/bin/env python3
"""
Stage 2: Generate Videos from Images - SPANISH VERSION (Narrator)
Reads generated images from Stage 1 and Spanish video prompts with narrator voice,
then generates videos using LTX2 with classical music background.

Uses: 02_video_prompts_spanish.txt (100-120 words, single maternal narrator)

Usage:
    python 02_generate_videos_spanish.py <story_name>
    python 02_generate_videos_spanish.py lumi_bunny
    python 02_generate_videos_spanish.py all
"""

import json
import sys
import time
import requests
import io
from pathlib import Path
from typing import List, Tuple


class SpanishVideoGenerator:
    def __init__(self, comfyui_url: str = "http://127.0.0.1:8001"):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.base_path = Path(__file__).parent.parent
        self.comfyui_input_path = Path("C:/ComfyUI/input")

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
            'zorro_luna': '05_zorro_luna'
        }

        folder = story_mapping.get(story_name.lower(), story_name)
        return self.base_path / 'stories' / folder

    def load_video_prompts(self, story_path: Path) -> List[str]:
        """Load Spanish video prompts from file."""
        prompts_file = story_path / '02_video_prompts_spanish.txt'

        if not prompts_file.exists():
            raise FileNotFoundError(f"Spanish video prompts file not found: {prompts_file}")

        with open(prompts_file, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        return prompts

    def find_generated_images(self, story_name: str) -> List[Path]:
        """Find images generated in Stage 1."""
        output_dir = Path("C:/ComfyUI/output")
        story_path = self.get_story_path(story_name)
        folder_name = story_path.name

        pattern = f"{folder_name}_scene_*.png"
        images = sorted(output_dir.glob(pattern))

        return images

    def get_scene_number(self, image_path: Path) -> int:
        """Extract scene number from image filename."""
        # Example: 01_lumi_bunny_scene_001_00001.png -> 1
        parts = image_path.stem.split('_scene_')
        if len(parts) == 2:
            scene_part = parts[1].split('_')[0]
            return int(scene_part)
        return 0

    def prepare_image_for_comfyui(self, image_path: Path) -> str:
        """Copy image to ComfyUI input folder and return filename."""
        import shutil

        dest = self.comfyui_input_path / image_path.name
        if not dest.exists():
            self.comfyui_input_path.mkdir(parents=True, exist_ok=True)
            shutil.copy2(image_path, dest)

        return image_path.name

    def queue_video(self, image_filename: str, prompt: str, scene_number: int, output_prefix: str) -> str:
        """Queue a single video generation with Spanish narration."""
        workflow = {
            "1": {
                "inputs": {
                    "ckpt_name": "ltx-av-step-1751000_vocoder_24K.safetensors"
                },
                "class_type": "CheckpointLoaderSimple"
            },
            "2": {
                "inputs": {
                    "stop_at_clip_layer": -2,
                    "clip": ["1", 1]
                },
                "class_type": "CLIPSetLastLayer"
            },
            "3": {
                "inputs": {
                    "text": prompt,
                    "clip": ["2", 0]
                },
                "class_type": "CLIPTextEncode"
            },
            "4": {
                "inputs": {
                    "text": "",
                    "clip": ["2", 0]
                },
                "class_type": "CLIPTextEncode"
            },
            "8": {
                "inputs": {
                    "width": 512,
                    "height": 512,
                    "length": 480,  # 480 frames = 20 seconds at 24fps
                    "batch_size": 1
                },
                "class_type": "EmptyLTXVLatentVideo"
            },
            "94": {
                "inputs": {
                    "image": image_filename,
                    "upload": "image"
                },
                "class_type": "LoadImage"
            },
            "95": {
                "inputs": {
                    "mode": "scale dimensions",
                    "width": 1280,
                    "height": 720,
                    "side_length": 512,
                    "crop_position": "center",
                    "interpolation": "lanczos",
                    "input": ["94", 0]
                },
                "class_type": "ResizeImageMaskNode"
            },
            "96": {
                "inputs": {
                    "image": ["95", 0]
                },
                "class_type": "LTXVImageToVideo"
            },
            "97": {
                "inputs": {
                    "sampling": "euler",
                    "steps": 30,
                    "cfg": 3,
                    "sampler_name": "normal",
                    "scheduler": "sgm_uniform",
                    "denoise": 1,
                    "model": ["1", 0],
                    "positive": ["3", 0],
                    "negative": ["4", 0],
                    "latent_image": ["96", 0]
                },
                "class_type": "SamplerCustom"
            },
            "98": {
                "inputs": {
                    "samples": ["97", 0],
                    "vae": ["1", 2]
                },
                "class_type": "VAEDecode"
            },
            "99": {
                "inputs": {
                    "filename_prefix": f"{output_prefix}_spanish_scene_{scene_number:03d}",
                    "fps": 24,
                    "compress_level": 4,
                    "images": ["98", 0]
                },
                "class_type": "SaveAnimatedWEBP"
            },
            "100": {
                "inputs": {
                    "images": ["98", 0],
                    "fps": 24,
                    "filename_prefix": f"{output_prefix}_spanish_scene_{scene_number:03d}"
                },
                "class_type": "VHSVideoCombine"
            }
        }

        payload = {
            "prompt": workflow,
            "client_id": f"spanish_video_{scene_number}"
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
        """Generate all Spanish videos for a story."""
        story_path = self.get_story_path(story_name)

        if not story_path.exists():
            print(f"❌ Story not found: {story_name}")
            print(f"   Path: {story_path}")
            return

        print(f"\n📖 Processing: {story_path.name} (SPANISH)")
        print(f"   Path: {story_path}")

        # Load Spanish video prompts
        try:
            video_prompts = self.load_video_prompts(story_path)
            print(f"   Found {len(video_prompts)} Spanish video prompts")
        except FileNotFoundError as e:
            print(f"❌ {e}")
            return

        # Find generated images
        images = self.find_generated_images(story_name)

        if not images:
            print(f"❌ No images found for {story_name}")
            print(f"   Run Stage 1 first: python 01_generate_images.py {story_name}")
            return

        print(f"   Found {len(images)} generated images")

        # Match images to prompts by scene number
        scene_pairs = []
        for image in images:
            scene_num = self.get_scene_number(image)
            if 1 <= scene_num <= len(video_prompts):
                prompt = video_prompts[scene_num - 1]
                scene_pairs.append((scene_num, image, prompt))

        if not scene_pairs:
            print(f"❌ Could not match images to prompts")
            return

        print(f"   Matched {len(scene_pairs)} image/prompt pairs\n")

        # Generate videos
        output_prefix = story_path.name
        successful = 0
        failed = 0

        print("="*70)
        print(f"🎬 Generating Spanish Videos for {story_path.name}")
        print(f"   Voice: Maternal Spanish narrator (NARRADOR)")
        print(f"   Music: Classical background")
        print("="*70)

        for scene_num, image_path, prompt in scene_pairs:
            # Prepare image
            image_filename = self.prepare_image_for_comfyui(image_path)

            display_prompt = prompt[:60] + "..." if len(prompt) > 60 else prompt
            print(f"[{scene_num:03d}] {display_prompt}")
            print(f"      Image: {image_path.name}")

            prompt_id = self.queue_video(image_filename, prompt, scene_num, output_prefix)

            if prompt_id:
                print(f"      ✅ Queued (ID: {prompt_id[:8]}...)")
                successful += 1
            else:
                print(f"      ❌ Failed")
                failed += 1

            time.sleep(0.3)

        print("\n" + "="*70)
        print(f"✨ Complete - {story_path.name} (SPANISH)")
        print("="*70)
        print(f"   ✅ Queued: {successful}")
        print(f"   ❌ Failed: {failed}")
        print(f"   📁 Output: C:/ComfyUI/output/")
        print(f"   🎵 Features: Spanish narrator + Classical music")
        print("="*70 + "\n")


def main():
    """Main entry point."""
    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*70)
    print("  🎬 Stage 2: Spanish Video Generation (LTX2)")
    print("  🗣️  Spanish Narrator Version")
    print("="*70 + "\n")

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python 02_generate_videos_spanish.py <story_name>")
        print("\nExamples:")
        print("  python 02_generate_videos_spanish.py lumi_bunny")
        print("  python 02_generate_videos_spanish.py bruno_bear")
        print("  python 02_generate_videos_spanish.py all")
        print("\nAvailable stories:")
        print("  - lumi_bunny (or: lumi)")
        print("  - bruno_bear (or: bruno)")
        print("  - gatita_nube (or: gatita)")
        print("  - cierva_rio (or: cierva)")
        print("  - zorro_luna (or: zorro)")
        print("\n⚠️  Note: Run Stage 1 first to generate images!")
        print("\n📝 This version uses Spanish narrator voice")
        print("   For English character voices, use: 02_generate_videos_english.py")
        print()
        sys.exit(1)

    story_name = sys.argv[1]

    generator = SpanishVideoGenerator()

    if story_name.lower() == 'all':
        stories = ['lumi_bunny', 'bruno_bear', 'gatita_nube', 'cierva_rio', 'zorro_luna']
        for story in stories:
            generator.generate_story(story)
    else:
        generator.generate_story(story_name)


if __name__ == "__main__":
    main()

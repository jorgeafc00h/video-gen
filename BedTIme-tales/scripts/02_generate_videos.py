#!/usr/bin/env python3
"""
Stage 2: Generate Videos from Images
Reads generated images from Stage 1 and video prompts, then generates videos using LTX-2.
Uses the official LTX-2 i2v workflow template (1280x720, 481 frames, ~19.2s at 25fps).
Workflow includes spatial upscaler (ltx-2-spatial-upscaler-x2-1.0.safetensors).

Usage:
    python 02_generate_videos.py <story_name>
    python 02_generate_videos.py lumi_bunny
    python 02_generate_videos.py all
"""

import copy
import json
import sys
import time
import requests
from pathlib import Path
from typing import List, Tuple


class VideoGenerator:
    def __init__(self, comfyui_url: str = "http://127.0.0.1:8000"):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.base_path = Path(__file__).parent.parent
        self.comfyui_input_path = Path("C:/ComfyUI/input")

        # Load the official LTX-2 i2v API workflow template once
        template_path = self.base_path / "video_ltx2_image2video api.json"
        with open(template_path, 'r', encoding='utf-8') as f:
            self._workflow_template = json.load(f)

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

    def load_video_prompts(self, story_path: Path) -> List[str]:
        """Load video prompts from file."""
        prompts_file = story_path / '02_video_prompts.txt'

        if not prompts_file.exists():
            raise FileNotFoundError(f"Video prompts file not found: {prompts_file}")

        with open(prompts_file, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        return prompts

    def find_generated_images(self, story_name: str) -> List[Path]:
        """Find images generated in Stage 1."""
        # Images are saved in ComfyUI output folder with the pattern:
        # <story_folder>_scene_001_00001.png

        output_dir = Path("C:/ComfyUI/output")

        # Get story folder name for pattern matching
        story_path = self.get_story_path(story_name)
        folder_name = story_path.name

        # Find all matching images
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

        # Copy to ComfyUI input folder
        dest = self.comfyui_input_path / image_path.name
        if not dest.exists():
            self.comfyui_input_path.mkdir(parents=True, exist_ok=True)
            shutil.copy2(image_path, dest)

        return image_path.name

    def queue_video(self, image_filename: str, prompt: str, scene_number: int, output_prefix: str) -> str:
        """Queue a single video generation using the official LTX-2 i2v workflow template.

        Substitutes 4 fields in the template per scene:
          - node 98  (LoadImage):       image filename
          - node 92:3 (CLIPTextEncode): positive prompt
          - node 92:11 (RandomNoise):   seed
          - node 75  (SaveVideo):       filename_prefix
        Everything else (spatial upscaler, two-pass sampler, 1280x720, 481 frames) stays as-is.
        """
        seed = int(time.time() * 1000) % (2**32) + scene_number
        workflow = copy.deepcopy(self._workflow_template)

        workflow["98"]["inputs"]["image"] = image_filename
        workflow["92:3"]["inputs"]["text"] = prompt
        workflow["92:11"]["inputs"]["noise_seed"] = seed
        workflow["75"]["inputs"]["filename_prefix"] = f"video/{output_prefix}_scene_{scene_number:03d}"

        payload = {
            "prompt": workflow,
            "client_id": f"video_gen_{scene_number}"
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

    def generate_story(self, story_name: str):
        """Generate all videos for a story."""
        # Get story path
        story_path = self.get_story_path(story_name)

        if not story_path.exists():
            print(f"❌ Story not found: {story_name}")
            print(f"   Path: {story_path}")
            return

        print(f"\n📖 Processing: {story_path.name}")
        print(f"   Path: {story_path}")

        # Load video prompts
        try:
            video_prompts = self.load_video_prompts(story_path)
            print(f"   Found {len(video_prompts)} video prompts")
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
        print(f"🎬 Generating Videos for {story_path.name}")
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
        print(f"✨ Complete - {story_path.name}")
        print("="*70)
        print(f"   ✅ Queued: {successful}")
        print(f"   ❌ Failed: {failed}")
        print(f"   📁 Output: C:/ComfyUI/output/")
        print("="*70 + "\n")


def main():
    """Main entry point."""
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*70)
    print("  🎬 Stage 2: Video Generation (LTX-2 i2v, 1280x720, 481f, spatial upscaler)")
    print("="*70 + "\n")

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python 02_generate_videos.py <story_name>")
        print("\nExamples:")
        print("  python 02_generate_videos.py lumi_bunny")
        print("  python 02_generate_videos.py bruno_bear")
        print("  python 02_generate_videos.py all")
        print("\nAvailable stories:")
        print("  - lumi_bunny (or: lumi)")
        print("  - bruno_bear (or: bruno)")
        print("  - gatita_nube (or: gatita)")
        print("  - cierva_rio (or: cierva)")
        print("  - zorro_luna (or: zorro)")
        print("\n⚠️  Note: Run Stage 1 first to generate images!")
        print()
        sys.exit(1)

    story_name = sys.argv[1]

    generator = VideoGenerator()

    if story_name.lower() == 'all':
        stories = ['lumi_bunny', 'bruno_bear', 'gatita_nube', 'cierva_rio', 'zorro_luna']
        for story in stories:
            generator.generate_story(story)
    else:
        generator.generate_story(story_name)


if __name__ == "__main__":
    main()

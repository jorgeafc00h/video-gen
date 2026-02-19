#!/usr/bin/env python3
"""
Facebook Reels - Stage 3: Nature Ambient Batch Generator
Generates portrait ambient loops from single-prompt text files.
Phase 1: Generates a 1080x1920 portrait image per prompt.
Phase 2: Queues a 512x896 ambient video per prompt (257 frames, ~25.7s at 10fps).

Usage:
    python 03_nature_ambient.py <prompt_name>
    python 03_nature_ambient.py moonlit_forest
    python 03_nature_ambient.py aurora_mountains
    python 03_nature_ambient.py all

Prompt files live in: content/nature_ambient/prompts/<prompt_name>.txt
The first non-blank, non-comment line in each file is used as the image prompt.

Note:
    This script queues images first, then videos in sequence.
    ComfyUI will process them in order -- images first, then videos.
    However, the video LoadImage node references the output filename before
    it exists. Ensure images are complete before videos begin processing,
    or run Phase 1 and Phase 2 separately.
"""

import json
import sys
import time
import shutil
import requests
from pathlib import Path
from typing import List, Optional, Tuple


COMFYUI_URL = "http://127.0.0.1:8000"
COMFYUI_OUTPUT = Path("C:/ComfyUI/output")
COMFYUI_INPUT = Path("C:/ComfyUI/input")


class NatureAmbientGenerator:
    def __init__(self, comfyui_url: str = COMFYUI_URL):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.base_path = Path(__file__).parent.parent
        self.prompts_dir = self.base_path / "content" / "nature_ambient" / "prompts"

    # ------------------------------------------------------------------
    # Prompt loading
    # ------------------------------------------------------------------

    def load_prompt_from_file(self, prompt_name: str) -> Optional[str]:
        """Load the first usable line from a prompt .txt file."""
        prompt_file = self.prompts_dir / f"{prompt_name}.txt"

        if not prompt_file.exists():
            print(f"Prompt file not found: {prompt_file}")
            return None

        with open(prompt_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    return line

        print(f"No usable prompt found in: {prompt_file}")
        return None

    def list_available_prompts(self) -> List[str]:
        """Return a sorted list of prompt names (without .txt extension)."""
        if not self.prompts_dir.exists():
            return []
        return sorted(p.stem for p in self.prompts_dir.glob("*.txt"))

    # ------------------------------------------------------------------
    # Ambient video prompt builder
    # ------------------------------------------------------------------

    def build_video_prompt(self, image_prompt: str) -> str:
        """Extend an image prompt with ambient motion keywords."""
        return (
            f"{image_prompt}, gentle ambient motion, subtle wind through the environment, "
            "slow camera drift, seamless loop feel, cinematic, no text, no titles"
        )

    # ------------------------------------------------------------------
    # ComfyUI: image workflow (1080x1920, Flux 2 Klein)
    # ------------------------------------------------------------------

    def queue_image(self, prompt: str, output_prefix: str) -> Optional[str]:
        """Queue a portrait image generation for a single ambient scene."""
        scene_number = 1
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
                    "width": 1080,
                    "height": 1920,
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
                    "noise_seed": int(time.time() * 1000) % (2**32) + scene_number
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
                    "filename_prefix": f"{output_prefix}_scene_001",
                    "images": ["12", 0]
                },
                "class_type": "SaveImage"
            }
        }

        payload = {
            "prompt": workflow,
            "client_id": f"ambient_image_{output_prefix}"
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

    # ------------------------------------------------------------------
    # ComfyUI: video workflow (512x896, LTX-2, 257 frames, 10fps)
    # ------------------------------------------------------------------

    def queue_video(self, image_filename: str, prompt: str, prompt_name: str) -> Optional[str]:
        """Queue an ambient portrait video generation."""
        output_prefix = f"reel_nature_ambient_{prompt_name}"
        seed = int(time.time() * 1000) % (2**32) + 1
        workflow = {
            "1": {
                "inputs": {
                    "ckpt_name": "ltx-2-19b-dev-fp8.safetensors"
                },
                "class_type": "CheckpointLoaderSimple"
            },
            "2": {
                "inputs": {
                    "text_encoder": "gemma_3_12B_it_fp4_mixed.safetensors",
                    "ckpt_name": "ltx-2-19b-dev-fp8.safetensors",
                    "device": "default"
                },
                "class_type": "LTXAVTextEncoderLoader"
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
                    "text": "blurry, low quality, still frame, watermark, overlay, titles, text, subtitles",
                    "clip": ["2", 0]
                },
                "class_type": "CLIPTextEncode"
            },
            "5": {
                "inputs": {
                    "positive": ["3", 0],
                    "negative": ["4", 0],
                    "frame_rate": 10.0
                },
                "class_type": "LTXVConditioning"
            },
            "6": {
                "inputs": {
                    "image": image_filename,
                    "upload": "image"
                },
                "class_type": "LoadImage"
            },
            "7": {
                "inputs": {
                    "positive": ["5", 0],
                    "negative": ["5", 1],
                    "vae": ["1", 2],
                    "image": ["6", 0],
                    "width": 512,
                    "height": 896,
                    "length": 257,  # 32x8+1 = 257 frames, ~25.7s at 10fps (~503 MiB, safe on 16GB)
                    "batch_size": 1,
                    "strength": 1.0
                },
                "class_type": "LTXVImgToVideo"
            },
            "8": {
                "inputs": {
                    "sampler_name": "euler"
                },
                "class_type": "KSamplerSelect"
            },
            "9": {
                "inputs": {
                    "steps": 20,
                    "max_shift": 2.05,
                    "base_shift": 0.95,
                    "stretch": True,
                    "terminal": 0.1
                },
                "class_type": "LTXVScheduler"
            },
            "10": {
                "inputs": {
                    "noise_seed": seed
                },
                "class_type": "RandomNoise"
            },
            "11": {
                "inputs": {
                    "model": ["1", 0],
                    "lora_name": "ltx-2-19b-distilled-lora-384.safetensors",
                    "strength_model": 1.0
                },
                "class_type": "LoraLoaderModelOnly"
            },
            "12": {
                "inputs": {
                    "model": ["11", 0],
                    "positive": ["7", 0],
                    "negative": ["7", 1],
                    "cfg": 1.0
                },
                "class_type": "CFGGuider"
            },
            "13": {
                "inputs": {
                    "noise": ["10", 0],
                    "guider": ["12", 0],
                    "sampler": ["8", 0],
                    "sigmas": ["9", 0],
                    "latent_image": ["7", 2]
                },
                "class_type": "SamplerCustomAdvanced"
            },
            "14": {
                "inputs": {
                    "samples": ["13", 0],
                    "vae": ["1", 2]
                },
                "class_type": "VAEDecode"
            },
            "15": {
                "inputs": {
                    "images": ["14", 0],
                    "fps": 10
                },
                "class_type": "CreateVideo"
            },
            "16": {
                "inputs": {
                    "video": ["15", 0],
                    "filename_prefix": f"video/{output_prefix}_scene_001",
                    "format": "mp4",
                    "codec": "h264"
                },
                "class_type": "SaveVideo"
            }
        }

        payload = {
            "prompt": workflow,
            "client_id": f"ambient_video_{output_prefix}"
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

    # ------------------------------------------------------------------
    # Metadata generation
    # ------------------------------------------------------------------

    def generate_batch_metadata(self, processed: List[Tuple[str, str]]):
        """Generate nature_ambient_batch_metadata.md in content/nature_ambient/."""
        ambient_dir = self.base_path / "content" / "nature_ambient"
        batch_info_file = ambient_dir / "batch_info.json"
        metadata_path = ambient_dir / "nature_ambient_batch_metadata.md"

        prompt_list_lines = "\n".join(
            f"- `{name}` → `reel_nature_ambient_{name}_scene_001`"
            for name, _ in processed
        )

        if batch_info_file.exists():
            with open(batch_info_file, 'r', encoding='utf-8') as f:
                info = json.load(f)

            hashtags_str = " ".join(info.get("hashtags", []))
            groups_str = ", ".join(info.get("suggested_groups", []))

            content = f"""# Nature Ambient Batch Metadata

## Batch Info
- **Style:** {info.get('style', 'Studio Ghibli painterly nature ambient')}
- **Scenes Processed:** {len(processed)}

## Processed Prompts
{prompt_list_lines}

## Shared Caption Template
{info.get('caption_template', '[Describe the scene briefly. Ask a calming question.]')}

## Hashtags
{hashtags_str}

## Call to Action
{info.get('cta', 'Save this for your next unwind session. Follow for more.')}

## Audio Recommendation
{info.get('audio_style', 'Soft ambient piano, lofi, or nature sounds (rain, wind, birds)')}

## Posting Times
{info.get('posting_times', 'Daily 8-10 AM or 9-11 PM (relaxation audience)')}

## Suggested Groups to Share In
{groups_str}

## Checklist
- [ ] Videos reviewed -- smooth loop, no jarring motion
- [ ] Captions written per scene
- [ ] Audio track added (looping)
- [ ] Thumbnail selected (most calming frame)
- [ ] Posted at optimal time
- [ ] Replied to comments within first hour
"""
        else:
            content = f"""# Nature Ambient Batch Metadata

## Batch Info
- **Style:** Studio Ghibli painterly nature ambient
- **Scenes Processed:** {len(processed)}

## Processed Prompts
{prompt_list_lines}

## Shared Caption Template
[Describe the scene briefly. Ask a calming question, e.g. "Which one calms you most?"]

## Hashtags
[Add 5-10 hashtags, e.g. #naturereels #ambientvideo #relaxing #calmdown]

## Call to Action
Save this for your next unwind session. Follow for more.

## Audio Recommendation
Soft ambient piano, lofi beats, or natural sounds (rain, wind, birds)

## Posting Times
Daily 8-10 AM or 9-11 PM (relaxation / sleep preparation audience)

## Checklist
- [ ] Videos reviewed -- smooth loop, no jarring motion
- [ ] Captions written per scene
- [ ] Audio track added (looping)
- [ ] Thumbnail selected (most calming frame)
- [ ] Posted at optimal time
- [ ] Replied to comments within first hour
"""

        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"   Batch metadata saved: {metadata_path}")

    # ------------------------------------------------------------------
    # Core run logic
    # ------------------------------------------------------------------

    def process_prompt(self, prompt_name: str) -> Optional[Tuple[str, str]]:
        """Process a single ambient prompt: queue image then video.

        Returns (prompt_name, image_filename) on success, None on failure.
        """
        image_prompt = self.load_prompt_from_file(prompt_name)
        if not image_prompt:
            return None

        output_prefix = f"reel_nature_ambient_{prompt_name}"
        # The expected output filename from ComfyUI (first file, batch index 1)
        expected_image_filename = f"{output_prefix}_scene_001_00001_.png"

        display_prompt = image_prompt[:65] + "..." if len(image_prompt) > 65 else image_prompt
        print(f"\n  Prompt:  {display_prompt}")
        print(f"  Prefix:  {output_prefix}")

        # Phase 1: queue image
        print(f"  [Phase 1] Queuing portrait image (1080x1920)...")
        img_id = self.queue_image(image_prompt, output_prefix)
        if img_id:
            print(f"            Queued (ID: {img_id[:8]}...)")
        else:
            print(f"            Failed - skipping video queue for {prompt_name}")
            return None

        time.sleep(0.3)

        # Phase 2: queue video using expected image filename
        video_prompt = self.build_video_prompt(image_prompt)
        print(f"  [Phase 2] Queuing ambient video (512x896, 257 frames, 10fps)...")
        print(f"            Image ref: {expected_image_filename}")

        vid_id = self.queue_video(expected_image_filename, video_prompt, prompt_name)
        if vid_id:
            print(f"            Queued (ID: {vid_id[:8]}...)")
        else:
            print(f"            Video queue failed for {prompt_name}")
            return None

        time.sleep(0.3)
        return (prompt_name, expected_image_filename)

    def run(self, prompt_names: List[str]):
        """Run the full batch for the given list of prompt names."""
        print("=" * 70)
        print(f"  Nature Ambient Batch - {len(prompt_names)} prompt(s)")
        print("=" * 70)
        print()
        print("  NOTE: Images are queued first, then videos.")
        print("  ComfyUI processes them sequentially.")
        print("  The video job references the image by its expected output")
        print("  filename. If images are not yet in C:/ComfyUI/input/,")
        print("  the video job will fail when it runs.")
        print("  Tip: Let images finish generating, then manually copy them")
        print("  to C:/ComfyUI/input/ before the video jobs start.")
        print()

        processed: List[Tuple[str, str]] = []
        failed: List[str] = []

        for prompt_name in prompt_names:
            print("-" * 50)
            print(f"Processing: {prompt_name}")
            result = self.process_prompt(prompt_name)
            if result:
                processed.append(result)
            else:
                failed.append(prompt_name)

        print()
        print("=" * 70)
        print("  Batch Complete")
        print("=" * 70)
        print(f"  Processed: {len(processed)}")
        print(f"  Failed:    {len(failed)}")
        if failed:
            print(f"  Failed items: {', '.join(failed)}")
        print(f"  Images output:  C:/ComfyUI/output/reel_nature_ambient_*")
        print(f"  Videos output:  C:/ComfyUI/output/video/reel_nature_ambient_*")
        print()

        if processed:
            self.generate_batch_metadata(processed)

        print("=" * 70 + "\n")


def main():
    """Main entry point."""
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "=" * 70)
    print("  Stage 3: Nature Ambient Batch (Flux 2 Klein + LTX-2, 512x896, 257f)")
    print("=" * 70 + "\n")

    generator = NatureAmbientGenerator()

    if len(sys.argv) < 2:
        available = generator.list_available_prompts()
        print("Usage:")
        print("  python 03_nature_ambient.py <prompt_name>")
        print("  python 03_nature_ambient.py all")
        print("\nExamples:")
        print("  python 03_nature_ambient.py moonlit_forest")
        print("  python 03_nature_ambient.py aurora_mountains")
        print("  python 03_nature_ambient.py all")
        if available:
            print(f"\nAvailable prompts in content/nature_ambient/prompts/:")
            for name in available:
                print(f"  - {name}")
        else:
            print(f"\nPrompts directory: {generator.prompts_dir}")
            print("  (no .txt files found)")
        print()
        sys.exit(1)

    arg = sys.argv[1]

    if arg.lower() == 'all':
        prompt_names = generator.list_available_prompts()
        if not prompt_names:
            print(f"No .txt files found in: {generator.prompts_dir}")
            sys.exit(1)
        print(f"Found {len(prompt_names)} prompt(s): {', '.join(prompt_names)}\n")
    else:
        prompt_names = [arg]

    generator.run(prompt_names)


if __name__ == "__main__":
    main()

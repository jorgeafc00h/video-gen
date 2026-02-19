#!/usr/bin/env python3
"""
Auto Batch Processor for ComfyUI - Enhanced Version
Automatically processes prompts from a text file (one per line).

Features:
- Drag & drop text file support
- Real-time progress tracking
- Automatic file watching mode
- No custom nodes required

Usage:
    python auto_batch_processor.py prompts.txt
    python auto_batch_processor.py prompts.txt --watch  (auto-reload when file changes)
"""

import json
import sys
import time
import requests
from pathlib import Path
from typing import List, Optional
import hashlib


class ComfyUIBatchProcessor:
    def __init__(self, comfyui_url: str = "http://127.0.0.1:8001"):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.workflow_template = self._load_workflow_template()

    def _load_workflow_template(self) -> dict:
        """Load the workflow JSON template."""
        workflow_path = Path(__file__).parent / "Flux 2 Klein 9B - Simple Batch (No Custom Nodes).json"

        if not workflow_path.exists():
            print(f"❌ Error: Workflow file not found: {workflow_path}")
            sys.exit(1)

        with open(workflow_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def check_comfyui_status(self) -> bool:
        """Check if ComfyUI is running."""
        try:
            response = requests.get(f"{self.comfyui_url}/system_stats", timeout=2)
            return response.status_code == 200
        except:
            return False

    def get_queue_status(self) -> dict:
        """Get current queue status."""
        try:
            response = requests.get(f"{self.comfyui_url}/queue")
            if response.status_code == 200:
                data = response.json()
                return {
                    'running': len(data.get('queue_running', [])),
                    'pending': len(data.get('queue_pending', []))
                }
        except:
            pass
        return {'running': 0, 'pending': 0}

    def queue_prompt_api(self, prompt_text: str, batch_number: int) -> Optional[str]:
        """Queue a prompt using ComfyUI API format."""
        # Build API-format workflow
        filename_prefix = f"Flux2-Klein-Batch_{batch_number:04d}_"

        api_workflow = {
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
                    "text": prompt_text,
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
                    "width": 1024,
                    "height": 1024,
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
                    "noise_seed": int(time.time() * 1000) % (2**32),
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
                    "filename_prefix": filename_prefix,
                    "images": ["12", 0]
                },
                "class_type": "SaveImage"
            }
        }

        payload = {
            "prompt": api_workflow,
            "client_id": f"batch_{batch_number}"
        }

        try:
            response = requests.post(f"{self.comfyui_url}/prompt", json=payload, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result.get('prompt_id')
            else:
                print(f"     Error: HTTP {response.status_code} - {response.text[:100]}")
                return None
        except Exception as e:
            print(f"     Error queuing prompt: {e}")
            return None

    def process_batch(self, prompts: List[str], show_progress: bool = True):
        """Process a batch of prompts."""
        if not prompts:
            print("⚠️  No prompts to process!")
            return

        print(f"\n{'='*70}")
        print(f"🚀 Batch Processing Started")
        print(f"{'='*70}")
        print(f"   ComfyUI: {self.comfyui_url}")
        print(f"   Prompts: {len(prompts)}")
        print(f"{'='*70}\n")

        successful = 0
        failed = 0
        prompt_ids = []

        for i, prompt in enumerate(prompts, start=1):
            # Truncate long prompts for display
            display_prompt = prompt[:65] + "..." if len(prompt) > 65 else prompt

            print(f"[{i:03d}/{len(prompts):03d}] {display_prompt}")

            prompt_id = self.queue_prompt_api(prompt, i)

            if prompt_id:
                successful += 1
                prompt_ids.append(prompt_id)
                print(f"          ✅ Queued (ID: {prompt_id[:8]}...)")
            else:
                failed += 1
                print(f"          ❌ Failed to queue")

            # Brief pause between requests
            if i < len(prompts):
                time.sleep(0.3)

        # Show final status
        print(f"\n{'='*70}")
        print(f"✨ Batch Processing Complete")
        print(f"{'='*70}")
        print(f"   ✅ Queued: {successful}")
        print(f"   ❌ Failed: {failed}")

        if successful > 0:
            queue_status = self.get_queue_status()
            print(f"   📊 Queue: {queue_status['running']} running, {queue_status['pending']} pending")

        print(f"{'='*70}\n")


def load_prompts(file_path: Path) -> List[str]:
    """Load prompts from a text file."""
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        prompts = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

    return prompts


def get_file_hash(file_path: Path) -> str:
    """Get hash of file contents for change detection."""
    if not file_path.exists():
        return ""

    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def watch_and_process(processor: ComfyUIBatchProcessor, file_path: Path):
    """Watch file for changes and auto-process."""
    print(f"\n👀 Watch mode enabled for: {file_path.name}")
    print(f"   Press Ctrl+C to stop watching\n")

    last_hash = ""

    try:
        while True:
            current_hash = get_file_hash(file_path)

            if current_hash and current_hash != last_hash:
                if last_hash:  # Not first run
                    print(f"\n🔄 File changed detected! Reloading...\n")

                prompts = load_prompts(file_path)

                if prompts:
                    print(f"📄 Loaded {len(prompts)} prompts from {file_path.name}")
                    processor.process_batch(prompts)
                    last_hash = current_hash
                else:
                    print(f"⚠️  No valid prompts found in {file_path.name}")

            time.sleep(2)  # Check every 2 seconds

    except KeyboardInterrupt:
        print(f"\n\n👋 Watch mode stopped.\n")


def main():
    """Main entry point."""
    import sys
    import io

    # Fix Windows console encoding for Unicode characters
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*70)
    print("  🎨 ComfyUI Auto Batch Processor")
    print("="*70 + "\n")

    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python auto_batch_processor.py <prompts_file>")
        print("  python auto_batch_processor.py <prompts_file> --watch")
        print("\nExample:")
        print("  python auto_batch_processor.py prompts.txt")
        print("  python auto_batch_processor.py prompts.txt --watch\n")
        sys.exit(1)

    prompts_file = Path(sys.argv[1])
    watch_mode = "--watch" in sys.argv or "-w" in sys.argv

    # Check ComfyUI URL
    comfyui_url = "http://127.0.0.1:8001"
    if "--url" in sys.argv:
        url_index = sys.argv.index("--url")
        if url_index + 1 < len(sys.argv):
            comfyui_url = sys.argv[url_index + 1]

    # Initialize processor
    processor = ComfyUIBatchProcessor(comfyui_url)

    # Check if ComfyUI is running
    print(f"🔍 Checking ComfyUI status...")
    if not processor.check_comfyui_status():
        print(f"❌ Cannot connect to ComfyUI at {comfyui_url}")
        print(f"   Please make sure ComfyUI is running!\n")
        sys.exit(1)

    print(f"✅ ComfyUI is running at {comfyui_url}\n")

    # Load and process
    if watch_mode:
        watch_and_process(processor, prompts_file)
    else:
        prompts = load_prompts(prompts_file)

        if not prompts:
            print(f"❌ No prompts found in {prompts_file}\n")
            sys.exit(1)

        print(f"📄 Loaded {len(prompts)} prompts from {prompts_file.name}\n")
        processor.process_batch(prompts)


if __name__ == "__main__":
    main()

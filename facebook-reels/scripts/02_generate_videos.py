#!/usr/bin/env python3
"""
Facebook Reels - Stage 2: Generate Portrait Videos
Uses the official LTX-2 i2v workflow template (720x1280 portrait, 481 frames, ~19.2s at 25fps).
Workflow includes spatial upscaler (ltx-2-spatial-upscaler-x2-1.0.safetensors).

Usage:
    python 02_generate_videos.py <content_type>/<story>
    python 02_generate_videos.py ghibli_mythology/01_norse_ragnarok
    python 02_generate_videos.py realistic_mythology/01_greek_prometheus
    python 02_generate_videos.py realistic_mythology/02_egyptian_ra_and_apep
"""

import copy
import json
import sys
import time
import shutil
import requests
from pathlib import Path
from typing import List, Tuple, Optional


class VideoGenerator:
    def __init__(self, comfyui_url: str = "http://127.0.0.1:8000"):
        self.comfyui_url = comfyui_url.rstrip('/')
        self.base_path = Path(__file__).parent.parent
        self.comfyui_input_path = Path("C:/ComfyUI/input")
        self.comfyui_output_path = Path("C:/ComfyUI/output")

        # Load the official LTX-2 i2v API workflow template once
        template_path = self.base_path / "video_ltx2_image2video api.json"
        with open(template_path, 'r', encoding='utf-8') as f:
            self._workflow_template = json.load(f)

    def load_video_prompts(self, story_path: Path) -> List[str]:
        """Load video prompts from file."""
        prompts_file = story_path / "video_prompts.txt"

        if not prompts_file.exists():
            raise FileNotFoundError(f"Video prompts file not found: {prompts_file}")

        with open(prompts_file, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        return prompts

    def find_generated_images(self, content_type: str, story_folder: str) -> List[Path]:
        """Find images generated in Stage 1, filtered to _00001_ to avoid duplicates."""
        pattern = f"reel_{content_type}_{story_folder}_scene_*_00001*.png"
        images = sorted(self.comfyui_output_path.glob(pattern))
        return images

    def get_scene_number(self, image_path: Path) -> int:
        """Extract scene number from image filename.

        Example: reel_ghibli_mythology_01_norse_ragnarok_scene_003_00001_.png -> 3
        """
        stem = image_path.stem
        if '_scene_' in stem:
            after_scene = stem.split('_scene_')[1]
            scene_part = after_scene.split('_')[0]
            try:
                return int(scene_part)
            except ValueError:
                pass
        return 0

    def prepare_image_for_comfyui(self, image_path: Path) -> str:
        """Copy image to ComfyUI input folder and return filename."""
        dest = self.comfyui_input_path / image_path.name
        if not dest.exists():
            self.comfyui_input_path.mkdir(parents=True, exist_ok=True)
            shutil.copy2(image_path, dest)
        return image_path.name

    def queue_video(
        self,
        image_filename: str,
        prompt: str,
        scene_number: int,
        content_type: str,
        story_folder: str
    ) -> Optional[str]:
        """Queue a single video generation using the official LTX-2 i2v workflow template.

        Substitutes 5 fields in the template per scene:
          - node 102   (ResizeImageMaskNode): portrait dimensions 720x1280
          - node 98    (LoadImage):           image filename
          - node 92:3  (CLIPTextEncode):      positive prompt
          - node 92:11 (RandomNoise):         seed
          - node 75    (SaveVideo):           filename_prefix
        Everything else (spatial upscaler, two-pass sampler, 481 frames) stays as-is.
        """
        seed = int(time.time() * 1000) % (2**32) + scene_number
        workflow = copy.deepcopy(self._workflow_template)

        # Portrait 9:16 for Reels
        workflow["102"]["inputs"]["resize_type.width"] = 720
        workflow["102"]["inputs"]["resize_type.height"] = 1280

        workflow["98"]["inputs"]["image"] = image_filename
        workflow["92:3"]["inputs"]["text"] = prompt
        workflow["92:11"]["inputs"]["noise_seed"] = seed
        workflow["75"]["inputs"]["filename_prefix"] = (
            f"video/reel_{content_type}_{story_folder}_scene_{scene_number:03d}"
        )

        payload = {
            "prompt": workflow,
            "client_id": f"reel_video_gen_{scene_number}"
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

    def generate_metadata(
        self,
        story_path: Path,
        content_type: str,
        story_folder: str,
        queued_count: int
    ):
        """Generate reel_metadata.md for posting workflow."""
        info_file = story_path / "story_info.json"
        metadata_path = story_path / "reel_metadata.md"

        if info_file.exists():
            with open(info_file, 'r', encoding='utf-8') as f:
                info = json.load(f)

            hashtags_str = " ".join(info.get("hashtags", []))
            groups_str = ", ".join(info.get("suggested_groups", []))

            content = f"""# Reel Metadata: {info.get('title', story_folder)}

## Información del Contenido
- **Estilo:** {info.get('style', 'N/A')}
- **Videos Generados:** {queued_count} escenas

## Hook (Primeros 3 segundos)
> {info.get('hook_text', '')}

## Descripción
{info.get('caption', '')}

## Hashtags
{hashtags_str}

## Llamada a la Acción
{info.get('cta', '')}

## Recomendación de Audio
{info.get('audio_style', '')}

## Horarios de Publicación
{info.get('posting_times', '')}

## Grupos Sugeridos para Compartir
{groups_str}

## Lista de Verificación
- [ ] Videos revisados y seleccionadas las mejores tomas
- [ ] Descripción finalizada
- [ ] Pista de audio añadida
- [ ] Miniatura seleccionada (fotograma de mayor impacto)
- [ ] Publicado en el horario óptimo
- [ ] Respondido comentarios en la primera hora
"""
        else:
            content = f"""# Reel Metadata: {story_folder}

## Información del Contenido
- **Estilo:** [Completar estilo]
- **Videos Generados:** {queued_count} escenas

## Hook (Primeros 3 segundos)
> [Escribe tu hook — declaración dramática o pregunta]

## Descripción
[Escribe tu descripción — historia breve + pregunta para engagement]

## Hashtags
[Añade 5-10 hashtags]

## Llamada a la Acción
[Ej: "Guarda esto y síguenos" o "Comenta tu respuesta abajo"]

## Recomendación de Audio
[Ej: "Orquesta épica" o "Piano ambiente suave"]

## Horarios de Publicación
Mar–Jue 7–9 AM o 7–9 PM (mejor engagement)

## Lista de Verificación
- [ ] Videos revisados y seleccionadas las mejores tomas
- [ ] Descripción finalizada
- [ ] Pista de audio añadida
- [ ] Miniatura seleccionada
- [ ] Publicado en el horario óptimo
- [ ] Respondido comentarios en la primera hora
"""

        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"   Metadata saved: {metadata_path}")

    def generate_all(self):
        """Generate videos for all content types and stories."""
        content_path = self.base_path / "content"

        print("\n" + "=" * 70)
        print("  Generating ALL reels videos")
        print("=" * 70)

        # ghibli_mythology and realistic_mythology
        for content_type in ["ghibli_mythology", "realistic_mythology"]:
            type_path = content_path / content_type
            if not type_path.exists():
                continue
            stories = sorted([d for d in type_path.iterdir() if d.is_dir()])
            for story_path in stories:
                self.generate(content_type, story_path.name)

        # nature_ambient — use image prompt as video prompt
        nature_prompts_path = content_path / "nature_ambient" / "prompts"
        if nature_prompts_path.exists():
            for pf in sorted(nature_prompts_path.glob("*.txt")):
                scene_name = pf.stem
                with open(pf, 'r', encoding='utf-8') as f:
                    prompt = f.read().strip()
                if not prompt:
                    continue
                # Find the generated image
                pattern = f"reel_nature_ambient_{scene_name}_scene_001_00001*.png"
                images = sorted(self.comfyui_output_path.glob(pattern))
                if not images:
                    print(f"   Skipping nature_ambient/{scene_name} — image not found yet")
                    continue
                image_filename = self.prepare_image_for_comfyui(images[0])
                print("=" * 70)
                print(f"Stage 2: Video Generation - nature_ambient/{scene_name}")
                print("=" * 70)
                display = prompt[:60] + "..." if len(prompt) > 60 else prompt
                print(f"[001] {display}")
                print(f"      Image: {images[0].name}")
                prompt_id = self.queue_video(image_filename, prompt, 1, "nature_ambient", scene_name)
                if prompt_id:
                    print(f"      Queued (ID: {prompt_id[:8]}...)")
                else:
                    print(f"      Failed")
                time.sleep(0.3)

        print("\n" + "=" * 70)
        print("  All videos queued!")
        print("=" * 70 + "\n")

    def generate(self, content_type: str, story_folder: str):
        """Generate all videos for a content type / story."""
        story_path = self.base_path / "content" / content_type / story_folder

        if not story_path.exists():
            print(f"Story path not found: {story_path}")
            print(f"   Expected: content/{content_type}/{story_folder}/")
            return

        print(f"\nProcessing: {content_type}/{story_folder}")
        print(f"   Path: {story_path}")

        # Load video prompts
        try:
            video_prompts = self.load_video_prompts(story_path)
            print(f"   Found {len(video_prompts)} video prompts")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        # Find generated images
        images = self.find_generated_images(content_type, story_folder)

        if not images:
            print(f"No images found for reel_{content_type}_{story_folder}_scene_*_00001*.png")
            print(f"   Searched in: {self.comfyui_output_path}")
            print(f"   Run Stage 1 first: python 01_generate_images.py {content_type}/{story_folder}")
            return

        print(f"   Found {len(images)} generated images")

        # Match images to prompts by scene number
        scene_pairs: List[Tuple[int, Path, str]] = []
        for image in images:
            scene_num = self.get_scene_number(image)
            if 1 <= scene_num <= len(video_prompts):
                prompt = video_prompts[scene_num - 1]
                scene_pairs.append((scene_num, image, prompt))
            else:
                print(f"   Warning: scene {scene_num} out of range (have {len(video_prompts)} prompts), skipping {image.name}")

        if not scene_pairs:
            print(f"Could not match any images to prompts")
            return

        print(f"   Matched {len(scene_pairs)} image/prompt pairs\n")

        # Generate videos
        successful = 0
        failed = 0

        print("=" * 70)
        print(f"Stage 2: Video Generation (LTX-2 i2v, 720x1280, 481f, spatial upscaler)")
        print(f"         {content_type}/{story_folder}")
        print("=" * 70)

        for scene_num, image_path, prompt in scene_pairs:
            image_filename = self.prepare_image_for_comfyui(image_path)

            display_prompt = prompt[:60] + "..." if len(prompt) > 60 else prompt
            print(f"[{scene_num:03d}] {display_prompt}")
            print(f"      Image: {image_path.name}")

            prompt_id = self.queue_video(image_filename, prompt, scene_num, content_type, story_folder)

            if prompt_id:
                print(f"      Queued (ID: {prompt_id[:8]}...)")
                successful += 1
            else:
                print(f"      Failed")
                failed += 1

            time.sleep(0.3)

        print("\n" + "=" * 70)
        print(f"Complete - {content_type}/{story_folder}")
        print("=" * 70)
        print(f"   Queued:  {successful}")
        print(f"   Failed:  {failed}")
        print(f"   Output:  C:/ComfyUI/output/video/")

        # Generate metadata file
        print()
        self.generate_metadata(story_path, content_type, story_folder, successful)
        print("=" * 70 + "\n")


def main():
    """Main entry point."""
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "=" * 70)
    print("  Stage 2: Video Generation (LTX-2 i2v, 720x1280, 481f, spatial upscaler)")
    print("=" * 70 + "\n")

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python 02_generate_videos.py <content_type>/<story_folder>")
        print("\nExamples:")
        print("  python 02_generate_videos.py ghibli_mythology/01_norse_ragnarok")
        print("  python 02_generate_videos.py ghibli_mythology/02_japanese_amaterasu")
        print("  python 02_generate_videos.py realistic_mythology/01_greek_prometheus")
        print("  python 02_generate_videos.py realistic_mythology/02_egyptian_ra_and_apep")
        print("\nNote: Run Stage 1 first to generate images!")
        print("      Images must be in C:/ComfyUI/output/ matching:")
        print("      reel_<content_type>_<story_folder>_scene_*_00001*.png")
        print()
        sys.exit(1)

    arg = sys.argv[1]

    if '/' not in arg:
        print(f"Error: argument must be in format <content_type>/<story_folder>")
        print(f"   Got: {arg}")
        print(f"   Example: ghibli_mythology/01_norse_ragnarok")
        sys.exit(1)

    parts = arg.split('/', 1)
    content_type = parts[0]
    story_folder = parts[1]

    generator = VideoGenerator()
    generator.generate(content_type, story_folder)


if __name__ == "__main__":
    main()

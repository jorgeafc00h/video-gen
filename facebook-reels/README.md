# Facebook Reels AI Production Pipeline

## Overview

This pipeline produces short-form vertical video content for Facebook Reels using:

- **Flux 2 Klein** — AI image generation (1080x1920 portrait, 9:16)
- **LTX-2** — AI video generation (576x1024, ~20 seconds, 497 frames)

Content is organized into three thematic channels, each with its own visual style, audience, and posting strategy.

---

## Content Types

| Channel | Style | Description |
|---|---|---|
| `ghibli_mythology` | Studio Ghibli watercolor anime | Ancient myths retold in soft painterly Ghibli aesthetic |
| `realistic_mythology` | Hyper-realistic cinematic oil painting | Dramatic chiaroscuro mythology for mature audiences |
| `nature_ambient` | Studio Ghibli painterly | Calming ambient nature loops for relaxation content |

---

## Quick Start

### Step 1 — Generate Images

```bash
python BedTIme-tales/scripts/01_generate_images.py
```

Or with a custom ComfyUI URL:

```python
import importlib.util, sys
spec = importlib.util.spec_from_file_location("gen", "BedTIme-tales/scripts/01_generate_images.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
gen = mod.ImageGenerator('http://127.0.0.1:8000')
gen.run()
```

### Step 2 — Generate Videos

```bash
python BedTIme-tales/scripts/02_generate_videos.py
```

Key parameter: use **497 frames** for ~20s at 25fps (must be divisible by 8+1 pattern).

### Step 3 — Review and Post

- Check outputs in each story's `outputs/` folder
- Refer to `story_info.json` for caption, hashtags, CTA, and posting times
- See `GUIDELINES.md` for full Facebook Reels strategy

---

## Folder Structure

```
facebook-reels/
├── README.md                        # This file
├── GUIDELINES.md                    # Full Facebook Reels strategy guide
└── content/
    ├── ghibli_mythology/
    │   ├── 01_norse_ragnarok/
    │   │   ├── image_prompts.txt    # 3 portrait image prompts
    │   │   ├── video_prompts.txt    # 3 motion prompts
    │   │   └── story_info.json      # Caption, hashtags, CTA, audio
    │   └── 02_japanese_amaterasu/
    │       ├── image_prompts.txt
    │       ├── video_prompts.txt
    │       └── story_info.json
    ├── realistic_mythology/
    │   ├── 01_greek_prometheus/
    │   │   ├── image_prompts.txt
    │   │   ├── video_prompts.txt
    │   │   └── story_info.json
    │   └── 02_egyptian_ra_and_apep/
    │       ├── image_prompts.txt
    │       ├── video_prompts.txt
    │       └── story_info.json
    └── nature_ambient/
        ├── batch_info.json          # Shared hashtags, captions, audio
        └── prompts/
            ├── moonlit_forest.txt
            ├── aurora_mountains.txt
            ├── rain_cherry_blossoms.txt
            ├── ocean_sunrise.txt
            └── bamboo_mist.txt
```

---

## Key Technical Specs

| Parameter | Value |
|---|---|
| Image resolution | 1080 x 1920 px (portrait 9:16) |
| Video resolution | 576 x 1024 px |
| Video duration | ~20 seconds |
| Frame count | 497 frames |
| Frame rate | 25 fps |
| ComfyUI URL | http://127.0.0.1:8000 |

---

## Workflow Per Story

1. Write / review `image_prompts.txt` — one prompt per line, no blank lines
2. Generate images via Flux 2 Klein (ComfyUI workflow)
3. Write / review `video_prompts.txt` — one motion description per line
4. Generate videos via LTX-2 (497 frames, 576x1024)
5. Trim, color-grade, add audio in your editor
6. Copy caption + hashtags from `story_info.json`
7. Post at recommended times from `GUIDELINES.md`

---

## Notes

- All image prompts are written for **portrait (vertical) orientation** — do not use landscape framing keywords
- LTX-2 frame count must satisfy `(n - 1) % 8 == 0` — valid values: 97, 121, 169, 241, 481, 497...
- For ambient nature content, a single looping clip per scene is the goal (no cuts)
- See `GUIDELINES.md` for hook writing, caption strategy, and monetization notes

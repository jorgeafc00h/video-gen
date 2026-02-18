# 🎬 Bedtime Tales - Automated Story Video Generation

Complete pipeline for generating narrated bedtime story videos using a two-stage workflow:
1. **Stage 1:** Generate images (Flux 2 Klein) - Start frames for each scene
2. **Stage 2:** Generate videos (LTX2) - Animate with narration + classical music

**NEW:** Dual-language support with Spanish narrator & English character voices!

---

## 📁 Folder Structure

```
BedTIme-tales/
├── stories/
│   ├── 01_lumi_bunny/
│   │   ├── 01_image_prompts.txt                  # For Flux 2 Klein
│   │   ├── 02_video_prompts_spanish.txt          # Spanish narrator
│   │   ├── 02_video_prompts_english_optimized.txt # English character voices
│   │   ├── spanish_narration.txt                  # Spanish script
│   │   └── english_narration.txt                  # English dialog script
│   ├── 02_bruno_bear/
│   ├── 03_gatita_nube/
│   ├── 04_cierva_rio/
│   └── 05_zorro_luna/
│
├── scripts/
│   ├── 01_generate_images.py                      # Stage 1: Generate images
│   ├── 02_generate_videos_spanish.py              # Stage 2: Spanish version
│   └── 02_generate_videos_english.py              # Stage 2: English version
│
├── workflows/
│   └── ltx2_image_to_video.json                   # LTX2 workflow reference
│
├── LTX2_OPTIMIZATION_GUIDE.md                     # Prompt optimization guide
├── PROMPT_FORMAT_WITH_MUSIC.md                    # Classical music guide
└── README.md                                       # This file
```

---

## ⚡ Quick Start

### Prerequisites
```bash
pip install requests
```

### Complete Workflow Example (Spanish)

```bash
# Navigate to scripts directory
cd "c:\repos\video-gen\BedTIme-tales\scripts"

# Stage 1: Generate all scene images (16 scenes)
python 01_generate_images.py lumi_bunny

# Wait for images to complete (check C:\ComfyUI\output\)

# Stage 2: Generate videos with Spanish narration
python 02_generate_videos_spanish.py lumi_bunny

# Done! Videos in C:\ComfyUI\output\
```

### Complete Workflow Example (English with Character Voices)

```bash
# Stage 1: Same as above
python 01_generate_images.py lumi_bunny

# Stage 2: Generate with English character voices
python 02_generate_videos_english.py lumi_bunny

# Done! Each character has their own voice!
```

---

## 🎨 Stage 1: Image Generation

### Purpose
Generate static images for each scene using Flux 2 Klein.
These become the first frame for video generation.

### Usage
```bash
# Single story
python 01_generate_images.py lumi_bunny
python 01_generate_images.py bruno_bear

# All stories (80 images total - 16 per story × 5 stories)
python 01_generate_images.py all
```

### Output
Images saved to: `C:\ComfyUI\output\`

Format: `<story>_scene_<number>_<batch>.png`

Examples:
```
01_lumi_bunny_scene_001_00001.png
01_lumi_bunny_scene_002_00001.png
...
01_lumi_bunny_scene_016_00001.png
```

---

## 🎬 Stage 2: Video Generation with Narration

### Purpose
Animate images using LTX2 image-to-video with:
- Classical music background
- Narration (Spanish or English)
- Character voices (English only)

### Spanish Version (Single Narrator)
```bash
python 02_generate_videos_spanish.py lumi_bunny
```

**Features:**
- Single warm maternal narrator voice
- Spanish language narration
- Classical music background
- 20 seconds per scene

### English Version (Character Voices)
```bash
python 02_generate_videos_english.py lumi_bunny
```

**Features:**
- Multiple character voices:
  - NARRATOR: Soft maternal voice
  - LUMI: Young innocent child voice
  - WISE OWL: Deep grandfatherly voice
  - CRICKET: Cheerful friendly voice
- English language dialogue
- Classical music background
- 20 seconds per scene

### Output
Videos saved to: `C:\ComfyUI\output\`

**Video specs:**
- Duration: 20 seconds per scene (480 frames at 24fps)
- Resolution: 1280x720 (HD)
- Total story: 16 scenes = ~5 minutes 20 seconds

Formats:
- `.webp` (animated WEBP)
- `.mp4` (via VHSVideoCombine)

Examples:
```
01_lumi_bunny_scene_001.webp  (Spanish or English)
01_lumi_bunny_scene_001.mp4   (Spanish or English)
...
```

---

## 🎵 Classical Music + Narration

### Music Background
All videos include soothing classical music:
- Brahms' Lullaby (calming)
- Debussy's Clair de Lune (peaceful)
- Chopin's Nocturnes (soothing)
- Tchaikovsky's Nutcracker (magical)
- Bach, Mozart, Vivaldi (various moods)

**Audio levels:**
- Music: -18dB to -22dB (background)
- Narrator: -8dB (clear, primary)
- Characters: -9dB to -10dB (clear)

### Narration Files

Each story includes:
- `spanish_narration.txt` - Full Spanish script with narrator
- `english_narration.txt` - Full English script with character voices

---

## 📊 Complete Example: Lumi Bunny Story

### 1. Prepare (Already Done!)

Files exist:
- ✅ `01_image_prompts.txt` (16 image prompts)
- ✅ `02_video_prompts_spanish.txt` (Spanish narration)
- ✅ `02_video_prompts_english_optimized.txt` (English character voices)
- ✅ `spanish_narration.txt` (Spanish script)
- ✅ `english_narration.txt` (English dialog)

### 2. Generate Images

```bash
cd scripts
python 01_generate_images.py lumi_bunny
```

Output: 16 images queued

### 3. Wait for Images

Check `C:\ComfyUI\output\` - wait for all 16 images.

### 4A. Generate Videos (Spanish)

```bash
python 02_generate_videos_spanish.py lumi_bunny
```

Result: 16 videos with Spanish narrator

### 4B. Generate Videos (English)

```bash
python 02_generate_videos_english.py lumi_bunny
```

Result: 16 videos with English character voices

### 5. Done!

Total per language:
- 16 scenes × 20 seconds = **5 minutes 20 seconds**
- Complete narrated bedtime story!

---

## 📚 All Available Stories

| Story | Folder | Scenes | Style | Languages |
|-------|--------|--------|-------|-----------|
| Lumi the Bunny | `01_lumi_bunny` | 16 | Watercolor | ES + EN ✅ |
| Bruno the Bear | `02_bruno_bear` | 16 | Pixar | ES + EN |
| Gatita Nube | `03_gatita_nube` | 16 | Anime | ES + EN |
| La Pequeña Cierva | `04_cierva_rio` | 16 | Watercolor | ES + EN |
| El Pequeño Zorro | `05_zorro_luna` | 16 | Watercolor | ES + EN |

**Total:** 80 scenes across 5 stories = ~26 minutes per language

---

## ⚙️ Configuration

### Video Length (20 seconds)

Edit `scripts/02_generate_videos_*.py` line ~110:

```python
"length": 480,   # 480 frames ÷ 24fps = 20 seconds
                 # Alternatives: 240 (10s), 360 (15s), 600 (25s)
```

### Video Resolution

Edit around line ~130:

```python
"width": 1280,   # 720p HD
"height": 720,   # Standard: 512, 720, 1080
```

### Generation Steps (Quality)

Edit around line ~140:

```python
"steps": 30,     # 20 (fast), 30 (balanced), 40 (high quality)
```

---

## 🎯 LTX2 Optimization

### Token Limits
**Critical:** LTX2 has ~200-250 token limit per prompt!

**Optimal prompt length:** 120-150 words

See `LTX2_OPTIMIZATION_GUIDE.md` for:
- Detailed optimization strategies
- Word count guidelines
- Character voice specifications
- Music integration best practices

### Prompt Structure
```
[Art Style] [Scene] [Camera 20s] [Lens] [Colors] [Motion] 24fps.
MUSIC: [Piece] [tempo]BPM vol -[dB]dB. [CHARACTER]: ([voice]) "[dialog]"
```

---

## 🌍 Language Versions

### Spanish (Narrator-Focused)
- **File:** `02_video_prompts_spanish.txt`
- **Voice:** Single warm maternal narrator
- **Style:** Storyteller reading bedtime tale
- **Simpler:** ~100-120 words per prompt

### English (Character-Focused)
- **File:** `02_video_prompts_english_optimized.txt`
- **Voices:** Multiple characters (Lumi, Owl, Cricket, etc.)
- **Style:** Interactive story with character dialogue
- **Complex:** ~120-150 words per prompt

---

## 👥 Character Voice Guide

### Voice Specifications (English)

**NARRATOR:**
```
(soft warm maternal voice) vol -8dB
```

**LUMI (Bunny):**
```
(young innocent child voice, high-pitched, gentle) vol -10dB
```

**WISE OWL:**
```
(deep gentle grandfatherly voice, calm reassuring) vol -9dB
```

**CRICKET:**
```
(cheerful friendly voice, slightly high pitch) vol -10dB
```

**MOTHER BUNNY:**
```
(warm loving adult female voice, protective) vol -9dB
```

---

## 🔧 Troubleshooting

### "No images found for story"
- Run Stage 1 first: `python 01_generate_images.py <story>`
- Check images exist in `C:\ComfyUI\output\`

### "Could not match images to prompts"
- Ensure image filenames follow pattern: `<story>_scene_<num>.png`
- Check scene numbers match (001-016)

### "Module 'requests' not found"
```bash
pip install requests
```

### "Cannot connect to ComfyUI"
- Make sure ComfyUI is running
- Default URL: `http://127.0.0.1:8001`

### "Prompt too long error"
- Use `*_optimized.txt` files
- Check word count: should be 120-180 words
- See `LTX2_OPTIMIZATION_GUIDE.md`

---

## 💡 Tips

### Process All Stories
```bash
# Images for all stories (80 images)
python 01_generate_images.py all

# Spanish versions (80 videos)
python 02_generate_videos_spanish.py all

# English versions (80 videos)
python 02_generate_videos_english.py all
```

### Combine Scenes into Single Video
After generation, use ffmpeg to combine all scenes:

```bash
# Create file list
ls -1 01_lumi_bunny_scene_*.mp4 > scenes.txt

# Concatenate
ffmpeg -f concat -i scenes.txt -c copy lumi_complete_spanish.mp4
```

### Monitor Progress
```
Watch: C:\ComfyUI\output\
```

Images appear first, then videos process.

---

## 🎯 Workflow Summary

```
Text Prompts
     ↓
     ├─→ Image Prompts → [Flux 2 Klein] → Images (16)
     │                                        ↓
     └─→ Video Prompts (ES/EN)                │
              ↓                                │
         [LTX2 Image-to-Video] ←──────────────┘
              ↓
         Spanish: Single narrator
         English: Character voices
              ↓
         + Classical Music
              ↓
         Complete Story Videos! 🎬
```

---

## 🚀 Quick Reference

```bash
# Setup (once)
pip install requests

# Full Spanish workflow
cd "c:\repos\video-gen\BedTIme-tales\scripts"
python 01_generate_images.py lumi_bunny
python 02_generate_videos_spanish.py lumi_bunny

# Full English workflow
python 01_generate_images.py lumi_bunny
python 02_generate_videos_english.py lumi_bunny

# All stories, all languages
python 01_generate_images.py all
python 02_generate_videos_spanish.py all
python 02_generate_videos_english.py all
```

---

## 📖 Documentation Files

- **`README.md`** (this file) - Complete guide
- **`LTX2_OPTIMIZATION_GUIDE.md`** - Prompt optimization & token limits
- **`PROMPT_FORMAT_WITH_MUSIC.md`** - Classical music integration guide

---

**Complete narrated bedtime stories with classical music in two languages! 🌙✨**

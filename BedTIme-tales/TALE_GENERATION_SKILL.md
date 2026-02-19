# 🌙 Bedtime Tale Generation Skill

**Purpose:** Create complete bedtime story content optimized for LTX2 video generation with background music.

**Output:** Ready-to-use files for automated image and video generation, plus a separate Spanish narration script.

---

## 📋 Story Requirements

### Structure
- **16 scenes** per tale
- **~19 seconds** per scene (481 frames at 25fps)
- **Total duration:** ~5 minutes
- **Target audience:** Children 3-7 years old
- **Purpose:** Bedtime relaxation, sleep induction

### Theme Requirements
- ✅ Gentle, calming, reassuring
- ✅ Nature-based or magical settings
- ✅ Simple conflict with peaceful resolution
- ✅ Educational (emotional learning, overcoming fears)
- ❌ No scary elements
- ❌ No loud/jarring actions
- ❌ No complex plots

---

## 🎨 Art Style Options

Choose ONE style per tale:

### Watercolor
- Soft brushstrokes, paper texture visible
- Translucent washes, bleeding edges
- Gentle color gradients
- Perfect for: Nature stories, gentle animals
- Examples: Lumi Bunny, Cierva Rio, Zorro Luna, Tortuga Serena, Dragoncito Chispa

### Pixar 3D
- Photorealistic fur/textures
- Subsurface scattering, volumetric lighting
- Cinematic quality, rich colors
- Perfect for: Character-driven stories, emotional journeys
- Examples: Bruno Bear, Elefante Nube

### Anime (Studio Ghibli-inspired)
- Soft cel-shaded, clean ink-wash lines
- Vibrant colors, expressive characters
- Gentle magical effects
- Perfect for: Magical creatures, fantasy elements
- Examples: Gatita Nube, Panda Mochi

### Painterly Digital Art
- Rich vivid brushwork, dreamlike quality
- Spectacular color and light
- Perfect for: Epic natural phenomena, aurora borealis, ocean
- Example: Pinguino Polo

---

## 📖 16-Scene Story Arc Template

### Act 1: Setup (Scenes 1-4)
**Scene 1:** Establish setting (wide shot, environment)
**Scene 2:** Introduce protagonist (character introduction)
**Scene 3:** Present gentle conflict/question (what will they learn?)
**Scene 4:** Meet mentor/guide (wise character appears)

### Act 2: Journey (Scenes 5-12)
**Scene 5:** Lesson begins (teaching moment)
**Scene 6:** Exploration (discovering new things)
**Scene 7:** Wonder moment (magical discovery)
**Scene 8:** Reflection (quiet contemplation)
**Scene 9:** Understanding grows (aha moment building)
**Scene 10:** Friendship (companion appears or deepens)
**Scene 11:** Realization (lesson learned)
**Scene 12:** Return journey (heading home)

### Act 3: Resolution (Scenes 13-16)
**Scene 13:** Arrival home (safe return)
**Scene 14:** Settling in (bedtime routine)
**Scene 15:** Peaceful sleep (character sleeping)
**Scene 16:** Closing tableau (wide shot, everything at peace)

---

## ✍️ Required Files per Tale

### File 1: `01_image_prompts.txt`
**Purpose:** Generate still images (Flux 2 Klein, 1920×1088)
**Format:** One prompt per line, 16 total
**Length:** 40-80 words per prompt
**Focus:** Rich visual description only — no motion, no audio

**Example:**
```
Pixar 3D animation of small brown bear cub Bruno with fluffy soft fur, round chubby body, big expressive brown eyes, sitting in golden meadow at twilight, looking upward at starry sky, warm rim lighting, cool blue sky gradient, wildflowers around, cinematic quality, 1920x1088 widescreen
```

### File 2: `02_video_prompts.txt`
**Purpose:** Guide LTX2 video generation (visual + motion only)
**Format:** One prompt per line, 16 total
**Length:** 60-100 words per prompt
**Includes:** Art style + Scene visuals + Character action + Camera movement + Lighting/atmosphere
**Does NOT include:** Narrator, dialog, music specs — music is added in post-production

**Structure:**
```
[Art style]. [Scene/setting description]. [Character description and action]. [Camera movement] over 20s, [lens]mm, f/[stop]. [Color/light palette]. [Motion/animation details]. [Atmosphere/mood].
```

**Example:**
```
Pixar 3D animation. Vast starlit meadow at twilight, deep blue sky transitioning to purple-pink horizon, thousands of twinkling stars, rolling hills with gently swaying grass. Slow crane-up revealing expansive sky over 20s, 35mm, f/2.8. Rich twilight palette, volumetric God rays filtering through distant trees. Grass swaying in gentle breeze, stars beginning to pulse softly, magical peaceful atmosphere.
```

### File 3: `narration_spanish.md`
**Purpose:** Full Spanish narration script — used for post-production voice recording, NOT embedded in video prompts
**Format:** Scene-by-scene markdown with character labels
**Length:** 1-3 sentences per scene

**Example:**
```markdown
## Escena 1 — El prado al atardecer

**NARRADOR:** En un prado tranquilo donde las estrellas brillan cada noche, vivía el osito Bruno.

## Escena 2 — Bruno mira las estrellas

**NARRADOR:** Bruno tenía el pelaje más suave y unos ojitos llenos de curiosidad.
**BRUNO:** *(curioso)* "¿Por qué brillan tanto las estrellas?"
```

---

## 🎥 Camera Specifications

### Lens Choices
- **35mm:** Wide shots, establishing, landscapes
- **50mm:** Medium shots, general scenes
- **85mm:** Close-ups, emotional moments, character focus

### F-Stops
- **f/1.8:** Extreme shallow depth, intimate moments
- **f/2.0:** Shallow depth, character focus
- **f/2.2:** Moderate depth, two-shots
- **f/2.8:** Standard depth, general scenes

### Camera Movements (always 20 seconds)
- **Pan:** Horizontal movement (landscape reveals)
- **Tilt:** Vertical movement (ground to sky)
- **Dolly-in:** Move toward subject (approaching, discovery)
- **Dolly-out/Zoom-out:** Move away (revealing scope)
- **Orbit:** Circular around subject (showing all sides)
- **Follow-shot:** Track behind/beside moving character
- **Push-in:** Slow approach to face (emotional beat)
- **Crane:** Ascending or descending (epic moments)

---

## 📏 LTX2 Video Prompt Optimization Rules

### CRITICAL: Keep Prompts Focused
- **No narrator text** — LTX2 generates visuals, not speech
- **No music specs** — music is added in post-production
- **No dialog** — LTX2 cannot render spoken words
- **Focus on:** what is seen, how it moves, how the camera moves

### Word Budget
```
Art Style:           5-8 words
Scene Visuals:       25-35 words
Character Action:    10-15 words
Camera/Technical:    10-15 words
Color/Atmosphere:    10-15 words
Motion Details:      10-15 words
TOTAL:               70-100 words
```

### Optimization Techniques

**Always include:**
- Art style keyword at start
- Essential visual description of scene
- Character description + what they are doing
- Camera movement with "over 20s"
- Lighting and color palette
- Motion/animation cues (swaying, breathing, twitching, etc.)

**Remove:**
- Any NARRATOR or CHARACTER dialog
- Music BPM, volume specs
- Redundant adjectives
- Overly detailed textures that LTX2 won't render

**Good Example:**
```
Watercolor animation. Cozy burrow entrance, soft earth tones, moss and flowers, warm golden light spilling from inside. White bunny Lumi approaching home slowly through moonlit night. Dolly-in to entrance over 20s, 50mm, f/2.2. Warm amber glow contrasting cool night blues. Lumi walking with gentle contentment, pausing to look back at stars, light spilling warmly from doorway.
```

---

## 🎯 Complete Tale Creation Workflow

### Step 1: Concept
```
1. Choose protagonist (animal, child-like)
2. Choose lesson (fear of dark, being alone, trying new things)
3. Choose art style (watercolor/Pixar/anime/painterly)
4. Choose setting (forest, garden, meadow, river, arctic, ocean)
5. Name characters (simple, memorable, often alliterative)
```

### Step 2: Story Outline
```
Create 16-scene structure following arc template:
- Act 1 (1-4): Setup
- Act 2 (5-12): Journey
- Act 3 (13-16): Resolution
```

### Step 3: Create Files

**File 1: `01_image_prompts.txt`**
```
- 16 lines (blank line between each)
- Visual description only
- 40-80 words each
- Include: art style, character, setting, lighting, resolution
- End with: 1920x1088 widescreen
```

**File 2: `02_video_prompts.txt`**
```
- 16 lines (blank line between each)
- LTX2 visual/motion prompts only
- 70-100 words each
- NO narrator, NO dialog, NO music
- Include: art style, scene, character action, camera, motion, atmosphere
```

**File 3: `narration_spanish.md`**
```
- Markdown format
- 16 scenes labeled with ## headers
- Spanish narrator + character dialog
- 1-3 sentences per scene
- Bold character labels: **NARRADOR:**, **PERSONAJE:**
```

### Step 4: Validate
```
1. Check video prompt word counts (70-100 words)
2. Verify NO narrator/dialog/music in video prompts
3. Ensure camera movement is described in each scene
4. Confirm art style is consistent throughout
5. Confirm narration_spanish.md covers all 16 scenes
```

### Step 5: Folder Structure
```
stories/
└── <number>_<story_name>/
    ├── 01_image_prompts.txt
    ├── 02_video_prompts.txt
    └── narration_spanish.md
```

---

## 📝 Character Creation Guidelines

### Protagonist Requirements
- **Age:** Child or young
- **Trait:** Curious, gentle, learning
- **Arc:** Overcomes small fear or learns valuable lesson
- **Examples:** Lumi (bunny), Bruno (bear), Gatita (kitten), Mochi (panda)

### Mentor/Guide Requirements
- **Age:** Wise, older
- **Trait:** Patient, kind, knowledgeable
- **Role:** Teaches without forcing, guides gently
- **Examples:** Wise Owl, Old Bear, Luna (moon sprite), Ancient Panda Spirit

### Friend Characters
- **Role:** Supportive, companionship
- **Examples:** Cricket, Fireflies, Nia (polar bear cub), Kiku (firefly)
- **Purpose:** Show protagonist is not alone

---

## ✅ Quality Checklist

### Story Content
- [ ] 16 scenes total
- [ ] Clear beginning, middle, end
- [ ] Gentle conflict, peaceful resolution
- [ ] Age-appropriate (3-7 years)
- [ ] Calming, sleep-inducing
- [ ] Educational/emotional learning

### 01_image_prompts.txt
- [ ] 16 prompts, one per line with blank line between
- [ ] Visual description only (no motion/audio)
- [ ] Art style consistent
- [ ] Resolution specified (1920x1088 widescreen)

### 02_video_prompts.txt
- [ ] 16 prompts, one per line with blank line between
- [ ] NO narrator, NO dialog, NO music specs
- [ ] Art style keyword at start of each
- [ ] Camera movement described in every scene
- [ ] Motion/animation cues included
- [ ] 70-100 words per prompt

### narration_spanish.md
- [ ] 16 scenes with ## headers
- [ ] Spanish narration for each scene
- [ ] Character voices labeled
- [ ] Calm, warm, bedtime tone

---

## 📋 Story Naming Convention

```
<number>_<character>_<setting>

Examples:
01_lumi_bunny          (Lumi the Bunny — Watercolor)
02_bruno_bear          (Bruno the Bear — Pixar)
03_gatita_nube         (Gatita the Cloud Kitten — Anime)
04_cierva_rio          (Little Deer and River — Watercolor)
05_zorro_luna          (Little Fox and Moon — Watercolor)
06_tortuga_serena      (Tortuga the Serene Turtle — Watercolor)
07_elefante_nube       (Elefante the Cloud Elephant — Pixar)
08_panda_mochi         (Panda Mochi — Anime/Ghibli)
09_pinguino_polo       (Penguin Polo — Painterly Digital)
10_dragoncito_chispa   (Little Dragon Chispa — Fantasy Watercolor)
```

---

## 🚀 Generation Commands

```bash
# Generate images (Flux 2 Klein, 1920x1088)
python scripts/01_generate_images.py <story_name>

# Generate videos (LTX2, 481 frames, 25fps)
python scripts/02_generate_videos.py <story_name>

# Generate all stories
python scripts/01_generate_images.py all
python scripts/02_generate_videos.py all
```

---

## ✨ Final Notes

**Purpose:** Help children sleep peacefully
**Approach:** Gentle, calming, reassuring visuals
**Video:** Pure visual storytelling + background music (no spoken narration in video)
**Narration:** Separate Spanish .md script for voice recording in post-production
**Duration:** ~5 minutes per story (16 scenes × ~19s each)
**Resolution:** 1920×1088 (both images and video)
**Result:** Beautiful bedtime videos with calming music

---

**Follow this skill document to create perfect bedtime tales every time! 🌙💫**

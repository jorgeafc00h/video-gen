# 🌙 Bedtime Tale Generation Skill

**Purpose:** Create complete bedtime story content optimized for LTX2 video generation with narration and classical music.

**Output:** Ready-to-use files for automated video generation in Spanish and English.

---

## 📋 Story Requirements

### Structure
- **16 scenes** per tale
- **20 seconds** per scene (480 frames at 24fps)
- **Total duration:** ~5 minutes 20 seconds
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
- Examples: Lumi Bunny, Cierva Rio, Zorro Luna

### Pixar 3D
- Photorealistic fur/textures
- Subsurface scattering, volumetric lighting
- Cinematic quality, rich colors
- Perfect for: Character-driven stories, emotional journeys
- Example: Bruno Bear

### Anime
- Cel-shaded, clean lines
- Vibrant colors, expressive characters
- Gentle magical effects
- Perfect for: Magical creatures, fantasy elements
- Example: Gatita Nube

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
**Scene 10:** Friendship (companion appears)
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
**Purpose:** Generate still images (Flux 2 Klein)
**Format:** One prompt per line, 16 total
**Length:** 30-50 words per prompt
**Focus:** Visual description only, no motion/audio

**Example:**
```
Beautiful watercolor white bunny, fluffy fur, pink ears, big eyes, golden meadow sunset, wildflowers, soft brushstrokes, paper texture, warm colors, dreamy storybook quality
```

### File 2: `02_video_prompts_spanish.txt`
**Purpose:** Generate videos with Spanish narration
**Format:** One prompt per line, 16 total
**Length:** 100-120 words per prompt (LTX2 limit!)
**Includes:** Visuals + Camera + Music + Spanish narrator

**Structure:**
```
[Art style] animation. [Scene visuals]. [Camera movement] 20s, [lens]mm, f/[stop].
[Color palette]. [Motion], 24fps. MUSIC: [Classical piece] [instrument], [tempo]BPM,
vol -[20-22]dB. NARRADOR: (voz maternal cálida) "[narración en español]" vol -8dB.
```

### File 3: `02_video_prompts_english_optimized.txt`
**Purpose:** Generate videos with English character voices
**Format:** One prompt per line, 16 total
**Length:** 120-150 words per prompt (LTX2 limit!)
**Includes:** Visuals + Camera + Music + Character voices

**Structure:**
```
[Art style] animation. [Scene visuals]. [Camera movement] 20s, [lens]mm, f/[stop].
[Color palette]. [Motion], 24fps. MUSIC: [Classical piece] [instrument], [tempo]BPM,
vol -[20-22]dB. NARRATOR: ([voice type]) "[narration]" vol -8dB. CHARACTER: ([voice type])
"[dialogue]" vol -[9-10]dB.
```

### File 4: `spanish_narration.txt`
**Purpose:** Full Spanish narration script
**Format:** Scene-by-scene dialogue with character labels
**Length:** 1-2 sentences per scene

**Example:**
```
[ESCENA 1 - Bosque al atardecer]
NARRADOR: En un bosque tranquilo, donde las estrellas cantan cada noche, vivía un conejito llamado Lumi.

[ESCENA 2 - Lumi aparece]
NARRADOR: Lumi era especial, con pelaje suave como nubes y ojitos curiosos.
```

### File 5: `english_narration.txt`
**Purpose:** Full English dialogue script with character voices
**Format:** Scene-by-scene with multiple characters
**Length:** 1-3 lines per scene

**Example:**
```
[SCENE 1 - Forest at Sunset]
NARRATOR: In a peaceful forest where stars sing, lived little bunny Lumi.

[SCENE 2 - Lumi Appears]
NARRATOR: Lumi was special, with fur soft as clouds and curious eyes.
LUMI: (young child voice) The night is so big and full of mysteries!
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

## 🎵 Classical Music Guide

### Scene Mood → Music Mapping

**Opening/Establishing (Scene 1):**
- Brahms' Lullaby - Piano
- 60 BPM, vol -20dB
- Calm, welcoming

**Introduction (Scenes 2-3):**
- Tchaikovsky Sugar Plum - Celesta/Flute
- 70 BPM, vol -19dB
- Gentle, magical

**Teaching Moments (Scenes 4-5):**
- Vivaldi Winter Largo - Strings
- Chopin Nocturne - Piano
- 55-68 BPM, vol -19 to -21dB
- Wise, contemplative

**Exploration (Scenes 6-7):**
- Beethoven Pastoral - Flute/Strings
- Grieg Morning Mood - Celesta/Harp
- 65-70 BPM, vol -19 to -20dB
- Wonder, discovery

**Reflection (Scenes 8-9):**
- Debussy Clair de Lune - Piano/Harp
- Satie Gymnopédie - Piano
- 50-58 BPM, vol -21 to -22dB
- Peaceful, meditative

**Friendship (Scene 10):**
- Mozart Nachtmusik - Woodwinds/Strings
- 72 BPM, vol -19dB
- Friendly, warm

**Resolution (Scene 11):**
- Pachelbel Canon - Strings
- 60 BPM, vol -20dB
- Understanding, acceptance

**Return (Scene 12):**
- Schubert Ave Maria - Piano/Strings
- 62 BPM, vol -20dB
- Homeward, safe

**Arrival (Scene 13):**
- Bach Air on G String - Violin/Piano
- 55 BPM, vol -21dB
- Home, comfort

**Bedtime (Scenes 14-15):**
- Brahms Lullaby - Piano
- Chopin Nocturne - Piano
- 40-48 BPM, vol -22 to -23dB
- Sleepy, peaceful

**Closing (Scene 16):**
- Piano/Strings fading to silence
- 40 BPM, vol -24dB to silence
- Complete peace

---

## 👥 Character Voice Specifications

### Narrator (Always Present)
```
NARRATOR: (soft warm maternal voice) vol -8dB
NARRADOR: (voz maternal cálida suave) vol -8dB
```

### Child Protagonists
```
(young innocent child voice, high-pitched, gentle) vol -10dB
(voz de niño inocente joven, aguda, gentil) vol -10dB
```

### Wise Mentors (Owls, Old Animals)
```
(deep gentle grandfatherly voice, calm reassuring) vol -9dB
(voz profunda abuelo gentil, calmada tranquilizadora) vol -9dB
```

### Adult Protective Characters (Parents)
```
(warm loving adult female/male voice, protective) vol -9dB
(voz adulta cariñosa femenina/masculina, protectora) vol -9dB
```

### Friend Characters (Insects, Small Animals)
```
(cheerful friendly voice, slightly high pitch) vol -10dB
(voz alegre amigable, tono ligeramente agudo) vol -10dB
```

---

## 📏 LTX2 Prompt Optimization Rules

### CRITICAL: Token Limits
- **Maximum:** 250 tokens (~180 words)
- **Optimal:** 150-180 tokens (~120-150 words)
- **Minimum:** 100 words (ensure detail)

### Word Budget Breakdown
```
Art Style:           5 words
Scene Visuals:       25-30 words
Camera/Technical:    12-15 words
Color/Atmosphere:    8-10 words
Motion:             8-10 words
Music:              15-20 words
Narration/Voices:   30-50 words
TOTAL:              120-150 words
```

### Optimization Techniques

**Remove:**
- Redundant adjectives
- Repetitive descriptions
- Over-detailed textures
- Multiple similar words

**Keep:**
- Art style keyword
- Essential visuals
- Camera specs (20s always!)
- Music reference
- Character voices
- Dialogue

**Example - Before (Too Long - 250 words):**
```
Beautiful watercolor painting animation with soft flowing brushstrokes and delicate
visible paper texture creating natural artistic quality. Tranquil peaceful serene forest
at golden sunset with painted purple and pink gradient sky featuring hand-painted
crescent moon and gentle watercolor stars with soft diffused edges...
```

**Example - After (Perfect - 130 words):**
```
Watercolor animation. Tranquil forest sunset, purple-pink sky, crescent moon, stars,
mountain silhouettes, meadow grass, wildflowers. Slow pan-right 20s, 35mm, f/2.8.
Golden palette, soft edges, dreamy quality. Gentle swaying, 24fps. MUSIC: Brahms
Lullaby piano-harp, 60BPM, vol -20dB, forest ambience. NARRATOR: (warm maternal)
"In peaceful forest where stars sing, lived little bunny Lumi." vol -8dB.
```

---

## 🌍 Language-Specific Guidelines

### Spanish Version
**Narration Style:** Single narrator reads the story
**Voice:** Warm maternal storyteller
**Tone:** Gentle bedtime story reading
**Word Count:** 100-120 words per prompt (simpler)

**Example Narration:**
```
NARRADOR: En un bosque tranquilo vivía un conejito llamado Lumi. Cada noche,
las estrellas cantaban para él mientras descubría los secretos de la noche mágica.
```

### English Version
**Narration Style:** Multiple character voices + narrator
**Voices:** Narrator + Character dialogue
**Tone:** Interactive story with character personalities
**Word Count:** 120-150 words per prompt (more complex)

**Example Dialogue:**
```
NARRATOR: (maternal voice) In a peaceful forest lived little bunny Lumi.
LUMI: (young child voice) The night is so big and mysterious!
NARRATOR: And so Lumi's adventure began.
```

---

## 📝 Character Creation Guidelines

### Protagonist Requirements
- **Age:** Child or young
- **Trait:** Curious, gentle, learning
- **Arc:** Overcomes small fear or learns valuable lesson
- **Examples:** Lumi (bunny), Bruno (bear), Gatita (kitten)

### Mentor/Guide Requirements
- **Age:** Wise, older
- **Trait:** Patient, kind, knowledgeable
- **Role:** Teaches without forcing, guides gently
- **Examples:** Wise Owl, Old Bear, Ancient Tree

### Friend Characters
- **Role:** Supportive, companionship
- **Examples:** Cricket, Fireflies, Small Birds
- **Purpose:** Show protagonist not alone

### Setting Characters (Optional)
- **Role:** Part of environment, magical elements
- **Examples:** Talking Flowers, Gentle Wind, Stars
- **Purpose:** Create magical atmosphere

---

## 🎯 Complete Tale Creation Workflow

### Step 1: Concept
```
1. Choose protagonist (animal, child-like)
2. Choose lesson (fear of dark, being alone, trying new things)
3. Choose art style (watercolor/Pixar/anime)
4. Choose setting (forest, garden, meadow, river)
5. Name characters (simple, memorable)
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
- 16 lines
- Visual description only
- 30-50 words each
- Focus on composition
```

**File 2: `spanish_narration.txt`**
```
- 16 scenes labeled
- Spanish dialogue
- 1-2 sentences per scene
```

**File 3: `english_narration.txt`**
```
- 16 scenes labeled
- Character names + voice types
- 1-3 lines per scene
```

**File 4: `02_video_prompts_spanish.txt`**
```
- 16 lines (one per scene)
- 100-120 words each
- Include: visuals + camera + music + Spanish narration
```

**File 5: `02_video_prompts_english_optimized.txt`**
```
- 16 lines (one per scene)
- 120-150 words each
- Include: visuals + camera + music + English character voices
```

### Step 4: Optimize
```
1. Check word counts (LTX2 limits!)
2. Verify music selections match mood
3. Ensure 20-second duration mentioned
4. Confirm voice types specified
5. Validate classical piece references
```

### Step 5: Folder Structure
```
stories/
└── <number>_<story_name>/
    ├── 01_image_prompts.txt
    ├── 02_video_prompts_spanish.txt
    ├── 02_video_prompts_english_optimized.txt
    ├── spanish_narration.txt
    └── english_narration.txt
```

---

## ✅ Quality Checklist

### Story Content
- [ ] 16 scenes total
- [ ] Clear beginning, middle, end
- [ ] Gentle conflict, peaceful resolution
- [ ] Age-appropriate (3-7 years)
- [ ] Calming, sleep-inducing
- [ ] Educational/emotional learning

### Technical Requirements
- [ ] All prompts optimized for LTX2 (120-180 words)
- [ ] 20-second duration mentioned in each scene
- [ ] Classical music specified with tempo/volume
- [ ] Character voices clearly defined
- [ ] Camera movements appropriate
- [ ] Art style consistent throughout

### File Requirements
- [ ] 5 files created per story
- [ ] Proper naming convention
- [ ] Correct folder structure
- [ ] Both Spanish and English versions

### Audio Specifications
- [ ] Music: -18dB to -22dB
- [ ] Narrator: -8dB
- [ ] Characters: -9dB to -10dB
- [ ] Tempo: 40-75 BPM (relaxing range)

---

## 📋 Story Naming Convention

```
<number>_<character>_<setting>

Examples:
01_lumi_bunny        (Lumi the Bunny)
02_bruno_bear        (Bruno the Bear)
03_gatita_nube       (Gatita Cloud/Nube)
04_cierva_rio        (Little Deer and River)
05_zorro_luna        (Little Fox and Moon)
06_ardilla_bosque    (Little Squirrel and Forest)
```

---

## 💡 Example Tale Prompts

### Tale 1: The Little Bunny (Watercolor)
**Protagonist:** Lumi, white bunny
**Lesson:** Night is not scary
**Style:** Watercolor, soft, dreamy
**Setting:** Forest, magical garden

### Tale 2: The Bear Cub (Pixar)
**Protagonist:** Bruno, brown bear
**Lesson:** You're never alone
**Style:** Pixar 3D, photorealistic
**Setting:** Meadow, starry night

### Tale 3: The Kitten (Anime)
**Protagonist:** Gatita, small kitten
**Lesson:** Dreams are beautiful
**Style:** Anime, cel-shaded, vibrant
**Setting:** Clouds, starry sky

---

## 🚀 Generation Command Examples

After creating all files:

```bash
# Generate images
python 01_generate_images.py <story_name>

# Generate Spanish version
python 02_generate_videos_spanish.py <story_name>

# Generate English version
python 02_generate_videos_english.py <story_name>
```

---

## 📖 Required Reading

Before creating tales, review:
1. **`LTX2_OPTIMIZATION_GUIDE.md`** - Token limits & optimization
2. **`PROMPT_FORMAT_WITH_MUSIC.md`** - Classical music guide
3. **`README.md`** - Complete system overview

---

## ✨ Final Notes

**Purpose:** Help children sleep peacefully
**Approach:** Gentle, calming, reassuring
**Quality:** Professional, consistent, optimized
**Languages:** Spanish (narrator) + English (characters)
**Duration:** ~5 minutes 20 seconds per story
**Music:** Classical, soothing, sleep-inducing
**Result:** Beautiful narrated bedtime videos

---

**Follow this skill document to create perfect bedtime tales every time! 🌙💫**

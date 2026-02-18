# 🎬 LTX2 Optimization Guide for Bedtime Tales

## ⚠️ Critical: LTX2 Token Limits

**Maximum prompt length:** ~200-250 tokens (approximately 150-180 words)
**Recommended:** 120-150 words per scene for optimal results

---

## 📋 Optimized Prompt Structure

### Essential Components (in order):
1. **Art Style** (5-10 words)
2. **Scene Description** (20-30 words)
3. **Camera Movement** (10-15 words)
4. **Music Reference** (15-20 words)
5. **Character Voices** (20-30 words per character)
6. **Duration** (always 20 seconds / 480 frames)

---

## ✅ Optimized Format Template

```
[ART_STYLE] animation. [SCENE_VISUAL] [CAMERA_MOVE] over 20s, [LENS]mm, f/[STOP].
[COLOR_PALETTE]. [MOTION_DESCRIPTION], 24fps. MUSIC: [PIECE_REFERENCE], [TEMPO]BPM,
vol -[DB]dB. [NARRATOR/CHARACTER_NAME]: ([VOICE_TYPE]) "[DIALOG]"
```

**Total:** ~120-150 words

---

## 📊 Example: Concise vs. Verbose

### ❌ TOO LONG (300+ words - EXCEEDS LIMIT):
```
Beautiful watercolor painting animation, soft flowing brushstrokes, delicate paper
texture visible. Tranquil forest at golden sunset, painted purple and pink gradient
sky with hand-painted crescent moon, gentle watercolor stars with soft diffused edges,
layered mountain silhouettes in diluted ink washes creating atmospheric depth, golden
meadow grass painted with loose flowing brushwork, tiny wildflowers in soft color blooms.
Gentle slow pan-right revealing painted landscape, 35mm lens, f/2.8, smooth lateral
movement lasting full 20 seconds. Warm golden-hour palette with translucent watercolor
washes, soft edges bleeding naturally...
[continues for 300+ words]
```

### ✅ OPTIMIZED (130 words - PERFECT):
```
Watercolor animation. Tranquil forest at sunset, purple-pink sky, crescent moon,
starlit horizon, mountain silhouettes, meadow grass, wildflowers. Slow pan-right
over 20s, 35mm, f/2.8. Warm golden palette, soft edges, dreamy quality. Gentle
swaying grass, 24fps peaceful movement. MUSIC: Brahms' Lullaby style piano, 60BPM,
vol -20dB, with forest ambience. NARRATOR: (warm maternal voice) "In a peaceful
forest where stars sing, lived little bunny Lumi."
```

---

## 🎵 Music + Voice Integration

### Format:
```
MUSIC: [Classical piece] style [instrument], [tempo]BPM, vol -[20-22]dB, background.
[CHARACTER]: ([voice description]) "[dialogue]" vol -[8-10]dB.
```

### Example:
```
MUSIC: Debussy Clair de Lune style piano-harp, 58BPM, vol -21dB, peaceful atmosphere.
LUMI: (young innocent child voice) "The stars are so beautiful!" vol -10dB.
NARRATOR: (soft maternal voice) "Lumi felt peace for the first time." vol -8dB.
```

---

## 👥 Character Voice Specifications

### Voice Types (Use These Exact Descriptions):

**NARRATOR:**
- `soft warm maternal voice` - Main storyteller
- Volume: -8dB (clear, audible)

**LUMI (Bunny):**
- `young innocent child voice, high-pitched, gentle`
- Volume: -10dB

**MOTHER BUNNY:**
- `warm loving adult female voice, protective`
- Volume: -9dB

**WISE OWL:**
- `deep gentle grandfatherly voice, calm reassuring`
- Volume: -9dB

**CRICKET:**
- `cheerful friendly voice, slightly high pitch`
- Volume: -10dB

---

## 📏 Word Count Guidelines

### By Section:
```
Art Style:           5-10 words
Visual Description:  20-30 words
Camera/Technical:    10-15 words
Music:              15-20 words
Character Voices:    20-40 words (total)
```

### Total Target: **120-150 words** (safe zone)
### Maximum: **180 words** (absolute limit)

---

## 🎯 Optimization Checklist

- [ ] Total word count: 120-180 words
- [ ] Art style mentioned (watercolor/Pixar/anime)
- [ ] Scene essentials described (not every detail)
- [ ] Camera movement: 20s duration stated
- [ ] Music: Classical reference, tempo, volume
- [ ] Character voices: Type specified, volume set
- [ ] No redundant descriptions
- [ ] Focus on essentials only

---

## ⚡ Quick Optimization Tips

### Remove:
- ❌ Redundant adjectives ("soft gentle delicate")
- ❌ Repetitive descriptions
- ❌ Over-detailed textures
- ❌ Multiple similar descriptors

### Keep:
- ✅ Art style keyword
- ✅ Main visual elements
- ✅ Camera specs (lens, movement, duration)
- ✅ Music reference (piece, tempo, volume)
- ✅ Character voices (type, volume, dialogue)
- ✅ 20-second duration

---

## 📝 Scene-by-Scene Token Budget

For 16 scenes × 150 words = 2,400 words total

| Element | Words | Priority |
|---------|-------|----------|
| Art Style | 5 | CRITICAL |
| Visuals | 25 | CRITICAL |
| Camera | 12 | CRITICAL |
| Music | 18 | HIGH |
| Voices | 30 | HIGH |
| Atmosphere | 10 | MEDIUM |
| **TOTAL** | **100-120** | **OPTIMAL** |

---

## 🎬 Language-Specific Optimizations

### Spanish (Narrator Only):
- Simpler: Single narrator voice
- Budget: 100-120 words per scene
- Focus: Narration + music + visuals

### English (Character Voices):
- Complex: Multiple character voices
- Budget: 120-150 words per scene
- Focus: Dialogue + music + visuals

---

## ✅ Validation

Before generating, check each prompt:

```python
def validate_prompt(prompt):
    word_count = len(prompt.split())
    if word_count > 180:
        return "❌ TOO LONG - Optimize!"
    elif word_count > 150:
        return "⚠️ LONG - Consider shortening"
    elif word_count < 100:
        return "⚠️ SHORT - May lack detail"
    else:
        return "✅ PERFECT LENGTH"
```

---

## 📚 Examples by Story Style

### Watercolor (Lumi, Cierva, Zorro):
```
Watercolor animation. [Scene]. Pan/dolly [duration], [lens], f/[stop].
[Palette]. [Motion], 24fps. MUSIC: [Piece], [BPM], vol -[dB].
[CHARACTER]: ([voice]) "[dialog]"
```

### Pixar (Bruno):
```
Pixar 3D animation. [Scene]. [Camera move] [duration], [lens], f/[stop].
[Lighting]. [Motion], 24fps. MUSIC: [Piece], [BPM], vol -[dB].
[CHARACTER]: ([voice]) "[dialog]"
```

### Anime (Gatita):
```
Anime animation, cel-shaded. [Scene]. [Camera] [duration], [lens], f/[stop].
[Colors]. [Motion], 24fps. MUSIC: [Piece], [BPM], vol -[dB].
[CHARACTER]: ([voice]) "[dialog]"
```

---

## 🚨 Common Mistakes to Avoid

1. **Over-describing visuals** - LTX2 infers details
2. **Multiple similar adjectives** - Choose one strong word
3. **Repeating style keywords** - State once at start
4. **Long dialogue** - Keep under 15 words per character
5. **Forgetting duration** - Always specify 20s

---

## 💡 Pro Tips

1. **Use industry terms** - LTX2 recognizes cinematography language
2. **Reference famous pieces** - "Brahms' Lullaby style" > "gentle piano"
3. **Specify voice types** - Helps LTX2 generate appropriate audio
4. **Volume levels matter** - Music (-20dB), Narrator (-8dB), Characters (-10dB)
5. **20-second magic** - Perfect length for story beats + music phrases

---

**Remember: Less is more! LTX2 is smart - give it essentials, let it create magic! ✨**

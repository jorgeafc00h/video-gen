# LTX-2 Video Creation Guidelines
## Best Practices for YouTube & Facebook Content Production

*Version 1.0 - February 2026*

---

## Table of Contents

1. [Overview](#overview)
2. [Model Capabilities](#model-capabilities)
3. [Hardware Requirements](#hardware-requirements)
4. [Platform Compliance](#platform-compliance)
5. [Prompting Best Practices](#prompting-best-practices)
6. [Production Workflows](#production-workflows)
7. [Technical Specifications](#technical-specifications)
8. [Content Creation Strategies](#content-creation-strategies)
9. [Optimization Tips](#optimization-tips)
10. [Common Pitfalls](#common-pitfalls)
11. [Resources](#resources)

---

## Overview

### What is LTX-2?

LTX-2 is an open-source, DiT-based audio-video foundation model developed by Lightricks that generates synchronized video and audio within a single model. It represents a significant advancement in AI video generation by treating audio and visuals as one unified generation problem rather than separate processes.

**Key Features:**
- Synchronized audio-video generation in a single pass
- Native 4K resolution support (up to 50 FPS)
- Multiple generation modes: Text-to-Video (T2V), Image-to-Video (I2V), Video-to-Video (V2V)
- Open weights with commercial usage permitted
- Runs locally on consumer hardware
- Trainable and customizable (LoRA support)

**Generation Modes:**
- **Fast Flow**: 4K generation in seconds for rapid concepting and brainstorming
- **Pro Flow**: High-quality visuals for stakeholder reviews, pitches, client presentations
- **Ultra Flow**: Production-ready 4K @ 50fps for final delivery and cinematic work

---

## Model Capabilities

### Video Specifications

| Capability | Specification |
|-----------|---------------|
| **Maximum Resolution** | 4K (3840x2160) UHD |
| **Supported Resolutions** | 540p, 720p, 1080p (FHD), 1440p (QHD), 2060p (UHD) |
| **Frame Rates** | 15, 24, 30, 50 FPS |
| **Duration** | 3-20 seconds (base model), 6/8/10 seconds (optimized) |
| **Aspect Ratios** | 16:9 (primary), 9:16 (coming soon) |
| **Audio** | Synchronized, includes dialogue, SFX, music, ambience |

### Generation Types

1. **Text-to-Video (T2V)**: Generate videos from text prompts
2. **Image-to-Video (I2V)**: Animate static images with motion
3. **Video-to-Video (V2V)**: Transform or enhance existing videos
4. **Keyframe Interpolation**: Generate smooth transitions between keyframes
5. **Controlled Generation**: Using IC-LoRAs for depth, pose, canny edge control

### Model Variants

- **Base Model (19B)**: Standard versatile generator, trainable and customizable
- **8-Step Distilled**: Fast iteration for idea exploration (8 steps stage 1, 4 steps stage 2)
- **Spatial Upscaler (2x)**: Doubles spatial resolution
- **Temporal Upscaler (2x)**: Doubles frame rate
- **IC-LoRAs**: Depth, Pose, Canny, and Union control models

---

## Hardware Requirements

### Recommended GPU Specifications

| GPU VRAM | Recommended Settings | Generation Time (720p, 4s) |
|----------|---------------------|---------------------------|
| **8-12GB** | 540p @ 24fps, 3-4 seconds, 20 steps | ~60-90 seconds |
| **16GB** | 720p @ 24fps, 4 seconds, 20 steps | ~40-60 seconds |
| **24GB+** | 720p @ 24fps, 4 seconds, 20 steps | ~25-40 seconds |
| **32GB (RTX 5090)** | 720p @ 24fps, 4 seconds, full VRAM | ~25 seconds |
| **32GB (RTX 5090)** | 720p @ 24fps, 8 seconds, weight streaming | ~3 minutes |

### VRAM Optimization Strategies

**For Limited VRAM (8-16GB):**
- Use 540p or 720p resolution
- Limit video length to 3-4 seconds
- Use 15 FPS for static scenes
- Enable weight streaming (automatic in ComfyUI)
- Consider NVFP8 quantized weights (30% smaller, 2x faster on RTX GPUs)

**Memory Management:**
- Lower resolution: 720p (16GB+) or 540p (12GB+)
- Shorter duration: 3-4 seconds instead of 8-10 seconds
- Reduce steps: 15-20 steps instead of 25+
- Use FP8 transformer mode for lower memory footprint

**Pro Tip:** Iterate at lower settings (540p, 4 seconds, 15 steps), then upscale final versions.

---

## Platform Compliance

### YouTube AI Content Policies (2026)

**✅ ALLOWED:**
- AI-assisted content with human creative input
- AI-generated visuals with human narration/commentary
- Properly disclosed AI-generated content
- Original content that adds value beyond AI generation
- Educational content about AI tools

**❌ PROHIBITED:**
- Mass-produced repetitive content
- Fully automated channels with zero human input
- Generic stock footage + TTS narration only
- Identical template/script reuse across videos
- Deepfakes without disclosure
- Misleading synthetic media
- Impersonation of real people

**DISCLOSURE REQUIREMENTS:**
- Use YouTube's upload disclosure toggle for altered/synthetic content
- Mark content during upload process if:
  - Realistic scenes are AI-generated
  - People appear to say/do things they didn't
  - Events are simulated
  - Voices are cloned
- Disclosure NOT required for:
  - Fantasy/stylized effects
  - AI assistance in editing/scripting
  - Background generation
  - Color grading/enhancement

**MONETIZATION SAFE PRACTICES:**
1. **Add Human Value**: Include personal narration, on-camera presence, or original commentary
2. **Transform Content**: Don't just generate; edit, arrange, add B-roll, sound design
3. **Maintain Originality**: Avoid repetitive formats and templates
4. **Proper Attribution**: Cite sources, provide context
5. **Engage Authentically**: Foster genuine audience connection

**High-Risk Formats to AVOID:**
- Faceless automation channels
- Mass-produced shorts (10+ similar videos daily)
- Pure stock footage + generic TTS
- Auto-generated news aggregation
- Repetitive narrated slideshows

### Facebook/Meta AI Content Policies

**Meta's C2PA Labeling:**
- Auto-labels AI content via Content Credentials metadata
- Applies to content from Adobe Firefly, DALL-E 3, Microsoft Designer
- Labels appear automatically if metadata is detected

**Best Practices:**
- Document all generative tool usage
- Disclose when realism is involved
- Avoid deepfakes/unauthorized AI likenesses
- Use clear "AI-generated" tags for branded content

### EU AI Act (Article 50) - Effective August 2026

**Labeling Requirements:**
- Content "significantly generated by AI" must be labeled
- Exemption: Content with substantial human review/editing
- Applies to: Photorealistic images, synthetic voices, AI-written text
- Geographic scope: Content directed at EU users

**Compliance Strategy:**
- Have humans review and edit all AI outputs
- Maintain editorial responsibility
- Document creative process
- Keep human-in-the-loop workflow

### Universal Platform Guidelines

**DO:**
- ✅ Disclose AI usage transparently
- ✅ Add substantial human creative input
- ✅ Create original, transformative content
- ✅ Maintain quality and viewer value
- ✅ Monitor engagement metrics

**DON'T:**
- ❌ Claim content is 100% human-made when it's not
- ❌ Use AI to impersonate real people without disclosure
- ❌ Mass-produce low-effort repetitive content
- ❌ Mislead viewers about content authenticity
- ❌ Violate copyright with AI-generated reproductions

---

## Prompting Best Practices

### Core Prompting Philosophy

LTX-2 responds best to **concrete, chronological, detailed descriptions** structured like a director's shot list—not vague vibes or paragraph novels.

### Prompt Structure Framework

**Optimal Format:**
```
[Style Definition] + [Scene Anchor] + [Subject & Action] + [Camera & Lens] + [Visual Style] + [Motion & Time] + [Audio Description]
```

**Example:**
```
Style: Cinematic film noir. Night-time city street corner, neon signs reflecting on wet pavement, light fog drifting. A detective in a tan trench coat walks slowly toward camera, hands in pockets, expression weary. Slow dolly-in, 50mm, f/2.8, medium shot, stable rig. Deep contrast, muted colors, film grain texture. Natural motion blur, 24 fps feel, 180° shutter equivalent. Distant car horns, footsteps on wet pavement, faint jazz music from nearby bar.
```

### Detailed Component Breakdown

#### 1. Style Definition (Optional but Powerful)
Place at the beginning: `Style: [style description], [rest of prompt]`

**Examples:**
- `Style: Stop-motion clay animation`
- `Style: 1980s VHS camcorder footage`
- `Style: Cinematic period drama`
- `Style: Hand-drawn 2D animation`
- `Style: Documentary realism`

#### 2. Scene Anchor (Required)
Establish location, time, atmosphere

**Template:** `[time of day] [location type], [atmospheric details], [environmental elements]`

**Examples:**
- "Dawn over a misty alpine lake, light fog, glassy water"
- "Modern tech startup office, afternoon sunlight through windows, minimalist design"
- "Medieval stone castle courtyard, overcast sky, autumn leaves scattered"

#### 3. Subject & Action (Required)
Who/what + specific verb describing motion

**Template:** `[subject description] [action verb] [manner/direction]`

**Examples:**
- "A red canoe gliding across, single rower in yellow raincoat paddling steadily"
- "Young woman in business attire walking briskly through, carrying leather briefcase"
- "Golden retriever running playfully across grass, tail wagging, tongue out"

**Action Specificity Matters:**
- ❌ "Person moves" → ✅ "Person walks briskly forward"
- ❌ "Object appears" → ✅ "Coffee cup slides into frame from left"
- ❌ "Scene changes" → ✅ "Camera pans right revealing mountains"

#### 4. Camera & Lens (Highly Recommended)
Movement, focal length, aperture, framing

**Camera Movement Options:**
- Static: "Tripod-locked, parallax from foreground elements"
- Dolly: "Slow dolly-in on subject", "Smooth dolly-right tracking"
- Crane: "Rising crane shot revealing landscape"
- Handheld: "Handheld walk-and-talk, micro jitters"
- Pan/Tilt: "Slow pan-right following subject"

**Lens Specifications:**
- Focal length: 24mm (wide), 50mm (standard), 85mm (portrait), 200mm (telephoto)
- Aperture: f/1.4 (shallow DoF), f/2.8 (balanced), f/8 (deep focus)
- Special: "Anamorphic squeeze", "Fisheye lens", "Tilt-shift effect"

**Framing:**
- Wide shot, Medium shot, Close-up, Extreme close-up
- Over-the-shoulder, POV (point of view)
- High angle, Low angle, Dutch angle

#### 5. Visual Style & Look
Color science, grading, texture, lighting

**Color Grading:**
- "Soft contrast, rich primaries, Kodak 2383 print look"
- "High micro-contrast, desaturated palette, bleach bypass feel"
- "Vibrant colors, high saturation, commercial advertising look"
- "Muted tones, low contrast, indie film aesthetic"

**Texture & Quality:**
- "High micro-contrast, fine film grain (subtle), clean edges"
- "Avoid high-frequency patterns, soften distant textures"
- "Sharp detail, minimal grain, digital cinema clarity"

**Lighting Descriptions:**
- "Key light 45° softbox feel, edge/rim light separation"
- "Golden hour bounce, warm backlight, soft shadows"
- "Harsh overhead noon sun, strong shadows"
- "Soft pools of light, controlled speculars" (for night scenes)

#### 6. Motion & Temporal Feel
Speed, cadence, motion blur characteristics

**Motion Keywords:**
- "Natural motion blur, constant speed, minimal jitter"
- "Film-like cadence, 24fps feel, 180° shutter equivalent"
- "Fast shutter speed, crisp motion, action sports feel"
- "Slow motion at 50 fps, smooth temporal flow"

**Speed Descriptors:**
- Slow/gentle/gradual
- Steady/constant/even
- Brisk/quick/rapid
- Sudden/abrupt (use sparingly)

#### 7. Audio Description (Critical for LTX-2)
Describe sounds chronologically and specifically

**Audio Categories:**

**Ambient/Environmental:**
- "Ambient coffeeshop noises, clinking cups, distant conversation"
- "Forest ambience with birds singing, rustling leaves, distant stream"
- "City street sounds, traffic hum, distant sirens"

**Sound Effects:**
- "Soft footsteps on tile echoing slightly"
- "Door creaking open slowly, metallic hinge sound"
- "Keyboard typing rhythmically, mouse clicks"

**Dialogue (when needed):**
- Provide exact words in quotes with character description
- Example: "The tall man speaks in a low, gravelly voice saying: 'You won't believe what I just saw!' His hands gesture expressively."
- Include language if not English and accent if relevant

**Music/Score:**
- "Gentle piano melody, melancholic, slow tempo"
- "Upbeat electronic music, rhythmic beats, energetic"
- "Faint jazz music drifting from nearby, saxophone solo"

**Pro Audio Tips:**
- Be specific: "soft footsteps on tile" NOT "ambient sound"
- If no dialogue needed, DON'T mention talking unless you provide exact words
- Layer sounds: background + foreground + specific effects

### Advanced Prompting Techniques

#### For Image-to-Video (I2V)

**Core Rules:**
1. **Describe ONLY motion and audio** - don't repeat what's visible in image
2. **Maintain consistency** - avoid instructions that contradict image
3. **Focus on temporal elements** - what changes, moves, or sounds

**Template:**
```
[Action/motion happening over time] + [Camera movement if any] + [Audio description]
```

**Example (for image of coffee shop interior):**
```
Steam rises slowly from coffee cups, customers in background chat quietly, barista moves behind counter preparing drinks. Gentle camera push-in toward foreground table. Ambient coffee shop sounds, espresso machine hissing, soft background jazz, quiet conversation murmur.
```

#### Negative Prompts

Always include to avoid quality issues:

**Standard Negative:**
```
worst quality, inconsistent motion, blurry, jittery, distorted, watermarks, text overlay, compression artifacts, pixelation, flickering, discontinuous motion
```

**For Specific Issues:**
- Anti-shimmer: "high-frequency patterns, repeating textures, moiré effect"
- Anti-artifacts: "over-sharpening halos, edge artifacts, banding"
- Anti-glitches: "temporal discontinuity, frame skipping, morphing"

#### Prompt Enhancement

LTX-2 supports automatic prompt enhancement via `enhance_prompt` parameter. This AI enhancement can:
- Expand vague descriptions
- Add cinematic details
- Improve temporal coherence
- Balance audio-visual elements

**When to use:**
- ✅ Quick concepting with simple prompts
- ✅ Exploring variations of a concept
- ❌ Fine-tuned control needed
- ❌ Specific technical requirements

### Prompting Don'ts

**❌ AVOID:**
- Inventing camera motion unless specifically needed
- Using timestamps or describing scene cuts
- Starting with "The scene opens with..." or "The video starts..."
- Vague vibes like "cozy minimalist scene"
- Paragraph novels - keep structure clear
- Modifying user dialogue (if provided)
- Interpreting emotions - describe only observable actions
- Describing multiple cuts/edits in one prompt

**✅ DO:**
- Start directly with style (optional) then chronological description
- Use concrete nouns and active verbs
- Specify camera and lens when control matters
- Layer audio thoughtfully
- Keep language mild, natural, understated
- Describe only what is seen and heard

### Prompt Examples Library

#### Example 1: Product Showcase
```
Style: Commercial advertising look. White studio backdrop, soft gradient lighting, clean minimal setup. Sleek smartphone rotates slowly on turntable, screen displays vibrant interface, glass back reflects light. Slow 360° dolly orbit, 85mm lens, f/2.8, medium close-up, perfectly smooth rotation. High micro-contrast, rich colors, sharp detail, subtle reflection highlights. Constant rotation speed, no motion blur, premium product feel. Quiet studio ambience, soft mechanical whir of turntable, gentle UI notification sounds.
```

#### Example 2: Nature Documentary
```
Style: Documentary realism. Early morning misty forest clearing, golden sunlight filtering through canopy, dewdrops on spider web. Red fox emerges cautiously from undergrowth, sniffs air, ears perked and alert, then trots across clearing. Slow pan-right following fox movement, 200mm telephoto, f/4, shallow depth of field, handheld micro-movements. Natural color grading, soft morning light, gentle bokeh. Smooth animal motion, 24 fps organic feel. Forest ambience with bird calls, soft rustling leaves, fox footsteps on grass, distant woodpecker.
```

#### Example 3: Urban Lifestyle
```
Style: Cinematic lifestyle vlog. Bustling Tokyo intersection at night, neon signs reflecting on wet pavement, crowds crossing, vibrant city energy. Young photographer in streetwear raises vintage film camera to eye, frames shot of street scene, shutter clicks. Slow dolly-in from medium to close-up on photographer, 50mm, f/1.8, shallow focus on subject. Rich colors, high contrast, neon glow, film-like grain. Natural handheld feel, subtle camera drift, 24 fps cinematic. City ambience with traffic sounds, distant conversations, camera shutter mechanical click, footsteps on wet ground.
```

#### Example 4: Educational Content
```
Style: Clean educational presentation. Bright modern studio, white background, professional setup, soft even lighting. Science educator in casual attire stands at transparent digital board, gestures enthusiastically while explaining, draws diagram with digital marker. Static camera, tripod-locked, 35mm, f/4, medium-wide shot, professional framing. Balanced contrast, natural colors, sharp clean image, minimal grain. Steady motion, clear gestures, professional pacing. Quiet studio background, educator speaking clearly with enthusiastic tone saying: "Let me show you how this works!" Light marker sounds on digital board, subtle room acoustics.
```

#### Example 5: Cooking Content
```
Style: Food content creation. Rustic kitchen counter, wooden cutting board, natural window light from left, warm homey atmosphere. Chef's hands expertly dice fresh vegetables with professional knife, precise cuts, colorful ingredients. Overhead static shot, 50mm macro, f/2.8, tight framing on cutting board and hands. Warm color temperature, soft shadows, appetizing lighting, subtle texture enhancement. Rhythmic cutting motion, natural cooking pace, 24 fps. Kitchen ambience, rhythmic knife sounds on cutting board, soft background music (acoustic guitar), occasional vegetable crisp snap.
```

---

## Production Workflows

### Workflow 1: Rapid Iteration for Concept Development

**Goal:** Generate multiple concept variations quickly

**Steps:**
1. **Start Low-Res:** 540p, 3-4 seconds, 15 steps
2. **Test Multiple Prompts:** Generate 5-10 variations with different styles
3. **Lock Noise Seed:** Use fixed seed for consistent comparison
4. **Evaluate:** Choose best concept based on motion, composition, coherence
5. **Refine Prompt:** Adjust winning prompt for better control
6. **Upscale Final:** Generate final version at 720p or 1080p, 20 steps

**Tools:** 8-step distilled model for maximum speed

**Timeline:** 30-60 minutes for 10 concept variations

### Workflow 2: High-Quality Final Production

**Goal:** Create production-ready content for publishing

**Steps:**
1. **Base Generation:** 720p or 1080p, 4-6 seconds, 20-25 steps
2. **Use Reference Image (I2V):** Start with key frame for better consistency
3. **Generate Multiple Takes:** Create 3-5 variations with subtle prompt changes
4. **Spatial Upscale:** Use 2x spatial upscaler for 1440p or 4K
5. **Temporal Upscale (optional):** Increase to 50 FPS for smooth motion
6. **Post-Production:** 
   - Edit in NLE (DaVinci Resolve, Premiere Pro)
   - Add color grading
   - Enhance audio (mix, EQ, compression)
   - Add graphics/text overlays
   - Include human narration/commentary
7. **Platform Optimization:** Export in platform-specific formats

**Tools:** Base model + upscalers

**Timeline:** 2-4 hours for 10-second polished segment

### Workflow 3: Educational Series Production

**Goal:** Create consistent educational video series

**Base Template Setup:**
1. Create style prompt template for series consistency
2. Design reference frame templates for different segment types
3. Establish audio signature (intro music, ambient tone)

**Episode Production:**
1. **Script Writing:** Human-written educational script
2. **Scene Planning:** Break script into 4-6 second visual segments
3. **Visual Generation:** 
   - Generate each segment with I2V from designed frames
   - Maintain consistent style prompt
   - Ensure smooth narrative flow
4. **Audio Enhancement:**
   - Record human narration/voiceover
   - Mix with AI-generated ambient/music
   - Add educational sound effects
5. **Assembly:** Edit segments in NLE with transitions
6. **Graphics Overlay:** Add educational graphics, text, diagrams
7. **Platform Compliance:** Add disclosure, proper descriptions

**Consistency Keys:**
- Fixed style prompt for entire series
- Consistent reference frame design
- Standardized color grading preset
- Unified audio mixing template

### Workflow 4: Long-Form Content Assembly

**Goal:** Create 3-10 minute YouTube videos from AI segments

**Approach:** Multi-segment mosaic technique

**Process:**
1. **Story Arc:** Plan full narrative structure (beginning/middle/end)
2. **Segment List:** Break into 15-30 individual 4-8 second clips
3. **Batch Generation:**
   - Generate all base clips (720p, 4s)
   - Use varied prompts maintaining story coherence
   - Keep scene transitions in mind
4. **Selective Upscaling:** Only upscale clips that made final cut
5. **NLE Assembly:**
   - Import all clips to timeline
   - Arrange narrative sequence
   - Add transition effects between AI segments
   - Insert B-roll, stock footage, screen recordings
6. **Human Elements:**
   - Record intro/outro with human presenter
   - Add voice narration throughout
   - Include on-screen commentary
7. **Audio Layering:**
   - Mix AI-generated audio with music bed
   - Add sound effects
   - Balance narration, music, ambient
8. **Final Polish:** Color grade, add graphics, export

**Value Addition:**
- Human narration transforms AI clips into educational content
- Personal commentary adds unique perspective
- Custom graphics reinforce key points
- Editing rhythm creates engaging pacing

### Workflow 5: Controlled Generation with IC-LoRAs

**Goal:** Precise compositional and motion control

**Use Cases:**
- Match specific choreography or movement
- Maintain character pose/position
- Follow architectural depth
- Match existing footage style

**Types of Control:**
- **Depth Control:** Maintain spatial relationships, architectural scenes
- **Pose Control:** Character animation, dance, specific gestures
- **Canny Edge:** Line art animation, maintain strong edges
- **Union Control:** Combine multiple control types

**Process:**
1. **Prepare Control Input:**
   - Depth: Extract depth map from reference image
   - Pose: Use pose detection (OpenPose) on reference
   - Canny: Extract edge map
2. **Setup Control Workflow:** Load IC-LoRA in ComfyUI
3. **Balance Control Strength:** Adjust LoRA weight (0.5-1.0)
4. **Generate with Control:** Prompt + Control Image + IC-LoRA
5. **Iterate:** Adjust control strength and prompt as needed

**Best Results:**
- Use high-quality control images
- Balance between control and creative freedom
- Combine with strong prompts for best coherence

---

## Technical Specifications

### ComfyUI Setup & Installation

**Prerequisites:**
- ComfyUI installed (latest version from comfy.org)
- Python ≥3.12
- CUDA >12.7
- PyTorch ~=2.7

**Installation Methods:**

**Method 1: ComfyUI Manager (Recommended)**
1. Open ComfyUI Manager
2. Navigate to Video section
3. Select LTX-2 workflow template
4. Models download automatically on first use

**Method 2: Manual Installation**
1. Clone repository:
   ```bash
   git clone https://github.com/Lightricks/ComfyUI-LTXVideo
   cd ComfyUI-LTXVideo
   ```
2. Install custom nodes in ComfyUI
3. Download required models manually (see model links below)

### Required Model Files

**Core Models:**

1. **LTX-2 Base Checkpoint:**
   - `ltx-2-19b-dev.safetensors` (Base model)
   - Location: `COMFYUI_ROOT/models/checkpoints/`

2. **LTX-2 Quantized (NVIDIA RTX 40+ series):**
   - `ltx-2-19b-dev-nvfp8.safetensors` (FP8 quantized, 30% smaller, 2x faster)
   - Location: `COMFYUI_ROOT/models/checkpoints/`

3. **Text Encoder:**
   - Gemma 3 12B IT (`gemma-3-12b-it-qat-q4_0-unquantized`)
   - Location: `COMFYUI_ROOT/models/text_encoders/gemma-3-12b-it-qat-q4_0-unquantized/`
   - Download entire folder from HuggingFace

4. **VAE Models:**
   - Video VAE: Included in base model
   - Audio VAE: Included in base model
   - SD VAE (for depth preprocessing): `sd-vae-ft-mse-original`

**Optional Enhancement Models:**

5. **Distilled LoRA (Fast Generation):**
   - `ltx-2-19b-distilled-lora-384.safetensors`
   - Location: `COMFYUI_ROOT/models/loras/`
   - Enables 8-step rapid generation

6. **Spatial Upscaler (2x):**
   - `ltx-2-spatial-upscaler-x2-1.0.safetensors`
   - Location: `COMFYUI_ROOT/models/latent_upscale_models/`

7. **Temporal Upscaler (2x):**
   - `ltx-2-temporal-upscaler-x2-1.0.safetensors`
   - Location: `COMFYUI_ROOT/models/latent_upscale_models/`

8. **IC-LoRA Control Models:**
   - Union LoRA (all-in-one): `ltx-2-19b-ic-lora-union-ref0.5.safetensors`
   - Depth LoRA: `ltx-2-19b-ic-lora-depth-ref0.5.safetensors`
   - Pose LoRA: `ltx-2-19b-ic-lora-pose-ref0.5.safetensors`
   - Canny LoRA: `ltx-2-19b-ic-lora-canny-ref0.5.safetensors`
   - Location: `COMFYUI_ROOT/models/loras/`

**Download Links:**
- All models: [HuggingFace - Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)
- Documentation: [docs.ltx.video](https://docs.ltx.video/)

### Generation Parameters

**Base Parameters:**

| Parameter | Recommended Range | Description |
|-----------|------------------|-------------|
| **Steps** | 15-25 | Denoising steps (20 recommended) |
| **CFG Scale** | 3.5-5.0 | Prompt adherence (4.0 recommended) |
| **Width** | 960-3840 (must be divisible by 32) | Video width in pixels |
| **Height** | 544-2160 (must be divisible by 32) | Video height in pixels |
| **Frames** | 25-161 (must be (N*8)+1) | Number of frames (97 = 4s @ 24fps) |
| **FPS** | 15, 24, 30, 50 | Frames per second |
| **Seed** | -1 (random) or fixed | Reproducibility control |

**Recommended Configurations:**

**Quick Preview (8-16GB VRAM):**
- Resolution: 960x544 (540p)
- Frames: 73 (3 seconds @ 24fps)
- Steps: 15
- CFG: 4.0

**Standard Quality (16GB+ VRAM):**
- Resolution: 1280x720 (720p)
- Frames: 97 (4 seconds @ 24fps)
- Steps: 20
- CFG: 4.0

**High Quality (24GB+ VRAM):**
- Resolution: 1920x1080 (1080p)
- Frames: 97-145 (4-6 seconds @ 24fps)
- Steps: 25
- CFG: 4.5

**Ultra Quality (32GB+ VRAM):**
- Resolution: 2560x1440 or 3840x2160
- Frames: 97 (4 seconds @ 24fps)
- Steps: 25
- CFG: 5.0
- Note: May require weight streaming for 4K

### Performance Optimization

**ComfyUI Parameters:**

1. **Reserve VRAM:**
   ```bash
   python main.py --reserve-vram 5
   ```
   Reserves 5GB VRAM for other processes

2. **Enable FP8 Mode:**
   - Use NVFP8 checkpoint on RTX 40+ series
   - ~30% memory reduction
   - ~2x speed increase

3. **Weight Streaming:**
   - Automatically engages when VRAM exceeded
   - Offloads to system RAM
   - Reduces performance but enables larger generations

**Iterative Optimization Strategy:**

1. **Development Phase:**
   - 540p, 3s, 15 steps
   - Test multiple variations quickly
   - Lock seed for comparison

2. **Refinement Phase:**
   - 720p, 4s, 20 steps
   - Refine winning concepts
   - Test minor prompt variations

3. **Final Production:**
   - 1080p+ with upscaling
   - 4-6 seconds
   - 20-25 steps
   - Apply post-production

### Export Settings

**YouTube Optimal:**
- Container: MP4 (H.264)
- Resolution: 1080p or 1440p
- Frame Rate: 24fps, 30fps, or 60fps
- Bitrate: 8-12 Mbps (1080p), 16-24 Mbps (1440p)
- Audio: AAC, 128-192 kbps, 48kHz

**Facebook Optimal:**
- Container: MP4 (H.264)
- Resolution: 1080p
- Frame Rate: 30fps
- Bitrate: 4-8 Mbps
- Aspect: 16:9 or 1:1 (square)
- Audio: AAC, 128 kbps, 48kHz

**General Best Practices:**
- Color Space: Rec.709 (SDR) or Rec.2020 (HDR)
- Deinterlace: Progressive scan
- Audio sync: Ensure perfect alignment
- Metadata: Include disclosure tags

---

## Content Creation Strategies

### Strategy 1: AI-Enhanced Educational Content

**Concept:** Use AI-generated visuals to illustrate educational concepts with human expertise

**Workflow:**
1. **Script:** Write educational script (human expertise)
2. **Visual Planning:** Identify which concepts need visual illustration
3. **AI Generation:** Create explanatory visuals with LTX-2
4. **Human Narration:** Record expert voice-over
5. **Assembly:** Combine in NLE with graphics, diagrams, animations
6. **Value Add:** Human insight + AI visualization = engaging education

**Monetization Safety:** ✅ High - substantial human value added

**Examples:**
- Science concepts visualization
- Historical event recreation
- Technical process demonstrations
- Language learning scenarios

### Strategy 2: Enhanced Storytelling

**Concept:** Combine AI-generated scenes with human narration for stories/tales

**Workflow:**
1. **Story Development:** Write original narrative (human creativity)
2. **Scene Breakdown:** Identify key visual moments
3. **Style Consistency:** Establish unified visual style prompt
4. **Scene Generation:** Create 4-8s clips for each story beat
5. **Narration:** Record expressive human storytelling
6. **Music & SFX:** Layer AI audio with custom music bed
7. **Assembly:** Edit into cohesive narrative with pacing

**Target Audiences:**
- Children's stories
- Historical narratives
- Fiction serialization
- Folklore and mythology

**Monetization Safety:** ✅ High - original stories with AI illustration

### Strategy 3: Product Review & Showcase

**Concept:** Demonstrate products with AI B-roll and human analysis

**Workflow:**
1. **Product Filming:** Record actual product with camera
2. **AI B-Roll:** Generate contextual scenes (product in use, lifestyle shots)
3. **On-Camera Review:** Human presenter provides analysis
4. **Integration:** Mix real footage, AI scenes, screen recordings
5. **Graphics:** Add specs, comparisons, call-to-action

**Value Proposition:**
- Human expertise and opinion
- Authentic product interaction
- AI enhances with lifestyle visualization

**Monetization Safety:** ✅ High - authentic review with AI enhancement

### Strategy 4: Behind-the-Scenes Process Content

**Concept:** Show creative process of making AI content (meta-content)

**Workflow:**
1. **Screen Recording:** Capture ComfyUI workflow, prompt writing
2. **AI Generation:** Show generations in real-time
3. **Commentary:** Explain decisions, techniques, prompting
4. **Before/After:** Compare iterations, show improvements
5. **Tutorial Elements:** Teach viewers how to achieve results

**Target Audience:**
- AI enthusiasts
- Content creators
- Digital artists
- Tech-curious viewers

**Monetization Safety:** ✅ Very High - educational, transparent, original

### Strategy 5: News & Current Events Commentary

**Concept:** AI-generated news visuals with human journalism

**Critical Requirements:**
- ✅ Human research and fact-checking
- ✅ Original reporting/analysis
- ✅ Clear AI disclosure
- ✅ Cite sources properly
- ✅ Human on-camera or voice narration

**Workflow:**
1. **Research:** Human investigation of topic
2. **Script:** Write news analysis/commentary
3. **Visual Support:** Generate AI visuals to illustrate points
4. **Presentation:** Human presenter delivers news
5. **Attribution:** Cite sources, disclose AI usage

**Monetization Risk:** ⚠️ Medium - requires high editorial standards

**Safety Checklist:**
- ❌ Don't auto-generate news without human verification
- ❌ Don't use AI for breaking news without disclosure
- ✅ Add substantial human analysis
- ✅ Maintain journalistic integrity

### Strategy 6: Music Visualization

**Concept:** Create visual experiences for music using AI video

**Workflow:**
1. **Music Source:** Original music or properly licensed
2. **Style Development:** Create visual style matching music mood
3. **Sync Planning:** Map visuals to musical structure
4. **Generation:** Create segments matching tempo/mood changes
5. **Editing:** Sync precisely to audio beats
6. **Effects:** Add transitions, effects matching musical energy

**Applications:**
- Lyric videos (with human-created lyrics)
- Ambient visualizations
- Concert/performance backgrounds
- Music promotion

**Monetization Safety:** ✅ High if music properly licensed

### Universal Principles for All Strategies

**Human Value Addition:**
- Original script/narration
- Personal expertise/insight
- On-camera presence
- Creative editing choices
- Unique perspective

**Quality Over Quantity:**
- Better to create 1 excellent video/week than 10 mediocre daily
- Focus on viewer value
- Maintain production standards

**Audience Engagement:**
- Respond to comments (human engagement)
- Ask for feedback
- Create community
- Build genuine relationships

**Platform Compliance:**
- Always disclose AI usage appropriately
- Follow monetization guidelines
- Avoid prohibited formats
- Stay current with policy changes

---

## Optimization Tips

### Prompt Optimization

**Iteration Technique:**
1. Start with basic prompt
2. Generate at low resolution
3. Identify issues (motion, coherence, style)
4. Add specific refinements to address issues
5. Regenerate and compare
6. Lock successful elements, vary others

**A/B Testing:**
- Keep most of prompt identical
- Change ONE variable (camera motion, lighting, audio)
- Generate both versions with same seed
- Compare to understand impact of that variable

**Prompt Library:**
- Save successful prompts in organized library
- Tag by: style, subject, motion type, quality level
- Reuse and remix proven templates
- Build personal prompt vocabulary

### Technical Optimization

**VRAM Management:**
- Monitor VRAM usage during generation
- If hitting limits:
  1. Reduce resolution first
  2. Reduce duration second
  3. Reduce steps last (affects quality)
- Use FP8 mode on compatible GPUs

**Batch Processing:**
- Generate multiple clips in sequence
- Use queue system in ComfyUI
- Set up overnight rendering for large projects
- Keep system cool for sustained performance

**Seed Management:**
- Lock seed when comparing prompt variations
- Document successful seeds for future use
- Use seed variation (+1, +2) for similar but different results

### Workflow Optimization

**Template Creation:**
- Save ComfyUI workflows as templates
- Create presets for: quick preview, standard, high quality
- Standardize node arrangements for efficiency
- Document custom workflow modifications

**Asset Organization:**
- Organize generated clips by project/date
- Use consistent naming: `project_scene#_version_resolution_date`
- Keep raw generations separate from edited finals
- Backup important generations

**Post-Production Efficiency:**
- Create NLE project templates
- Build preset color grades for consistency
- Save audio mixing templates
- Use keyboard shortcuts extensively

### Quality Optimization

**Coherence Improvements:**
- Use image-to-video with strong reference frame
- Keep prompts detailed but focused
- Avoid conflicting instructions
- Use negative prompts to prevent issues

**Motion Quality:**
- Specify camera movement explicitly or exclude it
- Use natural motion descriptors
- Avoid excessive complexity in single clip
- Consider multiple shorter clips vs one long

**Audio-Visual Sync:**
- Describe audio and visual chronologically aligned
- Use temporal cues in both domains
- In post, fine-tune sync with audio editing
- Layer AI audio with additional sound design

### Upscaling Strategy

**When to Upscale:**
- Only upscale clips that made final cut
- Generate base at 720p, upscale winners to 1080p/1440p
- Use spatial upscaler for resolution increase
- Use temporal upscaler for framerate increase

**Two-Stage Generation:**
1. Base generation: 720p, 24fps, 20 steps
2. Spatial upscale: 2x → 1440p
3. Temporal upscale (optional): 2x → 48fps
4. Final: High resolution, smooth motion

**Quality vs Speed Trade-off:**
- Development: Speed (low res, fewer steps)
- Client review: Balanced (720p, 20 steps)
- Final delivery: Quality (1080p+, upscaled, 25 steps)

---

## Common Pitfalls

### Pitfall 1: Over-Reliance on AI Without Human Value

**Problem:** Generating AI content without adding meaningful human input

**Symptoms:**
- Content feels generic and soulless
- Low viewer engagement
- Risk of demonetization
- Fails to stand out

**Solution:**
- ✅ Add personal narration explaining concepts
- ✅ Include on-camera segments with human presence
- ✅ Provide unique insights or analysis
- ✅ Edit creatively with human artistic choices
- ✅ Build genuine narrative arc

**Example Fix:**
- Before: Pure AI-generated nature scenes with AI narration
- After: AI nature visuals + expert biologist narration explaining ecosystems + personal field observations

### Pitfall 2: Repetitive Content Format

**Problem:** Using same template/structure for every video

**Symptoms:**
- YouTube flags as "inauthentic content"
- Audience boredom
- Declining view metrics
- Monetization risk

**Solution:**
- ✅ Vary visual styles between videos
- ✅ Change narrative structures
- ✅ Experiment with different formats
- ✅ Avoid cookie-cutter templates
- ✅ Keep content fresh and surprising

**Example Fix:**
- Before: Every video same intro, same music, same AI style, same script structure
- After: Unique intro per topic, varied music choices, style matches content theme, diverse storytelling approaches

### Pitfall 3: Insufficient Disclosure

**Problem:** Not properly labeling AI-generated content

**Symptoms:**
- Platform policy violations
- Loss of viewer trust
- Potential strikes/bans
- Negative community response

**Solution:**
- ✅ Use platform disclosure tools (YouTube upload toggle)
- ✅ Mention AI usage in video description
- ✅ Add verbal disclosure in content when appropriate
- ✅ Be transparent, not deceptive
- ✅ Stay updated on evolving requirements

**Example Fix:**
- Before: No mention of AI anywhere
- After: "This video uses AI-generated visuals combined with human expertise and narration" in description + YouTube disclosure toggle checked

### Pitfall 4: Prompt Quality Issues

**Problem:** Vague, inconsistent, or poorly structured prompts

**Symptoms:**
- Unpredictable results
- Poor motion coherence
- Visual artifacts
- Wasted generation time

**Solution:**
- ✅ Follow structured prompt templates
- ✅ Be specific and detailed
- ✅ Use chronological descriptions
- ✅ Include negative prompts
- ✅ Test and iterate systematically

**Example Fix:**
- Before: "A person walking in nature"
- After: "Style: Documentary realism. Forest trail on sunny afternoon, dappled light through trees, ferns on sides. Hiker in red jacket walks steadily toward camera on dirt path, backpack visible, trekking poles in hands. Slow dolly-back following hiker, 50mm, f/2.8, medium shot, smooth steady motion. Natural colors, soft contrast, forest ambience. Even walking pace, 24fps feel. Bird calls, footsteps crunching on trail, distant stream sounds."

### Pitfall 5: Ignoring Post-Production

**Problem:** Using raw AI output without editing or enhancement

**Symptoms:**
- Disjointed viewing experience
- Lack of professional polish
- Audio-visual inconsistencies
- Poor platform performance

**Solution:**
- ✅ Edit clips into cohesive sequences
- ✅ Color grade for consistency
- ✅ Mix and enhance audio properly
- ✅ Add transitions and pacing
- ✅ Include graphics, text, branding
- ✅ Professional export settings

**Example Fix:**
- Before: Upload raw 4-second AI clips as-is
- After: Import to NLE → arrange narrative → color grade → audio mix → add graphics → smooth transitions → professional export

### Pitfall 6: Hardware Mismatch

**Problem:** Attempting settings beyond hardware capabilities

**Symptoms:**
- Extremely slow generation
- System crashes
- Out of memory errors
- Frustration and inefficiency

**Solution:**
- ✅ Know your VRAM limits
- ✅ Use appropriate resolution/duration for your GPU
- ✅ Enable weight streaming when needed
- ✅ Use FP8 mode on compatible cards
- ✅ Iterate at lower settings, upscale finals

**GPU-Appropriate Settings:**
- 8-12GB: 540p, 3-4s, 15-20 steps
- 16GB: 720p, 4-6s, 20 steps
- 24GB+: 1080p, 4-8s, 20-25 steps
- 32GB: 1080p-1440p, up to 10s, full quality

### Pitfall 7: Copyright Violations

**Problem:** Recreating copyrighted characters, logos, or branded content

**Symptoms:**
- Copyright strikes
- Video takedowns
- Channel penalties
- Legal issues

**Solution:**
- ✅ Create original characters and content
- ✅ Use generic descriptions not brand names
- ✅ Avoid recreating copyrighted IP
- ✅ When discussing products, use licensed footage or original filming
- ✅ Understand fair use limitations

**Example:**
- ❌ DON'T: "Spider-Man swinging through New York"
- ✅ DO: "Superhero in red and blue suit swinging on webs through city"
- ✅ BETTER: Design completely original character

### Pitfall 8: Unrealistic Expectations

**Problem:** Expecting single-prompt perfection or magic results

**Symptoms:**
- Disappointment with results
- Giving up too quickly
- Not iterating enough
- Blaming the tool

**Solution:**
- ✅ Expect iteration and refinement
- ✅ Generate multiple variations
- ✅ Learn from each generation
- ✅ Build skills systematically
- ✅ Embrace creative experimentation

**Reality Check:**
- Professional results require: good prompts + multiple generations + selection + editing + human enhancement
- Expect 3-10 generations per final clip
- Budget time for post-production (50% of project time)

### Pitfall 9: Neglecting Audio

**Problem:** Focusing only on visuals, treating audio as afterthought

**Symptoms:**
- Poor audio quality
- Jarring audio transitions
- Generic or repetitive sounds
- Viewer drop-off

**Solution:**
- ✅ Describe audio as thoroughly as visuals in prompts
- ✅ Mix AI audio with professional music beds
- ✅ Add human narration/voiceover
- ✅ Layer sound effects thoughtfully
- ✅ Professional audio mixing in post

**Audio Enhancement Workflow:**
1. Use AI-generated base audio from LTX-2
2. Add professional music track (licensed)
3. Record human narration
4. Add additional SFX where needed
5. Mix in DAW or NLE with proper levels
6. Apply EQ, compression, limiting
7. Ensure consistent volume throughout

### Pitfall 10: Skipping Platform Research

**Problem:** Not understanding platform-specific requirements and best practices

**Symptoms:**
- Poor video performance
- Format incompatibilities
- Reduced reach
- Lower engagement

**Solution:**
- ✅ Research YouTube algorithm preferences (watch time, CTR, engagement)
- ✅ Understand Facebook video specs and audience behavior
- ✅ Optimize thumbnails and titles (human-created)
- ✅ Use platform analytics to improve
- ✅ Stay updated on platform changes

**Platform Specific:**

**YouTube:**
- Longer videos (8-15 min) often perform better for monetization
- Strong hook in first 30 seconds critical
- Encourage likes, comments, subscriptions (human CTAs)
- Consistent upload schedule

**Facebook:**
- Shorter videos (1-3 min) perform better
- Square or vertical formats for mobile
- Captions essential (85% watch without sound)
- Native uploads outperform links

---

## Resources

### Official Documentation

- **LTX-2 Official Site:** [ltx.io/model/ltx-2](https://ltx.io/model/ltx-2)
- **LTX Documentation:** [docs.ltx.video](https://docs.ltx.video/)
- **GitHub Repository:** [github.com/Lightricks/LTX-2](https://github.com/Lightricks/LTX-2)
- **ComfyUI Integration:** [github.com/Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo)
- **HuggingFace Model:** [huggingface.co/Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)

### Model Downloads

- **Main Model Weights:** [HuggingFace Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)
- **Gemma Text Encoder:** [HuggingFace google/gemma-3-12b-it-qat-q4_0-unquantized](https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized)
- **RES4LYF Sampler:** [github.com/ClownsharkBatwing/RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF)

### Tools & Software

- **ComfyUI:** [comfy.org](https://www.comfy.org/)
- **ComfyUI Documentation:** [docs.comfy.org](https://docs.comfy.org/)
- **NVIDIA Optimization Guide:** [NVIDIA LTX-2 Guide](https://www.nvidia.com/en-us/geforce/news/rtx-ai-video-generation-guide/)

### Platform Policies

- **YouTube Community Guidelines:** [support.google.com/youtube/answer/9288567](https://support.google.com/youtube/answer/9288567)
- **YouTube AI Disclosure:** [support.google.com/youtube/answer/14305575](https://support.google.com/youtube/answer/14305575)
- **YouTube Partner Program:** [support.google.com/youtube/answer/72857](https://support.google.com/youtube/answer/72857)
- **Meta AI Content Transparency:** [transparency.meta.com/features/explaining-ai-generated-content](https://transparency.meta.com/features/explaining-ai-generated-content)
- **EU AI Act Information:** [digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

### Community & Learning

- **ComfyUI Community:** [Reddit r/comfyui](https://www.reddit.com/r/comfyui/)
- **AI Video Generation:** [Reddit r/aivideo](https://www.reddit.com/r/aivideo/)
- **LTX Blog:** [ltx.io/blog](https://ltx.io/blog)
- **ComfyUI Blog:** [blog.comfy.org](https://blog.comfy.org/)

### Tutorials & Guides

- **LTX-2 Prompting Guide:** [ltx.io/model/model-blog/prompting-guide-for-ltx-2](https://ltx.io/model/model-blog/prompting-guide-for-ltx-2)
- **NVIDIA Quick Start:** [NVIDIA GeForce LTX-2 Guide](https://www.nvidia.com/en-us/geforce/news/rtx-ai-video-generation-guide/)
- **ComfyUI LTX-2 Tutorial:** [docs.comfy.org/tutorials/video/ltx/ltx-2](https://docs.comfy.org/tutorials/video/ltx/ltx-2)

### Hardware Resources

- **GPU Performance Database:** Research community benchmarks for your specific GPU
- **VRAM Calculators:** Estimate requirements for different settings
- **Cooling Solutions:** Important for sustained rendering sessions

### Post-Production Tools

**Video Editing (NLE):**
- DaVinci Resolve (free & paid)
- Adobe Premiere Pro
- Final Cut Pro
- CapCut (free, beginner-friendly)

**Audio Editing:**
- Audacity (free)
- Adobe Audition
- Logic Pro
- Reaper

**Graphics & Motion:**
- Adobe After Effects
- Blender (free)
- Canva (free & paid)

**Color Grading:**
- DaVinci Resolve (industry standard, free version available)
- FilmConvert
- LUT libraries

### Licensing & Legal

- **LTX-2 License:** [LTX-2 Community License Agreement](https://huggingface.co/Lightricks/LTX-2/blob/main/LICENSE.md)
- **Commercial Usage:** Permitted under LTX-2 license
- **Music Licensing:**
  - Epidemic Sound
  - Artlist
  - AudioJungle
  - YouTube Audio Library (free)
- **Stock Footage:**
  - Pexels Videos (free)
  - Pixabay (free)
  - Envato Elements

---

## Quick Reference

### Prompt Template

```
Style: [visual style description]. [Scene anchor: time, location, atmosphere]. [Subject and action: who/what doing what]. [Camera: movement, lens, framing]. [Visual style: color, lighting, texture]. [Motion: speed, cadence, feel]. [Audio: ambience, SFX, dialogue, music].
```

### Parameter Cheat Sheet

**Quick Start (8-16GB GPU):**
- 960x544, 73 frames (3s @ 24fps), 15 steps, CFG 4.0

**Standard (16GB+ GPU):**
- 1280x720, 97 frames (4s @ 24fps), 20 steps, CFG 4.0

**High Quality (24GB+ GPU):**
- 1920x1080, 97-145 frames (4-6s @ 24fps), 25 steps, CFG 4.5

### Platform Compliance Checklist

- [ ] Content adds substantial human value
- [ ] Properly disclosed AI usage where required
- [ ] Avoid mass-produced repetitive formats
- [ ] Include human narration/presence
- [ ] Original creative input demonstrated
- [ ] Platform-appropriate export settings
- [ ] Proper thumbnail and metadata (human-created)

### File Organization Template

```
/Project_Name/
├── /01_Scripts/           # Human-written scripts
├── /02_Prompts/           # Organized prompt library
├── /03_References/        # Reference images, style guides
├── /04_Raw_Generations/   # AI-generated clips
│   ├── /Scene_01/
│   ├── /Scene_02/
│   └── /Scene_03/
├── /05_Selected/          # Chosen clips for final edit
├── /06_Upscaled/          # High-res versions
├── /07_Assets/            # Graphics, music, SFX
├── /08_Edited/            # NLE project files
└── /09_Final_Exports/     # Rendered videos for upload
```

---

## Conclusion

LTX-2 represents a powerful tool for video content creation, offering unprecedented control over synchronized audio-visual generation. Success with this technology for YouTube and Facebook requires:

1. **Understanding platform policies** and staying compliant
2. **Adding substantial human value** beyond AI generation
3. **Mastering prompting techniques** for consistent quality
4. **Optimizing workflows** for efficiency and quality
5. **Professional post-production** to polish final content

Remember: LTX-2 is a creative tool, not a replacement for human creativity, expertise, and authentic connection with audiences. The most successful content creators will use AI to enhance their unique perspective, not substitute for it.

**Key Success Principles:**
- Transparency about AI usage
- Human expertise and insight
- Quality over quantity
- Continuous learning and iteration
- Authentic audience engagement
- Platform compliance
- Professional production values

By following these guidelines and best practices, you can create engaging, compliant, and monetizable video content that leverages the power of LTX-2 while maintaining the irreplaceable human element that audiences value.

---

*Document Version: 1.0*  
*Last Updated: February 2026*  
*Author: Created for El Salvador-based content production*  
*License: For personal and commercial project use*
# 🎨 Flux 2 Klein - Batch Image Generation

Automatically generate images from text files using Python + ComfyUI API.

---

## ⚡ Quick Start

```bash
# One-time setup
pip install requests

# Navigate to this directory
cd "c:\repos\video-gen\ImageEditing Workflows\Flux 2 Klein 9B FP8 (Distilled)"

# Process your prompts
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_lumi.txt
```

**That's it!** All prompts will be queued automatically.

---

## 📋 Usage

### Basic Usage
```bash
python auto_batch_processor.py <prompts_file>
```

### Watch Mode (auto-reload when file changes)
```bash
python auto_batch_processor.py <prompts_file> --watch
```

### Custom ComfyUI URL
```bash
python auto_batch_processor.py <prompts_file> --url http://127.0.0.1:8000
```

---

## 📝 Examples

### Process Bedtime Tales Stories

```bash
# Lumi the Bunny (15 scenes)
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_lumi.txt

# Bruno the Bear (15 scenes)
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_bruno.txt

# Gatita Nube (15 scenes)
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_gatita.txt

# La Pequeña Cierva (15 scenes)
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_cierva.txt

# El Pequeño Zorro (15 scenes)
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_zorro.txt
```

### Watch Mode (for iterative work)

```bash
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_lumi.txt --watch

# Now edit the prompts file in your editor
# Save → automatically re-queues all prompts!
```

---

## 📂 Prompt File Format

Create a `.txt` file with **one prompt per line**:

```
A cute bunny hopping through a magical garden, watercolor style
A little fox looking at the moon, children's book illustration
A bear watching the stars, pixar style, dreamy atmosphere
```

**Features:**
- Empty lines are ignored
- Use `#` for comments
- Each line = one image

**Example with comments:**
```
# Scene 1 - Introduction
A cute bunny in a magical garden, watercolor painting

# Scene 2 - Discovery
The bunny discovers glowing flowers that shimmer in the moonlight

# Scene 3 - Adventure
...
```

---

## ⚙️ Configuration

### ComfyUI Settings

**Default URL:** `http://127.0.0.1:8001`

The script auto-detects your ComfyUI instance. To use a different port:
```bash
python auto_batch_processor.py prompts.txt --url http://127.0.0.1:8188
```

### Image Generation Settings

Edit `auto_batch_processor.py` to customize:

**Image Size** (around line 110):
```python
"6": {
    "inputs": {
        "width": 1024,   # Change: 768, 1024, 1536
        "height": 1024,  # Change: 768, 1024, 1536
        "batch_size": 1
    },
```

**Sampling Steps** (around line 115):
```python
"8": {
    "inputs": {
        "steps": 20,     # Change: 15, 20, 25, 30
        "width": 1024,
        "height": 1024
    },
```

**CFG Scale** (around line 120):
```python
"9": {
    "inputs": {
        "cfg": 5.0,      # Change: 3.5, 5.0, 7.0
```

---

## 📊 Output

### File Naming
```
Flux2-Klein-Batch_0001_00001.png
Flux2-Klein-Batch_0002_00001.png
Flux2-Klein-Batch_0003_00001.png
...
```

### Output Location
```
C:\ComfyUI\output\
```

---

## ✨ Features

- ✅ **No custom nodes** - uses ComfyUI API directly
- ✅ **Batch processing** - queue hundreds of prompts instantly
- ✅ **Real-time progress** - see what's being queued
- ✅ **Watch mode** - auto-reload on file changes
- ✅ **Error handling** - continues even if one prompt fails
- ✅ **Auto-numbering** - sequential filenames
- ✅ **Unicode support** - handles special characters

---

## 📊 Example Output

```
======================================================================
  🎨 ComfyUI Auto Batch Processor
======================================================================

🔍 Checking ComfyUI status...
✅ ComfyUI is running at http://127.0.0.1:8001

📄 Loaded 15 prompts from batch_prompts_lumi.txt


======================================================================
🚀 Batch Processing Started
======================================================================
   ComfyUI: http://127.0.0.1:8001
   Prompts: 15
======================================================================

[001/015] A cute bunny hopping through a magical garden filled with...
          ✅ Queued (ID: 0d596114...)
[002/015] The bunny discovers glowing flowers that shimmer softly...
          ✅ Queued (ID: f867b7f4...)
[003/015] Lumi meets a wise old owl perched on a glowing tree...
          ✅ Queued (ID: f39e754b...)
...
[015/015] The bunny returns home, the garden glowing behind...
          ✅ Queued (ID: 1c507176...)

======================================================================
✨ Batch Processing Complete
======================================================================
   ✅ Queued: 15
   ❌ Failed: 0
   📊 Queue: 1 running, 14 pending
======================================================================
```

---

## 🔧 Troubleshooting

### "Cannot connect to ComfyUI"
- Make sure ComfyUI is running
- Default URL: `http://127.0.0.1:8001`
- Try different port: `--url http://127.0.0.1:8188`

### "Module 'requests' not found"
```bash
pip install requests
```

### "Workflow file not found"
- Make sure you're in the correct directory
- Workflow should be: `Flux 2 Klein 9B - Simple Batch (No Custom Nodes).json`

### Encoding Errors (Windows)
The script automatically handles Unicode. If you still see errors:
```bash
# Set console to UTF-8
chcp 65001
```

---

## 💡 Pro Tips

### 1. Queue Everything at Once
The script queues all prompts instantly - ComfyUI processes them in the background:
```bash
python auto_batch_processor.py batch_prompts_lumi.txt
# All 15 prompts queued in ~2 seconds
# ComfyUI processes over next 30-60 minutes
```

### 2. Use Watch Mode for Iteration
Perfect for refining prompts in real-time:
```bash
python auto_batch_processor.py prompts.txt --watch
# Edit prompts.txt
# Save → automatically re-queues
# Perfect for experimenting!
```

### 3. Organize with Comments
```
# Character Introduction
A cute bunny with soft fur and big eyes

# Setting the Scene
A magical garden filled with glowing flowers

# Action Sequence
The bunny discovers a hidden path
```

### 4. Process Multiple Stories Sequentially
```bash
# Queue all your stories in one go
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_lumi.txt
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_bruno.txt
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_gatita.txt
# Total: 45 images queued!
```

---

## 📁 Your Files

Ready to process:
```
../../BedTIme-tales/
├── batch_prompts_lumi.txt     (15 scenes - Conejito Lumi)
├── batch_prompts_bruno.txt    (15 scenes - Osito Bruno)
├── batch_prompts_gatita.txt   (15 scenes - Gatita Nube)
├── batch_prompts_cierva.txt   (15 scenes - La Pequeña Cierva)
└── batch_prompts_zorro.txt    (15 scenes - El Pequeño Zorro)
```

Example file included:
```
example-prompts-batch.txt (5 test prompts)
```

---

## 🎯 Workflow

The script uses this workflow internally:
- `Flux 2 Klein 9B - Batch from Text File (Working).json` (reference)

But you don't need to load it in ComfyUI - the script handles everything via API!

---

## 🚀 Complete Workflow

```bash
# 1. Make sure ComfyUI is running (http://127.0.0.1:8001)

# 2. Install requirements (first time only)
pip install requests

# 3. Navigate to this directory
cd "c:\repos\video-gen\ImageEditing Workflows\Flux 2 Klein 9B FP8 (Distilled)"

# 4. Process your prompts
python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_lumi.txt

# 5. Check output
# Images appear in: C:\ComfyUI\output\

# 6. Done! ✨
```

---

## 📚 Scripts

| File | Purpose |
|------|---------|
| `auto_batch_processor.py` | Main batch processing script |
| `example-prompts-batch.txt` | Example prompts for testing |

---

## 🎉 That's It!

Simple, automated batch processing with zero custom nodes required.

**Next Steps:**
1. Test with example file: `python auto_batch_processor.py example-prompts-batch.txt`
2. Process your stories: `python auto_batch_processor.py ../../BedTIme-tales/batch_prompts_lumi.txt`
3. Enjoy your automated image generation! 🚀

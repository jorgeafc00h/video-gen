# 🛡️ Safe Custom Node Installation Guide

## ⚠️ The Problem

Installing **ComfyUI-Logic** or multiple random packages can corrupt ComfyUI.
We'll install ONLY the most stable, essential package.

---

## ✅ Solution: Install ComfyUI-Custom-Scripts ONLY

This is the **most popular and stable** custom node package. It includes:
- ✅ `LoadText` - read from text files
- ✅ String manipulation
- ✅ Many useful utilities

### Step-by-Step Installation:

#### Method 1: Using ComfyUI Manager (Recommended)

1. **Open ComfyUI**
2. **Click "Manager" button** (bottom right or in menu)
3. **Click "Install Custom Nodes"**
4. **Search for:** `ComfyUI-Custom-Scripts`
5. **Find the one by:** `pythongosssss`
6. **Click Install**
7. **Restart ComfyUI**

---

#### Method 2: Manual Git Install (If Manager doesn't work)

1. **Open Command Prompt** (or Git Bash)

2. **Navigate to custom_nodes folder:**
```bash
cd "C:\Users\Equipo\AppData\Local\Programs\ComfyUI\resources\ComfyUI\custom_nodes"
```

3. **Clone the repository:**
```bash
git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git
```

4. **Restart ComfyUI**

---

#### Method 3: Manual Download (No Git required)

1. **Download ZIP** from:
   https://github.com/pythongosssss/ComfyUI-Custom-Scripts/archive/refs/heads/main.zip

2. **Extract the ZIP**

3. **Copy the folder to:**
   ```
   C:\Users\Equipo\AppData\Local\Programs\ComfyUI\resources\ComfyUI\custom_nodes\ComfyUI-Custom-Scripts
   ```

4. **Restart ComfyUI**

---

## ⚠️ What About the Other Missing Nodes?

Your workflow needs:
- ✅ `LoadText` - **INCLUDED in ComfyUI-Custom-Scripts**
- ❌ `StringToList` - from ComfyUI-Logic (PROBLEMATIC)
- ❌ `LoopManager` - from ComfyUI-Logic (PROBLEMATIC)
- ❌ `String Format` - from other packages

**ComfyUI-Logic causes the corruption issues!**

---

## 🔧 Fix the Workflow Instead

Since ComfyUI-Logic is problematic, I'll create a modified workflow that:
1. Uses `LoadText` from ComfyUI-Custom-Scripts
2. Replaces the problematic nodes with built-in alternatives
3. Works reliably without breaking ComfyUI

---

## 🚨 If ComfyUI is Already Broken:

### Clean Installation Steps:

1. **Backup your models folder:**
   ```
   C:\ComfyUI\models
   ```

2. **Remove broken custom nodes:**
   ```bash
   cd "C:\Users\Equipo\AppData\Local\Programs\ComfyUI\resources\ComfyUI\custom_nodes"
   # Delete any folders that look suspicious (ComfyUI-Logic, etc.)
   ```

3. **Reinstall Pillow (like we did before):**
   ```bash
   cd C:\ComfyUI
   .venv\Scripts\python.exe -m pip uninstall pillow -y
   .venv\Scripts\python.exe -m pip install pillow
   ```

4. **Start ComfyUI** - it should work now

5. **Install ONLY ComfyUI-Custom-Scripts** (see above)

---

## ✅ After Installation

Once ComfyUI-Custom-Scripts is installed, I'll give you a **modified workflow** that:
- Uses LoadText (from the safe package)
- Replaces StringToList and LoopManager with a different approach
- Processes all your prompts from text files
- Won't corrupt your installation

---

## 📞 Next Steps

1. **Try installing ComfyUI-Custom-Scripts** using Method 1 (Manager)
2. **Let me know if it works**
3. **I'll create a modified workflow** that uses only safe nodes

---

## 💡 Why This Package is Safe

- ⭐ **30,000+ stars** on GitHub
- ✅ **Actively maintained** (updated regularly)
- ✅ **No Python dependencies** that conflict
- ✅ **Used by thousands** without issues
- ✅ **Pure JavaScript** for most features (can't break Python env)

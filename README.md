# 📸 Canon Selphy Photo Heal
Fix incompatible photos so your Canon Selphy actually prints them

Canon Selphy printers are great… until they refuse to print your photos.

Many Selphy models only accept images that contain very specific EXIF metadata — the kind that typically only comes from Canon cameras.
If you try printing downloaded images, edited images, Canva exports, PNGs, screenshots, or anything without the “right” EXIF fields…

👉 The printer silently rejects them
👉 or shows "ghost" pictures
👉 or simply skips the file entirely.

This tool fixes that.

✨ What this tool does

Canon-Selphy-photo-heal is a small Python utility that:

✔ Imports EXIF metadata from a known working Canon-compatible photo
✔ Injects that EXIF into any input photo
✔ Automatically converts PNG, WebP, etc. into JPEG
✔ Regenerates a clean, valid EXIF thumbnail
✔ Outputs consistent .JPG files that Selphy printers accept
✔ Batch processes entire folders
✔ Deletes the original input files after processing (optional behavior you can change)

It is designed to be simple, fast, and frustration-free.

# 🧠 Why this exists

Canon Selphy printers enforce quirky, undocumented EXIF rules that:

- Require certain tags to be present
- Reject images without EXIF thumbnails
- Sometimes ignore photos with certain DPI fields
- Don’t like PNGs or images edited by some apps

Instead of reverse-engineering every tag, this tool copies the EXIF from a “known good” image and reuses it across all your photos.
This creates clean, printer-friendly files — with your actual image data preserved.

# 🚀 How to Use
1. Install requirements [see here for installing uv](https://docs.astral.sh/uv/getting-started/installation/)
```
uv sync
```

2. Prepare your folders
Your project directory should look like:
```
Canon-Selphy-photo-heal/
│
├── main.py            # The script
├── input/             # Put new photos here
└── output/            # Processed photos will appear here
```

3. Add photos to process

Put any of these formats inside the input/ folder:

- .jpg
- .jpeg
- .png
- .webp

4. Run the script
```
uv run main.py
```

5. Collect your photos

Photos appear in the `output` folder


❤️ Contributions Welcome

Feel free to submit pull requests for:

- A GUI version
- Drag-and-drop desktop app
- Docker support
- Prebuilt binaries for Windows/macOS
import piexif
from PIL import Image
import io
import shutil
import os

REFERENCE_IMAGE = "reference.JPG"       # A known-good Selphy-compatible file
INPUT_DIR = "input"
OUTPUT_DIR = "output"

def create_exif_thumbnail(img, max_size=160):
    thumbnail = img.copy()
    thumbnail.thumbnail((max_size, max_size))
    buf = io.BytesIO()
    thumbnail.save(buf, format="JPEG")
    return buf.getvalue()

def sanitize_exif(reference_exif, img):
    """Clone EXIF and replace thumbnail with a fresh one."""
    cleaned = {
        ifd: dict(tags) for ifd, tags in reference_exif.items() if isinstance(tags, dict)
    }
    cleaned["thumbnail"] = create_exif_thumbnail(img)
    return piexif.dump(cleaned)

def process_photo(reference_exif, input_path, output_path):
    # Load input image
    img = Image.open(input_path)

    # Convert to RGB (important for PNG/WebP/HEIC)
    img = img.convert("RGB")

    # Build EXIF (with new thumbnail)
    exif_bytes = sanitize_exif(reference_exif, img)

    # Save output as JPEG, always .JPG
    img.save(output_path, "jpeg", exif=exif_bytes)
    print(f"Processed: {input_path} → {output_path}")

def main():
    # Load EXIF from reference image only once
    reference_exif = piexif.load(REFERENCE_IMAGE)

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collect files to delete later
    files_to_delete = []

    # Allowed extensions Pillow can open
    allowed_ext = (".jpg", ".jpeg", ".png", ".webp", ".heif", ".heic")

    # Process each photo in input directory
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(allowed_ext):
            continue  # skip non-JPEG files

        in_path = os.path.join(INPUT_DIR, filename)
        
        # Force output filename to end with .JPG
        base_name = os.path.splitext(filename)[0]
        out_path = os.path.join(OUTPUT_DIR, base_name + ".JPG")

        process_photo(reference_exif, in_path, out_path)
        files_to_delete.append(in_path)

    # Remove input files after successful processing
    for f in files_to_delete:
        os.remove(f)
        print(f"Deleted: {f}")

    print("✅ Done! All photos processed and input folder cleared.")


if __name__ == "__main__":
    main()

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



def copy_exif(source_path, target_path, output_path):
    # Load EXIF from the known-working image
    exif_dict = piexif.load(source_path)

    exif_dict["thumbnail"] = None   

    # Load the target image (the one with missing/bad EXIF)
    img = Image.open(target_path)

    exif_dict["thumbnail"] = create_exif_thumbnail(img)

    # Dump EXIF back into bytes format
    exif_bytes = piexif.dump(exif_dict)

    # Save new image with transferred EXIF
    img.save(output_path, "jpeg", exif=exif_bytes)

    print(f"EXIF copied successfully → {output_path}")


if __name__ == "__main__":
    copy_exif(
        source_path="reference.JPG",      # Your Canon-accepted image
        target_path="target.jpeg",          # Internet image you want to print
        output_path="new_with_exif.JPG" # Output file with copied EXIF
    )

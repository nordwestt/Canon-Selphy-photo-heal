import piexif

REFERENCE_IMAGE = "reference.JPG"
OUTPUT_FILE = "reference_exif.bin"

exif_dict = piexif.load(REFERENCE_IMAGE)
exif_bytes = piexif.dump(exif_dict)

with open(OUTPUT_FILE, "wb") as f:
    f.write(exif_bytes)

print("EXIF dumped → reference_exif.bin")

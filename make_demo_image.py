from pathlib import Path
from urllib.request import urlopen

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

image_url = "https://upload.wikimedia.org/wikipedia/commons/b/b0/Tokyo_International_University_Logo.png"

with urlopen(image_url) as response:
    png_data = response.read()

if mode == "suspicious":
    png_data += b"\nPRIVATE_KEY: This is harmless demo hidden data for the StegoGuard lab.\n"

Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")

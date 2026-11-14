# A food-picture-01 entry (Python 3.13, standard library only): its picture is the
# entry.png beside this file, and the program copies it to /output/entry.png.
# The picture is a steaming gourmet ramen bowl: glossy tonkotsu broth, noodles
# lifted in chopsticks, a jammy soft egg, glistening chashu, fresh scallions
# and nori, in warm dramatic light.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # competition cap: image at most 1 MiB

src = Path(__file__).resolve().parent / "entry.png"
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

if not src.is_file():
    print(f"missing entry image: {src}", file=sys.stderr)
    sys.exit(1)

size = src.stat().st_size
if size > MAX_BYTES:
    print(f"entry image too large: {size} bytes > {MAX_BYTES}", file=sys.stderr)
    sys.exit(1)

# Validate it is a JPEG or PNG and read its pixel dimensions.
with open(src, "rb") as f:
    head = f.read(33)
if head[:3] == b"\xff\xd8\xff":
    # JPEG: scan segments for the SOF marker carrying width/height.
    w = h = None
    data = head
    i = 2
    while True:
        while i + 9 <= len(data) and w is None:
            if data[i] != 0xFF:
                break
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                h = struct.unpack(">H", data[i + 5:i + 7])[0]
                w = struct.unpack(">H", data[i + 7:i + 9])[0]
                break
            seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
            i += 2 + seg_len
        if w is not None or len(data) > 33:
            break
        with open(src, "rb") as f:
            data = f.read()
        i = 2
elif head[:8] == b"\x89PNG\r\n\x1a\n":
    w, h = struct.unpack(">II", head[16:24])
else:
    print("entry image is neither JPEG nor PNG", file=sys.stderr)
    sys.exit(1)
if w is None or h is None or w > 1024 or h > 1024:
    print(f"entry image dimensions invalid: {w}x{h} (max 1024x1024)", file=sys.stderr)
    sys.exit(1)

out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out / "entry.png")
print(f"wrote {out / 'entry.png'} ({w}x{h}, {size} bytes)")

from sys import argv
from pathlib import Path

from PIL import Image
from PIL.ImageOps import expand, contain

jpg_options = {
    "subsampling": 0,
    "quality": 95
}

def border_width(width: int, height: int) -> int:

    short_side = min(width, height)

    return int(short_side * 0.03)

if __name__ == "__main__":
    filepath = Path(argv[1])

    with open(filepath, "rb") as fp:
        img = Image.open(fp)

        border_size = border_width(*img.size)
        bordered_img = expand(image=img, border=border_size, fill="white")

        resized_img = contain(image=bordered_img, size=(1920, 1920))

    write_path = (
        Path(__file__)
        .parent.joinpath("processed")
        .joinpath(f"{filepath.stem}_processed")
        .with_suffix(filepath.suffix)
    )

    with open(write_path, "wb") as fp:
        resized_img.save(fp, **jpg_options)

from sys import argv
from pathlib import Path
from glob import glob

from PIL import Image
from PIL.ImageOps import expand, contain

jpg_options = {
    "subsampling": 0,
    "quality": 95
}

def border_width(width: int, height: int) -> int:

    short_side = min(width, height)

    return int(short_side * 0.03)


def process_from_path(path: Path) -> None:

    with open(path, "rb") as fp:
        img = Image.open(fp)

        border_size = border_width(*img.size)
        bordered_img = expand(image=img, border=border_size, fill="white")

        resized_img = contain(image=bordered_img, size=(1920, 1920))

    write_path = (
        Path(__file__)
        .parent.joinpath("processed")
        .joinpath(f"{path.stem}_processed")
        .with_suffix(path.suffix)
    )

    with open(write_path, "wb") as fp:
        resized_img.save(fp, **jpg_options)


if __name__ == "__main__":

    for file in argv[1:]:
        print(file)
        filepath = Path(file)
        process_from_path(filepath)

    
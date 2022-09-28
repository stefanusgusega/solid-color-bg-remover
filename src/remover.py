"""
Module for remover functions
"""
from PIL import Image
from tqdm import tqdm
from src.utils import color_hex_to_int


def remove_solid_color_bg(img_path: str, solid_color_hex: str, save_path: str):
    """
    Remove solid color background from an image and then
    save it.
    """
    img = Image.open(img_path)
    img = img.convert("RGBA")

    solid_color_in_rgb = color_hex_to_int(solid_color_hex)

    datas = img.getdata()

    new_data = []

    for item in tqdm(datas):
        if item[0:3] == solid_color_in_rgb:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(save_path, "png")

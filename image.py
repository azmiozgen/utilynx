import os

import numpy as np
from PIL import Image, ImageColor, ImageDraw, ImageFont

def crop_pil_image(image, bbox):
    '''
    Crop a PIL image
    bbox: [x1, y1, x2, y2]
    '''
    return image.crop(bbox)

def draw_rectangles_on_pil_image(image, rectangles, color=(0, 0, 255), width=3):
    '''
    Draw rectangles on a PIL image
    image: PIL image
    rectangles: (x1, y1, x2, y2)
    '''
    draw = ImageDraw.Draw(image)
    for rectangle in rectangles:
        draw.rectangle(rectangle, outline=color, width=width)
    return image

def draw_bbox_on_image(image, bbox, text,
                       color='black', font=None, font_size=16, text_angle=-45,
                       text_color='black', thickness=4):
    '''
    Draw bounding boxes on an image with given text
    image: PIL image
    bbox: (x1, y1, x2, y2)
    text: text to be written on the image
    color: color of the bounding box
    font: font of the text
    font_size: size of the font
    text_angle: angle of the text
    text_color: color of the text
    thickness: thickness of the bounding box
    '''
    x1, y1, x2, y2 = bbox
    draw = ImageDraw.Draw(image)
    draw.rectangle([x1, y1, x2, y2], outline=color, width=thickness)

    if font:
        font = ImageFont.truetype(font, size=font_size)
    else:
        font = ImageFont.load_default()
    font_size = font.getsize(text)
    font_height = font_size[1]

    text_bg_draw = Image.new('RGBA', font_size, (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_bg_draw)

    margin = np.ceil(0.05 * font_height)
    text_rgb_color = ImageColor.getrgb(text_color)
    text_draw.text((0, 0), text, font=font, fill=(*text_rgb_color, 255))
    text_rotated_draw = text_bg_draw.rotate(text_angle, expand=1)
    loc = (int(x1 + margin), int(y1 - margin))
    image.paste(text_rotated_draw, loc, text_rotated_draw)

    return image

def read_pil_image(image_file):
    '''
    Read a PIL image
    '''
    return Image.open(image_file)

def write_pil_image(image, image_file):
    '''
    Write a PIL image
    '''
    image.save(image_file)


if __name__ == '__main__':
    image_file = os.path.join('asset', 'girl_with_pearl_earring.jpg')

    ## Test read_pil_image
    image = read_pil_image(image_file)

    ## Test draw_bbox_on_image
    bbox = (400, 300, 600, 500)
    font = os.path.join('asset', 'Lato-Black.ttf')
    image = draw_bbox_on_image(image, bbox, 'Girl with Pearl Earring',
                               color='red', font=font, font_size=32, text_angle=-45,
                               text_color='black', thickness=4)
    output_file = os.path.join('output', 'girl_with_pearl_earring.jpg')
    os.makedirs('output', exist_ok=True)
    write_pil_image(image, output_file)
    print(output_file, 'written.')

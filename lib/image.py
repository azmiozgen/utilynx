#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import cv2
import numpy as np
from PIL import Image, ImageColor, ImageDraw, ImageFont

from numeric import get_l2_norm


def crop_pil_image(image, bbox):
    """
    Crop a PIL image
    bbox: [x1, y1, x2, y2]
    """
    return image.crop(bbox)


def draw_rectangles_on_pil_image(image, rectangles, color=(0, 0, 255), width=3):
    """
    Draw rectangles on a PIL image
    image: PIL image
    rectangles: (x1, y1, x2, y2)
    """
    draw = ImageDraw.Draw(image)
    for rectangle in rectangles:
        draw.rectangle(rectangle, outline=color, width=width)
    return image


def draw_bbox_on_image(image, bbox, text,
                       color='black', font=None, font_size=16, text_angle=-45,
                       text_color='black', thickness=4):
    """
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
    """
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


def extend_line_segment(p1, p2, w):
    """
    Extend a line segment
    p1: (x1, y1)
    p2: (x2, y2)
    w: width of the image
    """
    x1, y1 = p1
    x2, y2 = p2
    x1_new = 0
    x2_new = w
    slope = (y2 - y1) / (x2 - x1)
    y1_new = int(y1 + slope * (x1_new - x1))
    y2_new = int(y2 + slope * (x2_new - x2))
    return x1_new, y1_new, x2_new, y2_new


def read_pil_image(image_file):
    """
    Read a PIL image
    """
    return Image.open(image_file)


def trim_borders(image, bg=0):
    """
    Trim borders of binary image
    """
    h, w = image.shape[:2]
    region = np.where(image != bg)
    ymin, ymax = region[0].min(), region[0].max()
    xmin, xmax = region[1].min(), region[1].max()
    ymin = max(0, ymin - 1)
    ymax = min(h, ymax + 1)
    xmin = max(0, xmin - 1)
    xmax = min(w, xmax + 1)
    return image[ymin:ymax, xmin:xmax]


def write_pil_image(image, image_file):
    """
    Write a PIL image
    """
    image.save(image_file)


def warp_four_corners(image, corners):
    """
    Warp four corners of a polygon on image
    Opposite corners will be aligned horizontally
    image: numpy array
    corners: ((x1, y1), (x2, y2), (x3, y3), (x4, y4)) from top to bottom clockwise
    """
    x1, y1 = corners[0]
    x2, y2 = corners[1]
    x3, y3 = corners[2]
    x4, y4 = corners[3]
    h, w, _ = image.shape
    height1 = get_l2_norm(np.array([x1, y1]), np.array([x3, y3]))
    height2 = get_l2_norm(np.array([x2, y2]), np.array([x4, y4]))

    if height1 <= height2:
        new_corners = np.float32([[x1, y2], [x2, y2], [x3, y3], [x4, y3]])
    else:
        new_corners = np.float32([[x1, y1], [x2, y1], [x3, y4], [x4, y4]])

    transformation_matrix = cv2.getPerspectiveTransform(np.array(corners, dtype=np.float32),
                                                        new_corners)
    image_warped = cv2.warpPerspective(image, transformation_matrix, (w, h), flags=cv2.INTER_LINEAR)

    return image_warped


if __name__ == '__main__':
    image_file = os.path.join('asset', 'girl_with_pearl_earring.jpg')
    ## w, h, c = (1200, 800, 3)
    image_file2 = os.path.join('asset', 'binary_head.png')
    ## w, h, c = (488, 275, 3)
    os.makedirs('output', exist_ok=True)

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

    ## Test extend_line_segment on black image and show the image
    w, h = 100, 100
    image = Image.new('RGB', (w, h), (50, 50, 50))
    p1 = (60, 30)
    p2 = (50, 50)
    x1_new, y1_new, x2_new, y2_new = extend_line_segment(p1, p2, w)
    draw = ImageDraw.Draw(image)
    draw.line([(x1_new, y1_new), (x2_new, y2_new)], fill='red', width=3)
    draw.line([p1, p2], fill='white', width=4)
    output_file = os.path.join('output', 'extend_line_segment.jpg')
    os.makedirs('output', exist_ok=True)
    write_pil_image(image, output_file)
    print(output_file, 'written.')

    ## Test trim_borders
    image_binary = cv2.imread(image_file2, cv2.IMREAD_GRAYSCALE)
    image_binary_trimmed = trim_borders(image_binary)
    output_file = os.path.join('output', 'binary_head_trimmed.png')
    cv2.imwrite(output_file, image_binary_trimmed)
    print(output_file, 'written.')

    ## Test warp_four_corners on image_file
    image = cv2.imread(image_file)
    corners = ((100, 100), (1000, 200), (800, 600), (200, 700))
    ## draw circles on corners
    for corner in corners:
        cv2.circle(image, corner, 5, (0, 0, 255), -1)
    image_warped = warp_four_corners(image, corners)
    output_file = os.path.join('output', 'girl_with_pearl_earring_warped.jpg')
    cv2.imwrite(output_file, image_warped)
    print(output_file, 'written.')

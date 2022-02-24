from PIL import Image

def crop_pil_image(image, bbox):
    """
    Crop a PIL image
    bbox: [x1, y1, x2, y2]
    """
    return image.crop(bbox)

def read_pil_image(image_file):
    """
    Read a PIL image
    """
    return Image.open(image_file)

def write_pil_image(image, image_file):
    """
    Write a PIL image
    """
    image.save(image_file)
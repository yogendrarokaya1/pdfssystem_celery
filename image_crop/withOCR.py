import os

from PIL import Image
from barcode import barcode as m
from image_crop import ocr_code
from image_crop import text_extraction


def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)


def image_crop(image, pdf_name, image_name):

    obj_final = []
    dirs = 'image_dir/' + pdf_name + '/' + image_name
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    x1 = 0
    y1 = 0
    x2 = 551
    y2 = 293

    for row in range(0, 8):

        for column in range(0, 3):
            image_dir = '%s/%s_%s.jpg' % (dirs, row, column)
            crop(image, (x1, y1, x2, y2), image_dir)

            each_barcode = m.barcode_reader(image_dir, pdf_name)
            each_text = ocr_code.text(image_dir, pdf_name, row, column, image_name)
            required_text_obj = text_extraction.text_to_useable(each_text)

            obj_final.append((each_barcode, required_text_obj))
            x1 += 551
            x2 += 551
        x1 = 0
        x2 = 551
        y1 += 293
        y2 += 293

    return obj_final


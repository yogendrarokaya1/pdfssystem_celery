import os

import cv2
from pyzbar.pyzbar import decode


def barcode_reader(_image, _title):
    img = cv2.imread(_image)

    detected_barcodes = decode(img)

    if not detected_barcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        # file_object = open(file_name, 'a')
        for barcode in detected_barcodes:
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                return str(barcode.data.decode())



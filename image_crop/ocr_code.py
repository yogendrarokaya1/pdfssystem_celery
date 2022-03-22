import os

import pytesseract


def text(path, sname, _row, _column, _img_name):
    pytesseract.pytesseract.tesseract_cmd = r'D:\\tesseract-ocr\\tesseract'

    _dir = 'text_ocr' + '/' + sname + '/' + str(_img_name)
    if not os.path.exists(_dir):
        os.makedirs(_dir)

    file_name = _dir + '/' + str(_row) + str(_column) + '.txt'
    file_object = open(file_name, 'a')
    start = '***start***'
    end = '***end***'
    # print(start)
    # print(pytesseract.image_to_string(path))
    # print(end)
    file_object.write('%s\r\n' % str(start))
    file_object.write('%s\r\n' % str(pytesseract.image_to_string('%s' % path)))
    file_object.write('%s\r\n' % str(end))

    return file_name

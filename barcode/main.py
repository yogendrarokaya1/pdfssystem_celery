import os
from pdf2image import convert_from_path


def convert(file_path, file_name, outputdir):
    outputdir = outputdir + str(file_name) + '/'
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    pages = convert_from_path(file_path, 200)
    counter = 1
    for page in pages:
        myfile = outputdir + 'output' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")




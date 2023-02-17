import numpy as np
from PIL import Image, ImageOps


def pix_percentage(scratch_list, datum_list):
    scratch_avg = round(sum(scratch_list) / len(scratch_list), 2)
    datum_avg = round(sum(datum_list) / len(datum_list),2)

    percentage_difference = round(abs(scratch_avg - datum_avg) / ((scratch_avg + datum_avg)/2) * 100, 2)
    print("Result:")
    print("Datum AVG:" + str(datum_avg))
    print("Sample AVG:" + str(scratch_avg))
    print("Datum differs from scratch by: " + str(percentage_difference) + "%")
    print("")
    print("NOTE: Lower values appear darker and higher values are lighter")



def pixels_as_list(img):

    # get image x and y size
    width, height = img.size
    # retrieve values of all pixels
    pixels = img.load()
    all_pixels = []
    # fill new list with value of each pixel
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    # return list of pixel values
    return all_pixels


def load_image(file):
    # Create image object
    im = Image.open(file)
    return im


def gray_it(img):
    # convert image object to gray-scale
    im2 = ImageOps.grayscale(img)
    return im2


if __name__ == '__main__':
    main_color = 100
    indication_color = 170
    file_name_scratch = "sample_F_NS.jpg"
    file_name_datum = "sample_F_NS_datum.jpg"
    image_scratch = load_image(file_name_scratch)
    image_datum = load_image(file_name_datum)
    gray_scratch_list = pixels_as_list(gray_it(image_scratch))
    gray_datum_list = pixels_as_list(gray_it(image_datum))
    pix_percentage(gray_scratch_list,gray_datum_list)


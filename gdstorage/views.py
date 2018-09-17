from django.shortcuts import render

from gdstorage.gdapi import GdApi

gdapi = GdApi()


def upload_animal_images(animal_id, filepath):
    image_id = gdapi.upload_file(filename=animal_id, mimetype='image/jpeg', filepath=filepath)
    url = gdapi.get_src_image(image_id)

    return url

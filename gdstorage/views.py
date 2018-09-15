from django.shortcuts import render

from gdstorage.gdapi import gdapi



#gdapi.list_files(1000)




def upload_animal_images(animal_id):
    image_id = gdapi.upload_file(filename=animal_id, mimetype='image/jpeg', filepath="sistema.jpg")
    url = gdapi.get_src_image(image_id)
    context = {
        'url': url
    }
    return context


print(upload_animal_images('1'))
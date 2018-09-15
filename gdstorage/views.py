from django.shortcuts import render

from core.views import BaseView

from gdstorage.gdapi import gdapi


class ViewUploadImages(BaseView):

    def upload_animal_images(self, animal_id, filepath):
        image_id = gdapi.upload_file(filename=animal_id, mimetype='image/jpeg', filepath=filepath)
        url = gdapi.get_src_image(image_id)
        context = {
            'url': url
        }
        return context


upload_images = ViewUploadImages()
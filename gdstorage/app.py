from gdstorage.gdapi import GdApi

gdapi = GdApi()


def upload_animal_images(animal_id, filepath):
    delete_image_if_exists(animal_id)
    image_id = gdapi.upload_file(filename=animal_id, mimetype='image/jpeg', filepath=filepath)
    url = gdapi.get_src_image(image_id)

    return url


def delete_image_if_exists(animal_id):
    file_name = 'animal' + '-' + str(animal_id) + '.jpeg'
    results = gdapi.search_file_by_name(file_name)
    for result in results:
        gdapi.delete_file_by_id(result['id'])

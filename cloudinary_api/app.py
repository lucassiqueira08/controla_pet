import cloudinary
import cloudinary.uploader
import cloudinary.api
from decouple import config

cloudinary.config(
  cloud_name=config('CLOUDINARY_CLOUD_NAME'),
  api_key=config('CLOUDINARY_API_KEY'),
  api_secret=config('CLOUDINARY_API_SECRET'),
)


class CloudinaryApi:

    UPLOAD_ANIMAL_PATH = 'Morumbichos/Animais/'
    UPLOAD_CLIENTE_PATH = 'Morumbichos/Clientes/'

    def upload_animal_image(self, file, id_animal):
        filename = self.UPLOAD_ANIMAL_PATH + "animal_" + str(id_animal)
        tags = ["animal"]
        alt = "Foto de identificação do Animal de ID " + str(id_animal)
        request = cloudinary.uploader.upload(file=file,
                                             public_id=filename,
                                             height=300,
                                             width=300,
                                             quality="auto:eco",
                                             crop="limit",
                                             tags=tags,
                                             alt=alt)
        if request == {}:
            response = {}
            return response

        response = {'url': request['url']}
        return response

    def upload_cliente_imagem(self, file, id_client):
        filename = self.UPLOAD_CLIENTE_PATH + "cliente_" + str(id_client)
        tags = ["cliente"]
        alt = "Foto de identificação do Cliente de ID " + str(id_client)
        request = cloudinary.uploader.upload(file=file,
                                             public_id=filename,
                                             height=300,
                                             width=300,
                                             quality="auto:eco",
                                             crop="limit",
                                             tags=tags,
                                             alt=alt)
        if request == {}:
            response = {}
            return response

        response = {'url': request['url']}
        return response


cloudyapi = CloudinaryApi()
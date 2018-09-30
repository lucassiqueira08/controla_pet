from gdstorage.gdapi import GdApi

gdapi = GdApi()


def verifica_extensao(arquivo):
    TXT = ['text/plain']
    WORD = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    PDF = ['application/pdf']
    PPT = ['application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/vnd.ms-powerpoint']
    EXCEL = ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']
    IMAGE = ['application/vnd.google-apps.photo', 'image/jpeg', 'image/png']
    UNKNOWN = 'application/vnd.google-apps.unknown'

    content_type = arquivo.content_type
    if content_type in WORD:
        mimetype = 'text/docx'
        upload_mimetype = 'application/vnd.google-apps.document'
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': '.docx'}

    elif content_type in TXT:
        mimetype = 'plan/text'
        upload_mimetype = 'application/vnd.google-apps.document'
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': '.txt'}

    elif content_type in PDF:
        mimetype = 'application/pdf'
        upload_mimetype = 'application/vnd.google-apps.document'
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': '.pdf'}

    elif content_type in PPT:
        mimetype = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        upload_mimetype = 'application/vnd.google-apps.presentation'
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': '.ppt'}

    elif content_type in EXCEL:
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        upload_mimetype = 'application/vnd.google-apps.spreadsheet'
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': '.xls'}

    elif content_type in IMAGE:
        mimetype = 'image/jpeg'
        upload_mimetype = 'image/jpeg'
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': '.jpeg'}

    else:
        mimetype = UNKNOWN
        upload_mimetype = UNKNOWN
        return {'mimeType': mimetype, 'upload_mimeType': upload_mimetype, 'extensao': ''}


def upload_animal_autorizacao(arquivo, animal_id, filepath, procedimento_id):
    file_info = verifica_extensao(arquivo)
    filename = 'autorizacao_' + str(procedimento_id) + '_' + str(animal_id) + file_info['extensao']

    file_id = gdapi.upload_file(filename=filename,
                                mimetype=file_info['mimeType'],
                                filepath=filepath,
                                upload_mimeType=file_info['upload_mimeType'])

    url = gdapi.get_src_file(file_id, file_info['mimeType'])

    return url


def upload_animal_exame(arquivo, animal_id, filepath, data):
    file_info = verifica_extensao(arquivo)
    filename = 'exame_' + str(data) + '_' + str(animal_id) + file_info['extensao']

    file_id = gdapi.upload_file(filename=filename,
                                mimetype=file_info['mimeType'],
                                filepath=filepath,
                                upload_mimeType=file_info['upload_mimeType'])

    url = gdapi.get_src_file(file_id, file_info['mimeType'])

    return url

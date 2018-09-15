from django.views import View
from django.shortcuts import render

from gdstorage.gdapi import gdapi

gdapi.list_files(1000)
#gdapi.upload_file('unnamed.jpg','unnamed.jpg','image/jpeg')
#gdapi.download_file('1Knxs5kRAMnoH5fivGeNsdrj_SIgLiqzV','google.jpg')
#gdapi.create_folder('Google')
#gdapi.search_file(10,"name contains 'Getting'")

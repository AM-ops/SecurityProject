from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.VigTextEnc)
admin.site.register(models.VigTextDec)
admin.site.register(models.VerTextEnc)
admin.site.register(models.VerTextDec)
admin.site.register(models.TranspoTextEnc)
admin.site.register(models.TranspoTextDec)
admin.site.register(models.OwnTextEnc)
admin.site.register(models.OwnTextDec)

admin.site.register(models.VigFileEnc)
admin.site.register(models.VigFileDec)
admin.site.register(models.VerFileEnc)
admin.site.register(models.VerFileDec)
admin.site.register(models.TranspoFileEnc)
admin.site.register(models.TranspoFileDec)
admin.site.register(models.OwnFileEnc)
admin.site.register(models.OwnFileDec)

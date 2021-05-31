from django.db import models
#from django.core.urlresolvers import reverse
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from Algorithms import algorithms
import os
import io
import base64
from django.core.files.base import ContentFile, File

User = get_user_model()

class VigTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(null=False, default='')
    ciphertext = models.TextField(null=False,default='')
    key = models.TextField(null=False,default='')
    description = models.TextField(default='Vigenere Text Encryption')

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        self.ciphertext = algorithms.Vigenere_TEXT_Encryption(self.plaintext,self.key)

    def get_absolute_url(self):
        return reverse('SecApp:VigTextEnc_detail', kwargs={'pk':self.pk})

class VigTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()
    key = models.TextField(null=False,default='')
    description = models.TextField(default='Vigenere Text Decryption')

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        self.plaintext = algorithms.Vigenere_TEXT_Decryption(self.ciphertext,self.key)

    def get_absolute_url(self):
        return reverse('SecApp:VigTextDec_detail', kwargs={'pk':self.pk})

class VerTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(null=False, default='')
    ciphertext = models.TextField(null=False, default='')
    description = models.TextField(default='Vernam Text Encryption')

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        self.ciphertext = algorithms.Vernam_TEXT_Encryption(self.plaintext)

    def get_absolute_url(self):
        return reverse('SecApp:VerTextEnc_detail', kwargs={'pk':self.pk})

class VerTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(null=False, default='')
    ciphertext = models.TextField(null=False, default='')
    description = models.TextField(default='Vernam Text Decryption')

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        self.plaintext = algorithms.Vernam_TEXT_Decryption(self.ciphertext)

    def get_absolute_url(self):
        return reverse('SecApp:VerTextDec_detail', kwargs={'pk':self.pk})

class TranspoTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(null=False, default='')
    ciphertext = models.TextField(null=False, default='')
    key = models.TextField(null=False, default='')
    description = models.TextField(default='Transposition Text Encryption')

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        self.ciphertext = algorithms.Transposition_TEXT_Encryption(self.plaintext,self.key)

    def get_absolute_url(self):
        return reverse('SecApp:TranspoTextEnc_detail', kwargs={'pk':self.pk})

class TranspoTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(null=False, default='')
    ciphertext = models.TextField(null=False, default='')
    description = models.TextField(default='Transposition Text Decryption')
    key = models.TextField(null=False, default='')

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        self.plaintext = algorithms.Transposition_TEXT_Decryption(self.ciphertext,self.key)

    def get_absolute_url(self):
        return reverse('SecApp:TranspoTextDec_detail', kwargs={'pk':self.pk})

class OwnTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(null=False, default='')
    ciphertext = models.TextField(null=False,default='')
    key = models.TextField(null=False,default='')
    description = models.TextField(default='J&A Homebrew Text Encryption')

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        self.ciphertext = algorithms.own_TEXT_Encryption(self.plaintext,self.key)

    def get_absolute_url(self):
        return reverse('SecApp:OwnTextEnc_detail', kwargs={'pk':self.pk})

class OwnTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()
    key = models.TextField(null=False,default='')
    description = models.TextField(default='J&A Homebrew Text Decryption')

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        self.plaintext = algorithms.own_TEXT_Decryption(self.ciphertext,self.key)

    def get_absolute_url(self):
        return reverse('SecApp:OwnTextDec_detail', kwargs={'pk':self.pk})

class VigFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.TextField(default='')
    description = models.TextField(default='Vigenere File Encryption')
    key = models.TextField(blank=True,default='')
    ext = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.plaintext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Vigenere_FILE_Encryption(plainData,self.key)
        self.ciphertext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_vig_enc.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:VigFileEnc_detail', kwargs={'pk':self.pk})

class VigFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(default='')
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Vigenere File Decryption')
    key = models.TextField(blank=True,default='')
    ext = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.ciphertext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Vigenere_FILE_Decryption(plainData,self.key)
        self.plaintext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_vig_dec.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:VigFileDec_detail', kwargs={'pk':self.pk})

class VerFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.TextField(default='')
    description = models.TextField(default='Vernam File Encryption')
    ext = models.CharField(default='', max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.plaintext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Vernam_FILE_Encryption(plainData)
        self.ciphertext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_vernam_enc.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:VerFileEnc_detail', kwargs={'pk':self.pk})

class VerFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(default='')
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Vernam File Decryption')
    ext = models.CharField(default='', max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.ciphertext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Vernam_FILE_Decryption(plainData)
        self.plaintext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_vernam_dec.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:VerFileDec_detail', kwargs={'pk':self.pk})

class TranspoFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.TextField(default='')
    description = models.TextField(default='Transposition File Encryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args,**kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.plaintext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Transposition_FILE_Encryption(plainData,self.key)
        self.ciphertext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_transpo_enc.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:TranspoFileEnc_detail', kwargs={'pk':self.pk})

class TranspoFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(default='')
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Transposition File Decryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args,**kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.ciphertext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Transposition_FILE_Decryption(plainData,self.key)
        self.plaintext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_transpo_dec.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:TranspoFileDec_detail', kwargs={'pk':self.pk})

class OwnFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.TextField(default='')
    description = models.TextField(default='J&A Homebrew File Encryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args,**kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.plaintext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.own_FILE_Encryption(plainData,self.key)
        self.ciphertext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_own_enc.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:OwnFileEnc_detail', kwargs={'pk':self.pk})

class OwnFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.TextField(default='')
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='J&A Homebrew File Decryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args,**kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.ciphertext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.own_FILE_Decryption(plainData,self.key)
        self.plaintext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_own_dec.{0}'.format(self.ext)))

    def get_absolute_url(self):
        return reverse('SecApp:OwnFileDec_detail', kwargs={'pk':self.pk})
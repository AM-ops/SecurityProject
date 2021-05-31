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
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Vigenere File Encryption')
    key = models.TextField(blank=True,default='')
    ext = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.enc()
        

    def enc(self, *args, **kwargs):
        pass
        #plainData = algorithms.fileToByteString(self.plaintext)
        #cipherData = algorithms.Vigenere_FILE_Encryption(plainData,self.key)
        #algorithms.byteStringToFile(cipherData,self.ciphertext)

    def get_absolute_url(self):
        return reverse('home')

class VigFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Vigenere File Decryption')
    key = models.TextField(blank=True,default='')
    ext = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.enc()
        

    def enc(self, *args, **kwargs):
        pass
        #plainData = algorithms.fileToByteString(self.plaintext.path)
        #cipherData = algorithms.Vigenere_FILE_Encryption(plainData,self.key)
        #algorithms.byteStringToFile(cipherData,self.ciphertext.path)

    def get_absolute_url(self):
        return reverse('home')

class VerFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.TextField(default='')
    description = models.TextField(default='Vernam File Encryption')
    ext = models.CharField(default='', max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #self.ciphertext = self.plaintext
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        THIS_FOLDER = os.path.dirname(os.path.abspath(settings.MEDIA_ROOT))
        new_path = os.path.join(THIS_FOLDER, 'media')
        pt = str(self.plaintext.path)
        plainData = algorithms.fileToByteString(pt)
        cipherData = algorithms.Vernam_FILE_Encryption(plainData)
        self.ciphertext = algorithms.byteStringToFile(cipherData, os.path.join(new_path, 'newfile_vernam_enc.{0}'.format(self.ext)))
        #self.user = User.objects.get(username=self.request.user.username)
        
        #algorithms.byteStringToFile(cipherData,'newfile.{0}'.format(self.ext))
        #ct = str(self.ciphertext.path)
        #a = self.plaintext
        #self.ciphertext = a
        #self.ciphertext.save(name='newfile.{0}'.format(self.ext),content=ContentFile(b))
        #with open(b,'rb') as f:
        #self.ciphertext.save('newfile.{0}'.format(self.ext),ContentFile(b),save=False)
        #f.close()
        #self.save()
        
        #self.ciphertext = File(cipherfile)
        #f = open(cipherfile, 'rb')
        #self.ciphertext.save('newfile',ContentFile(f))
        #f.close()
        #self.ciphertext.save('newfile',ContentFile(cipherData))
        #file = File(io.BytesIO(content), name='foo.{0}'.format(self.ext))
        #file_data = ContentFile(base64.urlsafe_b64decode(content))
        #file_data = ContentFile(base64.b64decode(content))
        #self.ciphertext.save('newfile.{0}'.format(self.ext), file_data)

    def get_absolute_url(self):
        return reverse('SecApp:VerFileEnc_detail', kwargs={'pk':self.pk})

class VerFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Vernam File Decryption')
    ext = models.CharField(default='', max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.dec()

    def dec(self, *args, **kwargs)
    def get_absolute_url(self):
        return reverse('home')

class TranspoFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Transposition File Encryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #self.enc()

    def get_absolute_url(self):
        return reverse('home')

class TranspoFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='Transposition File Decryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #self.enc()

    def get_absolute_url(self):
        return reverse('home')

class OwnFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='J&A Homebrew File Encryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #self.enc()

    def get_absolute_url(self):
        return reverse('home')

class OwnFileDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plaintext = models.FileField(upload_to='', blank=True)
    ciphertext = models.FileField(upload_to='', blank=True)
    description = models.TextField(default='J&A Homebrew File Decryption')
    ext = models.CharField(default='', max_length=10)
    key = models.TextField(blank=True,default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #self.enc()

    def get_absolute_url(self):
        return reverse('home')

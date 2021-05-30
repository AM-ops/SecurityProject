from django.db import models
#from django.core.urlresolvers import reverse
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from Algorithms import algorithms

User = get_user_model()

class VigTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.FileField(upload_to='media', default='')
    ciphertext = models.FileField(upload_to='media', default='')
    description = models.TextField(default='Vigenere File Encryption')
    key = models.TextField(null=False,default='')

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        plainData = algorithms.fileToByteString(self.plaintext)
        cipherData = algorithms.Vigenere_FILE_Encryption(plainData,self.key)
        algorithms.byteStringToFile(cipherData,self.ciphertext)

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')
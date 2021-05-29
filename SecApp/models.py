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
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('SecApp:VigTextEnc_detail', kwargs={'pk':self.pk})

class VigTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')

class VigFileEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.FileField(upload_to='files', default='')
    ciphertext = models.FileField(upload_to='files', default='')

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')

class VerTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')

class VerTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')

class TranspoTextEnc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()

    def save(self, *args, **kwargs):
        self.enc()
        super().save(*args, **kwargs)

    def enc(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')

class TranspoTextDec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plaintext = models.TextField()
    ciphertext = models.TextField()

    def save(self, *args, **kwargs):
        self.dec()
        super().save(*args, **kwargs)

    def dec(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        #return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})
        return reverse('home')

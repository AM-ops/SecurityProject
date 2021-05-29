from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import VigTextEnc, VigTextDec, VerTextDec, VerTextEnc, TranspoTextEnc, TranspoTextDec
from django import forms

class VigTextEncModelForm(ModelForm):
    class Meta:
        model = VigTextEnc
        fields = ['plaintext','key']
        labels = {
        "plaintext": "Text to Encrypt",
        "key": "Key",
        }
        widgets = {
        'plaintext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letter','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VigTextDecModelForm(ModelForm):
    class Meta:
        model = VigTextDec
        fields = ['ciphertext','key']
        labels = {
        "ciphertext": "Text to Decrypt",
        'key':'Key',
        }
        widgets = {
        'ciphertext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letter','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VerTextEncModelForm(ModelForm):
    class Meta:
        model = VerTextEnc
        fields = ['plaintext']
        labels = {
        "plaintext": "Text to Encrypt",
        }
        widgets = {
        'plaintext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letter','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VerTextDecModelForm(ModelForm):
    class Meta:
        model = VerTextDec
        fields = ['ciphertext']
        labels = {
        "ciphertext": "Text to Decrypt",
        }
        widgets = {
        'ciphertext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class TranspoTextEncModelForm(ModelForm):
    class Meta:
        model = TranspoTextEnc
        fields = ['plaintext']
        labels = {
        "plaintext": "Text to Encrypt",
        }
        widgets = {
        'plaintext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class TranspoTextDecModelForm(ModelForm):
    class Meta:
        model = TranspoTextDec
        fields = ['ciphertext']
        labels = {
        "ciphertext": "Text to Decrypt",
        }
        widgets = {
        'ciphertext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
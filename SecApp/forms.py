from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import VigTextEnc, VigTextDec, VerTextDec, VerTextEnc, TranspoTextEnc, TranspoTextDec, OwnTextEnc, OwnTextDec, VigFileEnc, VigFileDec, VerFileEnc, VerFileDec, TranspoFileEnc,TranspoFileDec, OwnFileEnc, OwnFileDec
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
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
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
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
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
        fields = ['plaintext','key']
        labels = {
        "plaintext": "Text to Encrypt",
        }
        widgets = {
        'plaintext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class TranspoTextDecModelForm(ModelForm):
    class Meta:
        model = TranspoTextDec
        fields = ['ciphertext','key']
        labels = {
        "ciphertext": "Text to Decrypt",
        }
        widgets = {
        'ciphertext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class OwnTextEncModelForm(ModelForm):
    class Meta:
        model = OwnTextEnc
        fields = ['plaintext','key']
        labels = {
        "plaintext": "Text to Encrypt",
        "key": "Key",
        }
        widgets = {
        'plaintext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class OwnTextDecModelForm(ModelForm):
    class Meta:
        model = OwnTextDec
        fields = ['ciphertext','key']
        labels = {
        "ciphertext": "Text to Decrypt",
        'key':'Key',
        }
        widgets = {
        'ciphertext': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter text here','rows':5,}),
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VigFileEncModelForm(ModelForm):
    class Meta:
        model = VigFileEnc
        fields = ['plaintext','ext','key']
        labels = {
        "plaintext": "File to Encrypt",
        "key": "Key",
        "ext": "Extension",
        }
        widgets = {
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VigFileDecModelForm(ModelForm):
    class Meta:
        model = VigFileDec
        fields = ['ciphertext','ext','key']
        labels = {
        "ciphertext": "File to Decrypt",
        "key": "Key",
        "ext": "Extension",
        }
        widgets = {
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VerFileEncModelForm(ModelForm):
    class Meta:
        model = VerFileEnc
        fields = ['plaintext','ext']
        labels = {
        "plaintext": "File to Encrypt",
        'ext': 'Extension',
        }
        widgets = {
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class VerFileDecModelForm(ModelForm):
    class Meta:
        model = VerFileDec
        fields = ['ciphertext','ext']
        labels = {
        "ciphertext": "File to Decrypt",
        'ext': 'Extension',
        }
        widgets = {
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class TranspoFileEncModelForm(ModelForm):
    class Meta:
        model = TranspoFileEnc
        fields = ['plaintext','ext','key']
        labels = {
        "plaintext": "File to Encrypt",
        "key": "Key",
        "ext": "Extension",
        }
        widgets = {
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class TranspoFileDecModelForm(ModelForm):
    class Meta:
        model = TranspoFileDec
        fields = ['ciphertext','ext','key']
        labels = {
        "ciphertext": "File to Decrypt",
        "key": "Key",
        "ext": "Extension",
        }
        widgets = {
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class OwnFileEncModelForm(ModelForm):
    class Meta:
        model = OwnFileEnc
        fields = ['plaintext','ext','key']
        labels = {
        "plaintext": "File to Encrypt",
        "key": "Key",
        "ext": "Extension",
        }
        widgets = {
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class OwnFileDecModelForm(ModelForm):
    class Meta:
        model = OwnFileDec
        fields = ['ciphertext','ext','key']
        labels = {
        "ciphertext": "File to Decrypt",
        "key": "Key",
        "ext": "Extension",
        }
        widgets = {
        'key': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter ONLY Alphabet Letters','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
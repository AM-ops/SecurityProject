from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'

class SuccessPage(TemplateView):
    template_name = 'success.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

class DocsPage(TemplateView):
    template_name = 'docs.html'
    
def handler404(request, exception):
       return render(request, '404.html')
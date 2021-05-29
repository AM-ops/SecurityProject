from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'
#    def __init__(self, arg):
#        super(HomePage, self).__init__()
#        self.arg = arg
class SuccessPage(TemplateView):
    # """docstring for TestPage."""
    #
    # def __init__(self, arg):
    #     super(TestPage, self).__init__()
    #     self.arg = arg
    template_name = 'success.html'

class ThanksPage(TemplateView):
    # """docstring for ThanksPage."""
    #
    # def __init__(self, arg):
    #     super(ThanksPage, self).__init__()
    #     self.arg = arg
    template_name = 'thanks.html'

class ContactPage(TemplateView):
    # """docstring for ThanksPage."""
    #
    # def __init__(self, arg):
    #     super(ThanksPage, self).__init__()
    #     self.arg = arg
    template_name = 'contact.html'
    
def handler404(request, exception):
       return render(request, '404.html')
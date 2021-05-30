from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
#from django.http import request
from . import models
from . import forms
from .models import VigTextEnc, VigTextDec, VerTextEnc, VerTextDec, TranspoTextEnc, TranspoTextDec, OwnTextEnc, OwnTextDec
User = get_user_model()
# Create your views here.
class VigOverviewPage(TemplateView):
    template_name = 'SecApp/vig/overview.html'

class VerOverviewPage(TemplateView):
    template_name = 'SecApp/ver/overview.html'

class TranspoOverviewPage(TemplateView):
    template_name = 'SecApp/transpo/overview.html'

class OwnOverviewPage(TemplateView):
    template_name = 'SecApp/own/overview.html'

class VigTextEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VigTextEncModelForm
    template_name = 'SecApp/vig/vig_enc_create_form.html'
    model = models.VigTextEnc

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class VigTextDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VigTextDecModelForm
    template_name = 'SecApp/vig/vig_dec_create_form.html'
    model = models.VigTextDec

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class VerTextEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VerTextEncModelForm
    template_name = 'SecApp/ver/ver_enc_create_form.html'
    model = models.VerTextEnc

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class VerTextDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VerTextDecModelForm
    template_name = 'SecApp/ver/ver_dec_create_form.html'
    model = models.VerTextDec

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class TranspoTextEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.TranspoTextEncModelForm
    template_name = 'SecApp/transpo/transpo_enc_create_form.html'
    model = models.TranspoTextEnc

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class TranspoTextDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.TranspoTextDecModelForm
    template_name = 'SecApp/transpo/transpo_dec_create_form.html'
    model = models.TranspoTextDec

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class OwnTextEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.OwnTextEncModelForm
    template_name = 'SecApp/own/own_enc_create_form.html'
    model = models.OwnTextEnc

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class OwnTextDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.OwnTextDecModelForm
    template_name = 'SecApp/own/own_dec_create_form.html'
    model = models.OwnTextDec

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class VigFileEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VigFileEncModelForm
    template_name = 'SecApp/vig/vig_enc_create_file.html'
    model = models.VigFileEnc

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def upload(request):
        template = 'SecApp/vig/vig_enc_create_file.html'
        if request.method == 'POST':
            form = forms.VigFileEncModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return reverse_lazy('home')
        else:
            form = forms.VigFileEncModelForm()
        return render(request, 'SecApp/vig/vig_enc_create_file.html', {'form': form})

class CryptoListView(LoginRequiredMixin,ListView):
    template_name = 'SecApp/list.html'
    context_object_name = 'list'

    def get_queryset(self):
        queryset = VigTextEnc.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CryptoListView, self).get_context_data(**kwargs)
        VigTextDec_list = VigTextDec.objects.all()
        VerTextEnc_list = VerTextEnc.objects.all()
        VerTextDec_list = VerTextDec.objects.all()
        TranspoTextEnc_list = TranspoTextEnc.objects.all()
        TranspoTextDec_list = TranspoTextDec.objects.all()
        OwnTextEnc_list = OwnTextEnc.objects.all()
        OwnTextDec_list = OwnTextDec.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            VigTextDec_list = VigTextDec_list.filter(user=username)
            VerTextEnc_list = VerTextEnc_list.filter(user=username)
            VerTextDec_list = VerTextDec_list.filter(user=username)
            TranspoTextEnc_list = TranspoTextEnc_list.filter(user=username)
            TranspoTextDec_list = TranspoTextDec_list.filter(user=username)
            OwnTextEnc_list = OwnTextEnc_list.filter(user=username)
            OwnTextDec_list = OwnTextDec_list.filter(user=username)
        context['VigTextDec_list'] = VigTextDec_list
        context['VerTextEnc_list'] = VerTextEnc_list
        context['VerTextDec_list'] = VerTextDec_list
        context['TranspoTextEnc_list'] = TranspoTextEnc_list
        context['TranspoTextDec_list'] = TranspoTextDec_list
        context['OwnTextEnc_list'] = OwnTextEnc_list
        context['OwnTextDec_list'] = OwnTextDec_list
        return context

class VigTextEncDetailView(LoginRequiredMixin,DetailView):
    model = models.VigTextEnc
    context_object_name = 'detail'
    template_name = 'SecApp/vig/vig_text_enc_detail.html'

class VigTextDecDetailView(LoginRequiredMixin,DetailView):
    model = models.VigTextDec
    context_object_name = 'detail'
    template_name = 'SecApp/vig/vig_text_dec_detail.html'

class VerTextEncDetailView(LoginRequiredMixin,DetailView):
    model = models.VerTextEnc
    context_object_name = 'detail'
    template_name = 'SecApp/ver/ver_text_enc_detail.html'

class VerTextDecDetailView(LoginRequiredMixin,DetailView):
    model = models.VerTextDec
    context_object_name = 'detail'
    template_name = 'SecApp/ver/ver_text_dec_detail.html'

class TranspoTextEncDetailView(LoginRequiredMixin,DetailView):
    model = models.TranspoTextEnc
    context_object_name = 'detail'
    template_name = 'SecApp/transpo/transpo_text_enc_detail.html'

class TranspoTextDecDetailView(LoginRequiredMixin,DetailView):
    model = models.TranspoTextDec
    context_object_name = 'detail'
    template_name = 'SecApp/transpo/transpo_text_dec_detail.html'

class OwnTextEncDetailView(LoginRequiredMixin,DetailView):
    model = models.OwnTextEnc
    context_object_name = 'detail'
    template_name = 'SecApp/own/own_text_enc_detail.html'

class OwnTextDecDetailView(LoginRequiredMixin,DetailView):
    model = models.OwnTextDec
    context_object_name = 'detail'
    template_name = 'SecApp/own/own_text_dec_detail.html'

class VigTextEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VigTextEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class VigTextDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VigTextDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class VerTextEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VerTextEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class VerTextDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VerTextDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class TranspoTextEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.TranspoTextEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class TranspoTextDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.TranspoTextDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class OwnTextEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.OwnTextEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class OwnTextDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.OwnTextDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

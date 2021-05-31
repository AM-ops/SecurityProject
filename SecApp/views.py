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
from .models import VigTextEnc, VigTextDec, VerTextEnc, VerTextDec, TranspoTextEnc, TranspoTextDec, OwnTextEnc, OwnTextDec, VigFileEnc, VigFileDec, VerFileEnc, VerFileDec, TranspoFileEnc, TranspoFileDec, OwnFileDec, OwnFileEnc
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

class VigFileDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VigFileDecModelForm
    template_name = 'SecApp/vig/vig_dec_create_file.html'
    model = models.VigFileDec


class VerFileEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VerFileEncModelForm
    template_name = 'SecApp/ver/ver_enc_create_file.html'
    model = models.VerFileEnc

class VerFileDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.VerFileDecModelForm
    template_name = 'SecApp/ver/ver_dec_create_file.html'
    model = models.VerFileDec

class TranspoFileEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.TranspoFileEncModelForm
    template_name = 'SecApp/transpo/transpo_enc_create_file.html'
    model = models.TranspoFileEnc

class TranspoFileDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.TranspoFileDecModelForm
    template_name = 'SecApp/transpo/transpo_dec_create_file.html'
    model = models.TranspoFileDec

class OwnFileEncCreate(LoginRequiredMixin,CreateView):
    form_class = forms.OwnFileEncModelForm
    template_name = 'SecApp/own/own_enc_create_file.html'
    model = models.OwnFileEnc

class OwnFileDecCreate(LoginRequiredMixin,CreateView):
    form_class = forms.OwnFileDecModelForm
    template_name = 'SecApp/own/own_dec_create_file.html'
    model = models.OwnFileDec


#ListView

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

        VigFileEnc_list = VigFileEnc.objects.all()
        VigFileDec_list = VigFileDec.objects.all()
        VerFileEnc_list = VerFileEnc.objects.all()
        VerFileDec_list = VerFileDec.objects.all()
        TranspoFileEnc_list = TranspoFileEnc.objects.all()
        TranspoFileDec_list = TranspoFileDec.objects.all()
        OwnFileEnc_list = OwnFileEnc.objects.all()
        OwnFileDec_list = OwnFileDec.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            VigTextDec_list = VigTextDec_list.filter(user=username)
            VerTextEnc_list = VerTextEnc_list.filter(user=username)
            VerTextDec_list = VerTextDec_list.filter(user=username)
            TranspoTextEnc_list = TranspoTextEnc_list.filter(user=username)
            TranspoTextDec_list = TranspoTextDec_list.filter(user=username)
            OwnTextEnc_list = OwnTextEnc_list.filter(user=username)
            OwnTextDec_list = OwnTextDec_list.filter(user=username)

            VigFileEnc_list = VigFileEnc_list.filter(user=username)
            VigFileDec_list = VigFileDec_list.filter(user=username)
            VerFileEnc_list = VerFileEnc_list.filter(user=username)
            VerFileDec_list = VerFileDec_list.filter(user=username)
            TranspoFileEnc_list = TranspoFileEnc_list.filter(user=username)
            TranspoFileDec_list = TranspoFileDec_list.filter(user=username)
            OwnFileEnc_list = OwnFileEnc_list.filter(user=username)
            OwnFileDec_list = OwnFileDec_list.filter(user=username)
        context['VigTextDec_list'] = VigTextDec_list
        context['VerTextEnc_list'] = VerTextEnc_list
        context['VerTextDec_list'] = VerTextDec_list
        context['TranspoTextEnc_list'] = TranspoTextEnc_list
        context['TranspoTextDec_list'] = TranspoTextDec_list
        context['OwnTextEnc_list'] = OwnTextEnc_list
        context['OwnTextDec_list'] = OwnTextDec_list

        context['VigFileEnc_list'] = VigFileEnc_list
        context['VigFileDec_list'] = VigFileDec_list
        context['VerFileEnc_list'] = VerFileEnc_list
        context['VerFileDec_list'] = VerFileDec_list
        context['TranspoFileEnc_list'] = TranspoFileEnc_list
        context['TranspoFileDec_list'] = TranspoFileDec_list
        context['OwnFileEnc_list'] = OwnFileEnc_list
        context['OwnFileDec_list'] = OwnFileDec_list
        return context


#DetailViews

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

class VigFileEncDetailView(LoginRequiredMixin,DetailView):
    model = models.VigFileEnc
    context_object_name = 'detail'
    template_name = 'SecApp/vig/vig_file_enc_detail.html'

class VigFileDecDetailView(LoginRequiredMixin,DetailView):
    model = models.VigFileDec
    context_object_name = 'detail'
    template_name = 'SecApp/vig/vig_file_dec_detail.html'

class VerFileEncDetailView(LoginRequiredMixin,DetailView):
    model = models.VerFileEnc
    context_object_name = 'detail'
    template_name = 'SecApp/ver/ver_file_enc_detail.html'

class VerFileDecDetailView(LoginRequiredMixin,DetailView):
    model = models.VerFileDec
    context_object_name = 'detail'
    template_name = 'SecApp/ver/ver_file_dec_detail.html'

class TranspoFileEncDetailView(LoginRequiredMixin,DetailView):
    model = models.TranspoFileEnc
    context_object_name = 'detail'
    template_name = 'SecApp/transpo/transpo_file_enc_detail.html'

class TranspoFileDecDetailView(LoginRequiredMixin,DetailView):
    model = models.TranspoFileDec
    context_object_name = 'detail'
    template_name = 'SecApp/transpo/transpo_file_dec_detail.html'

class OwnFileEncDetailView(LoginRequiredMixin,DetailView):
    model = models.OwnFileEnc
    context_object_name = 'detail'
    template_name = 'SecApp/own/own_file_enc_detail.html'

class OwnFileDecDetailView(LoginRequiredMixin,DetailView):
    model = models.OwnFileDec
    context_object_name = 'detail'
    template_name = 'SecApp/own/own_file_dec_detail.html'

#Delete Views

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

class VigFileEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VigFileEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class VigFileDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VigFileDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class VerFileEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VerFileEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class VerFileDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.VerFileDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class TranspoFileEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.TranspoFileEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class TranspoFileDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.TranspoFileDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class OwnFileEncDeleteView(LoginRequiredMixin,DeleteView):
    model = models.OwnTextEnc
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

class OwnFileDecDeleteView(LoginRequiredMixin,DeleteView):
    model = models.OwnFileDec
    template_name = 'SecApp/delete.html'
    success_url = reverse_lazy('SecApp:list')

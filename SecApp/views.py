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
from .models import VigTextEnc, VigTextDec, VerTextEnc, VerTextDec, TranspoTextEnc, TranspoTextDec

# Create your views here.
class VigOverviewPage(TemplateView):
    template_name = 'SecApp/vig/overview.html'

class VerOverviewPage(TemplateView):
    template_name = 'SecApp/ver/overview.html'

class TranspoOverviewPage(TemplateView):
    template_name = 'SecApp/transpo/overview.html'

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



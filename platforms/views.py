from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from .models import Platform
from .forms import PlatformForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class PlatformCreateView(LoginRequiredMixin, CreateView):
    form_class = PlatformForm
    model = Platform
    template_name ='platforms/platform_form.html'
    
    def get_success_url(self) -> str:
        return reverse("platforms:list")
class PlatformUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PlatformForm
    model = Platform
    template_name ='platforms/platform_form.html'

    def get_success_url(self) -> str:
        return reverse("platforms:list")

class PlatformLitView(LoginRequiredMixin, ListView):
    model = Platform


class PlatformDetailView(LoginRequiredMixin, DetailView):
    model = Platform
    
class PlatformConfirmDeleteView(LoginRequiredMixin, DeleteView):
    model = Platform
    
    def get_success_url(self) -> str:
        return reverse("platforms:list")
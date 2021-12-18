from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.views.generic.base import View

from .forms import PlatformPasswordForm
from .models import PlatformPassword
from .mixins import MasterPasswordRequiredMixin

class PlatformPasswordDeleteView(LoginRequiredMixin, MasterPasswordRequiredMixin, DeleteView):
    model = PlatformPassword
    template_name = 'passwords/password_delete.html'

    def get_success_url(self):
        return reverse("passwords:list")


class PlatformDetailView(LoginRequiredMixin, MasterPasswordRequiredMixin, DetailView):
    model = PlatformPassword
    template_name = 'passwords/password_detail.html'


class PlatformPasswordUpdateView(LoginRequiredMixin, MasterPasswordRequiredMixin, UpdateView):
    model = PlatformPassword
    template_name = 'passwords/passwords_form.html'
    form_class = PlatformPasswordForm

    def get_success_url(self):
        return reverse("passwords:list")


class PasswordListView(LoginRequiredMixin, ListView):
    model = PlatformPassword
    template_name = 'passwords/passwords_list.html'


class PlatformPasswordCreateView(LoginRequiredMixin, MasterPasswordRequiredMixin, CreateView):
    model = PlatformPassword
    template_name = 'passwords/passwords_form.html'
    form_class = PlatformPasswordForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("passwords:list")

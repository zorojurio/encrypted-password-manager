from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.views.generic.base import View

from .forms import MasterForm, PlatformPasswordForm
from .models import PlatformPassword


class CheckMasterView(View):
    def get(self, request, *args, **kwargs):
        form = MasterForm()
        context = {
            'form': form
        }
        return render(request=request, template_name='passwords/master.html', context=context)
        
    
    def post(self, request, *args, **kwargs):
        form = MasterForm(request.POST)
        if form.is_valid():
            master = form.cleaned_data.get('master')
            print(master)
        context = {
            'form': form
        }
        return render(request=request, template_name='passwords/master.html', context=context)
    
class PlatformPasswordDeleteView(LoginRequiredMixin, DeleteView):
    model = PlatformPassword
    template_name = 'passwords/password_delete.html'

    def get_success_url(self):
        return reverse("passwords:list")


class PlatformDetailView(LoginRequiredMixin, DetailView):
    model = PlatformPassword
    template_name = 'passwords/password_detail.html'


class PlatformPasswordUpdateView(LoginRequiredMixin, UpdateView):
    model = PlatformPassword
    template_name = 'passwords/passwords_form.html'
    form_class = PlatformPasswordForm

    def get_success_url(self):
        return reverse("passwords:list")


class PasswordListView(LoginRequiredMixin, ListView):
    model = PlatformPassword
    template_name = 'passwords/passwords_list.html'


class PlatformPasswordCreateView(LoginRequiredMixin, CreateView):
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

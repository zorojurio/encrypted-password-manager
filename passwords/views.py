from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import  UpdateView, DetailView, DeleteView, ListView, CreateView
from django.views.generic.base import View
from masters.utils import decrypt_password, encrypt_platform_password
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
    
    
    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            master_password = self.request.session.get('master_password')
            self.object.password = decrypt_password(master_password, self.object.password)
            print(self.object.password)
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return context
    


class PlatformPasswordUpdateView(LoginRequiredMixin, MasterPasswordRequiredMixin, UpdateView):
    model = PlatformPassword
    template_name = 'passwords/passwords_form.html'
    form_class = PlatformPasswordForm

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            master_password = self.request.session.get('master_password')
            self.object.password = decrypt_password(master_password, self.object.password)
            kwargs.update({'instance': self.object})
        return kwargs
    
    def get_success_url(self):
        return reverse("passwords:list")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        print(self.request.session.get('master_password'))
        master_password = self.request.session.get('master_password')
        if master_password:
            self.object = form.save(commit=False)
            form_password = form.cleaned_data.get('password')
            print(form_password)
            self.object.password = encrypt_platform_password(master_password, form_password)
            self.object.save()
        return super().form_valid(form)

class PasswordListView(LoginRequiredMixin, MasterPasswordRequiredMixin, ListView):
    model = PlatformPassword
    template_name = 'passwords/passwords_list.html'


class PlatformPasswordCreateView(LoginRequiredMixin, MasterPasswordRequiredMixin, CreateView):
    model = PlatformPassword
    template_name = 'passwords/passwords_form.html'
    form_class = PlatformPasswordForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        master_password = self.request.session.get('master_password')
        if master_password:
            self.object = form.save(commit=False)
            form_password = form.cleaned_data.get('password')
            print(form_password)
            self.object.password = encrypt_platform_password(master_password, form_password)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("passwords:list")

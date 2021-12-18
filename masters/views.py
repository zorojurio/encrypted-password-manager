from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, View
from .models import MasterPassword
from .forms import CheckMasterPasswordForm, MastersPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from masters.utils import encrypt_master_password


class MasterCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = MastersPasswordForm()
        context = {
            'form': form
        }
        return render(request=request, template_name='masters/masters_form.html', context=context)
    
    def post(self, request, *args, **kwargs):
        form = MastersPasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            master_password_qs = MasterPassword.objects.filter(user=user)
            print(master_password_qs)
            if master_password_qs.exists():
                print("master password is already created")
                messages.warning(request, 'You have already created your master password')
            else:
                master_password = form.save(commit=False)
                master_password.user = user
                master_password.save()
        else:
            print(form.errors)
        context = {
            'form': form
        }
        return render(request=request, template_name='masters/masters_form.html', context=context)


class CheckMasterView(View):
    def get(self, request, *args, **kwargs):
        form = CheckMasterPasswordForm()
        context = {
            'form': form
        }
        return render(request=request, template_name='passwords/master.html', context=context)
        
    
    def post(self, request, *args, **kwargs):
        form = CheckMasterPasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            master_password_qs = MasterPassword.objects.filter(user=user)
            if master_password_qs.exists():
                decrypted_master = master_password_qs.first().password
                form_master_pass = form.cleaned_data.get('master')
                decrypted_form_master_pass = encrypt_master_password(form_master_pass)
                if str(decrypted_form_master_pass) == str(decrypted_master):
                    request.session['master_password'] = form_master_pass
                else:
                    messages.warning(request=request, message="Wrong Master password")
        context = {
            'form': form
        }
        return render(request=request, template_name='passwords/master.html', context=context)

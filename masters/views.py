from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, View
from .models import MasterPassword
from .forms import CheckMasterPasswordForm, MastersPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from masters.utils import encrypt_master_password


class MasterCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        master_password_qs = MasterPassword.objects.filter(user=request.user)
        if master_password_qs.exists():
            messages.warning(request, 'You have already created your master password please enter the master pasword to continue')
            return redirect("masters:check")
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
                messages.warning(request, 'You have already created your master password')
                return redirect("masters:check")
            else:
                master_password = form.save(commit=False)
                master_password.user = user
                master_password.save()
                request.session['master_password'] = form.cleaned_data.get('password')
                return redirect("passwords:list")
        else:
            print(form.errors)
        context = {
            'form': form
        }
        return render(request=request, template_name='masters/masters_form.html', context=context)


class CheckMasterView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CheckMasterPasswordForm()
        master_password_qs = MasterPassword.objects.filter(user=request.user)
        if not master_password_qs.exists():
            return redirect("masters:create")
        context = {
            'form': form
        }
        return render(request=request, template_name='masters/check.html', context=context)
        
    
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
                    next_url = request.GET.get('next')
                    if next_url:
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect("passwords:list")
                else:
                    messages.warning(request=request, message="Wrong Master password")
            else:
                return redirect("masters:create")
        context = {
            'form': form
        }
        return render(request=request, template_name='masters/check.html', context=context)

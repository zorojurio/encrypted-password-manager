from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, View
from .models import MasterPassword
from .forms import MastersPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
# MasterCreateView, MasterUpdateView, MasterCheckView


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
            master_password_qs = MasterPassword.objects.filter(user=request.user)
        context = {
            'form': form
        }
        return render(request=request, template_name='masters/masters_form.html', context=context)


class MasterCheckView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='masters/masters_form.html')

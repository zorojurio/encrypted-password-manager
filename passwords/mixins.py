import django.contrib.auth.models

from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse


class MasterPasswordRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('master_password'):
            redirect_url = reverse("masters:check")
            return redirect(f"{redirect_url}?next={request.path}")
        return super().dispatch(request, *args, **kwargs)

from django.urls import path
from .views import MasterCreateView, CheckMasterView

app_name='masters'
urlpatterns = [
    path('create/', MasterCreateView.as_view(), name='create'),
    path('check/', CheckMasterView.as_view(), name='check'),
]
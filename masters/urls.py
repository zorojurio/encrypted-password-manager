from django.urls import path
from .views import MasterCreateView, MasterCheckView

app_name='masters'
urlpatterns = [
    path('create/', MasterCreateView.as_view(), name='create'),
    path('check/', MasterCheckView.as_view(), name='check'),
]
from django.urls import path

from .views import (
    PasswordListView,
    PlatformPasswordCreateView,
    PlatformDetailView,
    PlatformPasswordUpdateView,
    PlatformPasswordDeleteView,
    CheckMasterView
)

app_name = 'passwords'
urlpatterns = [
    path('check/', CheckMasterView.as_view(), name='check'),
    path('', PasswordListView.as_view(), name='list'),
    path('create/', PlatformPasswordCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PlatformPasswordUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', PlatformDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', PlatformPasswordDeleteView.as_view(), name='delete'),
]

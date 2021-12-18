from django.urls import path

from .views import (
    PasswordListView,
    PlatformPasswordCreateView,
    PlatformDetailView,
    PlatformPasswordUpdateView,
    PlatformPasswordDeleteView,
)

app_name = 'passwords'
urlpatterns = [
    path('', PasswordListView.as_view(), name='list'),
    path('create/', PlatformPasswordCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PlatformPasswordUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', PlatformDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', PlatformPasswordDeleteView.as_view(), name='delete'),
]

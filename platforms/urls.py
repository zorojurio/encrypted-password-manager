from django.urls import path
from .views import PlatformCreateView, PlatformLitView, PlatformUpdateView, PlatformDetailView, PlatformConfirmDeleteView

app_name = "platforms"
urlpatterns = [
    path('create/', PlatformCreateView.as_view(), name='create'),
    path('list/', PlatformLitView.as_view(), name='list'),
    path('list/', PlatformLitView.as_view(), name='list'),
    path('<int:pk>/update/', PlatformUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', PlatformDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', PlatformConfirmDeleteView.as_view(), name='delete'),
]
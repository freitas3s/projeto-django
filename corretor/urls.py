
from django.urls import path
from django.conf.urls.static import static
from corretor import views
from django.conf import settings

app_name = 'corretor'

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

"""URLs principales del proyecto: incluyen las URLs de la app 'principal'."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Agrega esta línea ANTES de las demás
    path('admin/login/', LoginView.as_view(template_name='admin/login.html'), name='admin-login'),
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),  # todas las páginas del sitio
]

# ✅ ESTO es lo que te faltaba:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
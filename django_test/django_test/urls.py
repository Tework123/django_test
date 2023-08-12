from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_test import settings
from men.views import main, pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    # path('men/<int:men_id>/', include('men.urls')),
    path('authentication/', include('authentication.urls')),
    path('men/', include('men.urls')),
    path('women/', include('women.urls')),
    path("__debug__/", include("debug_toolbar.urls"))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

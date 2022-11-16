from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("rest_framework.urls")),
    path("api/", include("api.urls", namespace="api")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("mainapp.urls", namespace="mainapp")),
    path("users/", include("userapp.urls", namespace="users")),
    path("dev_authors/", include("devautorapp.urls", namespace="devautorapp")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "mainapp.views.error_400_view"
handler403 = "mainapp.views.error_403_view"
handler404 = "mainapp.views.error_404_view"
handler500 = "mainapp.views.error_500_view"

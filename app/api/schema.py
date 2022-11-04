from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions

from django.urls import path, include, re_path


schema_view = get_schema_view(  # new
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=[
        path("api/", include("api.urls")),
    ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

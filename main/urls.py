from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .router import router
from rest_framework.authtoken import views as restviews

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', restviews.obtain_auth_token, name="api-token-auth")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
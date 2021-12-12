from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairCustomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('user/', include('accounts.urls')),
    path("api/v1/items/", include("items.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairCustomView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
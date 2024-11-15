from django.urls import path, include, re_path

urlpatterns = [
    path('v1/', include('core.api.v1.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gamestore import views

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
router.register(r'users', views.CustomUserViewSet)
# router.register(r'users', views.user_list)
router.register(r'games', views.GameViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'publishers', views.PublisherViewSet)
# router.register(r'users/(?P<pk>[0-9]+)$', views.user_details)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/users/', views.user_list),
    # path('api/users/(?P<pk>[0-9]+)$', views.user_details),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

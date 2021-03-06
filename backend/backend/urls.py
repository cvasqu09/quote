"""backend URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from app.viewsets import UserViewSet, QuoteViewSet, QuoterViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'quote', QuoteViewSet, basename='quote')
router.register(r'quoter', QuoterViewSet, basename='quoter')
router.register(r'like', LikeViewSet, basename='like')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', obtain_auth_token, name='obtain_auth_token'),
              ] + router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('debug/', include(debug_toolbar.urls))]

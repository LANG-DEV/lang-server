"""Lang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from server import views

router = routers.DefaultRouter()
router.register(r'identity', views.IdentityViewSet)
router.register(r'lang_group', views.LangGroupViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'chat_room', views.ChatRoomViewSet)
router.register(r'board', views.BoardViewSet)
router.register(r'location', views.LocationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
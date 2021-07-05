"""admin URL Configuration

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
from django.urls import path

from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin

# from django.conf.urls import url, include
from common.views import Connection
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

# from board import views
# router = routers.DefaultRouter()
# router.register(r'member', views.MemberViewSet)
# router.register(r'board', views.BoardViewSet)


urlpatterns = [
    path('connection', Connection.as_view()),
    #url('^api/post', include('board.urls')),
    url(r'^api/member/', include('member.urls')), #  프로젝트 urls에 넘어옴 그것을 다시 app에 urls 로 넘겨준다
    url(r'^adm/member/', include('member.urls')),
    url(r'^api/post/', include('board.urls')),
]
''' CBV
from common.views import Connection
from django.urls import path, include
from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    path('connection', Connection.as_view()),
    path('board', include('board.urls')),
    path('member', include('member.urls')),

]
'''
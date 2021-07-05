from django.urls import path
from . import views  # 시블린관계에서는 . 사용

from django.conf.urls import url
from .views import Posts
urlpatterns = [
    url('/post',Posts.as_view()), # 프로젝트 urls 에서 넘어온것을 다시 view로
]
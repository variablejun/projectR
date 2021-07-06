from django.conf.urls import url
from django.urls import path
from member import views

urlpatterns = [# 프로젝트 urls 에서 넘어온것을 다시 view로
    url(r'^register', views.members),
    url(r'^list', views.members),
    url(r'^login', views.login),
    path('delete/<slug:pk>', views.member),
    url(r'^modify', views.member_modify),

]
'''  CBV
from django.conf.urls import url
from .views import Members as members
from .views import Member as member
from django.urls import path, include
urlpatterns = [
    url('/register', members.as_view()),
    path('/<int:pk>/', member.as_view()),
]'''
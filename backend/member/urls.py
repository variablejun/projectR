from django.conf.urls import url
from member import views

urlpatterns = [
    url(r'^register', views.members),  # 프로젝트 urls 에서 넘어온것을 다시 view로
    url(r'^list', views.members),

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
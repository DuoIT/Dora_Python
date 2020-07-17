from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'question/', views.viewquestion, name="viewlistquestion"),
    url(r'index/', views.index, name="home"),
    url(r'detail/', views.viewlist, name="viewlist"),
    url(r'answer/', views.viewanswer, name="viewanswer"),
    url(r'view/(?P<question_id>[0-9]+)/$', views.detailView, name="detailquestion"),
    url(r'login/', views.login, name="login"),
    url(r'^(?P<question_id>[0-9]+)/$', views.vote, name="vote")
]

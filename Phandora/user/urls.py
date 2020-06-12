from django.conf.urls import url

from user import views

app_name = 'user'

urlpatterns = [
    url(r'^user/$', views.CreateUserView.as_view(), name='User'),
    url(r'^token/$', views.CreateTokenView.as_view(), name='Token'),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserDetailView.as_view()),
]

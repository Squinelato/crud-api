from django.conf.urls import url

from user import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Phandora API')

app_name = 'user'

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/user$', views.CreateUserView.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)$', views.UserDetailView.as_view()),
]
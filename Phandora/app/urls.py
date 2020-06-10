from django.conf.urls import url
from app import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Phandora API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/app$', views.AppListView.as_view()),
    url(r'^api/app/(?P<pk>[0-9]+)$', views.AppDetailsView.as_view())
]

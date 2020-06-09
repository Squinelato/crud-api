from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^api/app$', views.app_list),
    url(r'^api/app/(?P<pk>[0-9]+)$', views.app_detail),
    url(r'^api/app/supers$', views.app_list_supers)
]

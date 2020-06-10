from rest_framework.schemas import AutoSchema
from rest_framework import generics

from app.models import App
from app.serializers import AppSerializer

import coreapi

class AppSchema(AutoSchema):
    
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('name'),
                coreapi.Field('email'),
                coreapi.Field('password'),
                coreapi.Field('status'),
                coreapi.Field('permission'),                
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class AppListView(generics.ListCreateAPIView):

    schema = AppSchema()
    queryset = App.objects.all()
    serializer_class = AppSerializer

class AppDetailsView(generics.RetrieveUpdateDestroyAPIView):

    schema = AppSchema()
    queryset = App.objects.all()
    serializer_class = AppSerializer


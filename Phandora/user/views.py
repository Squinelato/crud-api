from rest_framework.schemas import AutoSchema
from rest_framework import generics

from app.models import User
from user.serializers import UserSerializer

import coreapi


class UserSchema(AutoSchema):
    
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('name'),
                coreapi.Field('email'),
                coreapi.Field('password'),
                coreapi.Field('is_staff'),
                coreapi.Field('is_active'),                
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class CreateUserView(generics.ListCreateAPIView):
    """Create a new user and list them in the system"""
    schema = UserSchema()
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, updated, delete users"""
    schema = UserSchema()
    queryset = User.objects.all()
    serializer_class = UserSerializer

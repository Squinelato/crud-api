from rest_framework.schemas import AutoSchema
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from app.models import User

from user.serializers import UserSerializer, AuthTokenSerializer

import coreapi


class UserSchema(AutoSchema):
    """Creating a Schema for CRUD operations"""
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('name'),
                coreapi.Field('email'),
                coreapi.Field('password'),
                coreapi.Field('is_active'),                
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class TokenSchema(AutoSchema):
    """Create a schema for token POSTs"""
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('email'),
                coreapi.Field('password'),             
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class CreateUserView(generics.ListCreateAPIView):
    """Create a new user and list them in the system"""
    schema = UserSchema()
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    schema = TokenSchema()
    serializer_class = AuthTokenSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, updated, delete users"""
    schema = UserSchema()
    queryset = User.objects.all()
    serializer_class = UserSerializer

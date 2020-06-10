from rest_framework import serializers
from app.models import App


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = ('id',
                  'name',
                  'email',
                  'password',
                  'status',
                  'permission')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = App(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user 
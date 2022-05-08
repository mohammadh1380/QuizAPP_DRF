from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        email=validated_data['email'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

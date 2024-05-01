from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

class AccountSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        # 비밀번호 유효성 검사
        validate_password(value)
        # 비밀번호 해싱
        return make_password(value)
    def validate_birth_date(self, value):
        if value is None:
            raise ValidationError("Birth date cannot be null.")
        return value

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'birth_date',
        )

class AccountDetailSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
        )
        
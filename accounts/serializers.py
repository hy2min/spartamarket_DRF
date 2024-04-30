from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
        )
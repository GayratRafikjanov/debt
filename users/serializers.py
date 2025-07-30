from rest_framework import serializers
from .models import CustomUser


# FOYDALANUVCHI SERIALIZERLARI
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number']



# FOYDALANUVCHI RO'YXATI (GET)
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'is_active',
                  'is_staff', 'is_admin', 'is_superuser', 'date_joined', 'created_at', 'updated_at')



# FOYDALANUVCHI YARATISH (POST)
class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        min_length=10,
        max_length=44,
        required=True
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

        extra_kwargs = {
            'email': {
                'error_messages': {
                    'required': 'Email is required',
                    'invalid': 'Invalid email format'
                },
                'help_text': 'Please enter a valid email address. It should be unique and not already in use.'
            },
            'password': {
                'error_messages': {
                    'required': 'Password is required',
                    'min_length': 'Password must be at least 8 characters long'
                },
                'help_text': 'Your password must be at least 8 characters long.'
            }
        }




    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        """
            foydalanuvchi parolni yubora oladi (POST orqali)
            lekin API javobi Response da parol ko‘rinmaydi
        """

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # safe password yozadi
        user.save()
        return user



# FOYDALANUVCHI DETALLARI (GET)
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'is_active',
                  'is_staff', 'is_admin', 'is_superuser', 'date_joined', 'created_at', 'updated_at')


# FOYDALANUVCHI YANGILASH (PUT)
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')



# FOYDALANUVCHI OCHIRISH (DELETE)
class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')
        extra_kwargs = {'email': {'write_only': True}}

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
    """
    User create qilinib database ga saqlanayotganda
    kerakli bo'lgan muhim parametrlarni saqlash metodi
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    """
        create superuser
        this method is used to when we create a superuser IN TERMINAL 
        with command: python manage.py createsuperuser

    """
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        user = self.create_user(email, password, **extra_fields)
        user.save()
        return user



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

"""
    User registration page da korsatiladigan table
"""
class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=17, blank=True)
    username = None
    """
        None sababi, user creation bolayotganda agar None bolmasa, 
        2 ta bir xil username boladi va bu 
        "!!!!  UNIQUE constraint  !!!!" degan xatolik beradi, 
        yani NULL username field lik username already exists degan xatolik beradi
    """

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}, {self.first_name}'


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

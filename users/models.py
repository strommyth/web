from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, id_numbers, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser 必須有管理員權限')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser 必須啟用')

        return self.create_user(id_numbers, email, user_name, password, **other_fields)

    def create_user(self, id_numbers, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('請輸入電子信箱'))

        email = self.normalize_email(email)
        user = self.model(id_numbers=id_numbers, email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    id_numbers = models.CharField(_('身分證字號'), max_length=150, unique=True)
    email = models.EmailField(_('電子信箱'), unique=True)
    user_name = models.CharField(_('姓名'), max_length=150)
    about = models.TextField(_( '關於'), max_length=500, blank=True)
    is_staff = models.BooleanField(_('管理員'), default=False)
    is_active = models.BooleanField(_('啟用'), default=True)

    state_choices = (
        ("SEC404", "階段一"),
        ("SEC303", "階段二"),
        ("SEC202", "階段三"),
    )

    is_state = models.CharField(max_length=150, choices=state_choices, default="SEC404")



    objects = CustomAccountManager()

    USERNAME_FIELD = 'id_numbers'
    REQUIRED_FIELDS = ['user_name', 'email']

    def __str__(self):
        return self.user_name
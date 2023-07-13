from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import  BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password=None):
        """ Create and save a User with the given email and password """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, first_name, last_name):
        """ Create and save a SuperUser with the given email and password. """

        user = self._create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
    

    def verifyAccount(self, user, user_input, code):
        if user_input == code:
            user.is_active = True
            user.save(using=self._db)
            return user


class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField(blank=False, max_length=255, unique=True, verbose_name="email address")
    first_name = models.CharField(max_length=255, verbose_name="first_name")
    last_name = models.CharField(max_length=255, verbose_name="last_name")
    profile_image = models.ImageField(null=True, blank=True) 
    # profile_image = models.ImageField(default="../media/default_avatar.png", null=True, blank=True) 
    date_of_birth = models.DateField(blank=False, null=True, verbose_name="date_of_birth")
    phone = models.CharField(blank=False, max_length=12, verbose_name="phone")
    country = models.CharField(blank=False, max_length=150, verbose_name="country")
    city = models.CharField(blank=True, max_length=150, verbose_name="city")
    zip_code = models.CharField(blank=True, max_length=5, verbose_name="zip_code")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    '''
        CUSTOM USER MANAGER WHERE EMAIL IS THE UNIQUE IDENTIFIER FOR AUTHENTICATION INSTEAD OF USERNAME.
    '''

    def create_user(self, email, password, **kwargs):

        ''' CREATES REGULAR USER. '''
        if not email:
            raise ValueError(_("The email cannot be blank."))

        email = self.normalize_email(email)
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):

        ''' CREATES SUPER USER. ''' 

        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Cannot create superuser without is_superuser property set."))

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Cannot create superuser without staff permission."))

        return self.create_user(email, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):

    ''' CUSTOM USER MODEL WITH EMAIL AS UNIQUE FIELD. '''

    email = models.EmailField(_("email address"), max_length=255, unique=True)
    name = models.CharField(_("name"),max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


    
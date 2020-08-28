from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        """ Creates a new user and saves to the db """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
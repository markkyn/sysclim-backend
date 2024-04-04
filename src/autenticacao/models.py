from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class BaseUsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        """
        Cria e retorna um usuário (assistente) com um endereço de email, nome e senha.
        """
        if not email:
            raise ValueError('Os assistentes devem ter um endereço de email válido.')
        email = self.normalize_email(email)
        assistente = self.model(email=email, nome=nome, **extra_fields)
        assistente.set_password(password)
        assistente.save(using=self._db)
        return assistente

    def create_superuser(self, email, nome, password=None, **extra_fields):
        """
        Cria e retorna um superusuário (assistente) com um endereço de email, nome e senha.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')

        return self.create_user(email, nome, password, **extra_fields)
    
class ModeloUsuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = BaseUsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'modelousuario'
        abstract = True


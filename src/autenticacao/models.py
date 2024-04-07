from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class BaseUsuarioManager(BaseUserManager):
    def create_user(self, email, cpf, nome, genero, dt_nascimento, cargo, especialidade_id, endereco_id, password=None,ativo=True, **extra_fields):
        """
        Cria e retorna um usuário (profissional) com um email, cpf, nome, genero, data de nascimento, 
        cargo, status ativo, especialidade, endereco e senha.
        """
        if not email:
            raise ValueError('Os profissionais devem ter um endereço de email válido.')
        if not cpf:
            raise ValueError('O CPF é necessário.')
        if not nome:
            raise ValueError('O nome é necessário.')
        if not genero:
            raise ValueError('O gênero é necessário.')
        if not dt_nascimento:
            raise ValueError('A data de nascimento é necessária.')
        if not cargo:
            raise ValueError('O cargo é necessário.')

        email = self.normalize_email(email)
        
        profissional = self.model(
            email=email,
            cpf=cpf,
            nome=nome,
            genero=genero,
            dt_nascimento=dt_nascimento,
            cargo=cargo,
            ativo=ativo,
            especialidade_id=especialidade_id,
            endereco_id=endereco_id,
            **extra_fields
        )
        profissional.set_password(password)
        profissional.save(using=self._db)
        
        return profissional

    def create_superuser(self, email, cpf, nome, genero, dt_nascimento, cargo, especialidade_id, endereco_id, password=None, ativo=True, **extra_fields):
        """
        Cria e retorna um superusuário (profissional) com um email, cpf, nome, genero, data de nascimento, 
        cargo, status ativo, especialidade, endereco e senha, além de marcá-lo como staff e superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')

        return self.create_user(email, cpf, nome, genero, dt_nascimento, cargo, especialidade_id, endereco_id, password, ativo, **extra_fields)
    
class ModeloUsuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = BaseUsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dt_nascimento', 'endereco_id', 'cpf', 'nome', 'genero', 'cargo', 'especialidade_id' ]

    class Meta:
        db_table = 'modelousuario'
        abstract = True


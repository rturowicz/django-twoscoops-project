from django.contrib.auth.models import BaseUserManager


class AppUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an e-mail address')
        if not name:
            raise ValueError('User must have a name')

        user = self.model(
            email=AppUserManager.normalize_email(email),
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        user = self.create_user(email, name, password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

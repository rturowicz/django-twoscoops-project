from django.contrib.auth.models import BaseUserManager


class AppUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an e-mail address')
        if not username:
            raise ValueError('User must have a name')

        user = self.model(
            email=AppUserManager.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email, username, password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

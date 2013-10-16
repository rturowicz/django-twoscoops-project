from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import AppUserManager


USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['name', ]


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
        db_index=True
    )
    name = models.CharField(max_length=255)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = USERNAME_FIELD
    REQUIRED_FIELDS = REQUIRED_FIELDS

    objects = AppUserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return '%s - %s' % (self.email, self.name)

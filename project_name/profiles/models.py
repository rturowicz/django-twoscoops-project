import os
import time

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from sorl.thumbnail import ImageField, get_thumbnail
from hashlib import md5

from .managers import AppUserManager


USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['name', ]


def generate_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = '%s_%s' % (instance.pk, str(time.time()))
    filename = '%s/%s%s' % ('profiles/avatar', md5(filename).hexdigest(), extension)

    return filename


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
        db_index=True
    )
    name = models.CharField(max_length=255)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    image = ImageField(
        verbose_name=u'Avatar',
        blank=True, null=True,
        upload_to=generate_filename
    )

    USERNAME_FIELD = USERNAME_FIELD
    REQUIRED_FIELDS = REQUIRED_FIELDS

    objects = AppUserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return '%s - %s' % (self.email, self.name)

    def avatar_thumb(self):
        if self.image:
            return '<img src="%s%s" width="80px" height="80px"/>' %\
                   (settings.MEDIA_URL, get_thumbnail(self.image, '80x80', crop='center', quality=99).name)
        else:
            return '<img src="%simg/blank_user_80_80.jpg" width="80px" height="80px"/>' % settings.STATIC_URL

    avatar_thumb.short_description = 'Avatar'
    avatar_thumb.allow_tags = True

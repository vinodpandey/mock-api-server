from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

METHOD_CHOICES = (
    # ('',''),
    ('GET', 'GET'),
    ('POST', 'POST')
)

STATUS_CHOICES = (
    # ('',''),
    ('200', '200'),
    ('401', '401'),
    ('404', '404'),
    ('503', '503')
)


# Create your models here.
class Api(models.Model):
    path = models.CharField(_('path'), max_length=255, help_text=_('e.g. /auth/signin/'))
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    response = models.TextField('response')
    is_enabled = models.BooleanField('is enabled', default=False)

    class Meta:
        ordering = ('path',)

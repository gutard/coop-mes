# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ionyweb.page.models import AbstractPageApp


class PageApp_Map(AbstractPageApp):

    # Define your fields here
    bdis = models.BooleanField(u'Afficher la BDIS plutôt que la PASR')

    def __unicode__(self):
        return u'Map #%d' % (self.pk)

    class Meta:
        verbose_name = _(u"Map")
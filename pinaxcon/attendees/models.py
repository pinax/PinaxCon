# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



@python_2_unicode_compatible
class Attendee(models.Model):
    NONE = 'NON'
    VEGETARIANO = 'VEG'
    VEGANO = 'VGN'
    BAJO_SODIO = 'SOD'
    CELIACO = 'CEL'
    OTROS = 'CEL'
    FOOD_PREFERENCE_CHOICES = (
        (NONE, 'No tengo preferencia/necesidad'),
        (BAJO_SODIO, 'Bajo en sodio'),
        (VEGANO, 'Vegano'),
        (VEGETARIANO, 'Vegetariano'),
        (CELIACO, 'Celiaco'),
        (OTROS, 'Otros'),)


    user = models.OneToOneField(User, null=True, related_name="attendee", verbose_name=_("User"))
    full_name = models.CharField(verbose_name="Nombre completo o nick", max_length=100,
                            help_text=(u"Como te gustaría que se imprima en tu"
                                        " gafete.(si querés puede ser un nick)"))
    annotation = models.TextField(verbose_name="Observaciones",
                                  help_text=("Si tenés alguna necesidad"
                                      "especial que necesites que"
                                      "contemplemos,"
                                      "por favor completa este campo"))
    food_preference = ArrayField(
        models.CharField(verbose_name="Preferencia o necesidad alimenticia",
                                  help_text=("Vas a poder comprar y reservar"
                                      "tus viandas por internet previo al"
                                      "evento(preferentemente), o en el lugar"
                                      "completando este campo nos aseguramos"
                                      "de poder cubrir las necesidades de todos"),
			choices=FOOD_PREFERENCE_CHOICES, max_length=3,
                        blank=True, default=NONE),)

    registration_date = models.DateTimeField(auto_now_add=True,
        editable=False)
    cv = models.FileField(upload_to="attendees_cvs", blank=True,
            verbose_name="Curriculum vitae")
    show_to_sponsor = models.BooleanField( help_text=("Acepto que mis datos"
        "personales se compartan con los sponsors"))

    class Meta:
        ordering = ['full_name']
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"

    def __str__(self):
        if self.user:
            return self.full_name
        else:
            return "?"

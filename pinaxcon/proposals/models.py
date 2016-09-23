# -*- coding: utf-8 -*-
from django.db import models

from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, "Principiante"),
        (AUDIENCE_LEVEL_INTERMEDIATE, "Intermedia"),
        (AUDIENCE_LEVEL_EXPERIENCED, "Avanzada"),
    ]

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text="Al enviar tu propuesta, le estás dando permiso a los organizadores de la conferencia para grabar, editar y transmitir audio y/o video de tu presentación. Si no estas de acuerdo con esto, no chequees este recuadro."
    )

    class Meta:
        abstract = True


class TalkProposal(Proposal):

    class Meta:
        verbose_name = "Propuesta de charla/taller"
        verbose_name_plural = "Propuestas de charlas/talleres"

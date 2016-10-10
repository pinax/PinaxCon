# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

from .models import Attendee


class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee
        fields = [
            "full_name",
            "annotation",
            "show_to_sponsor",
            "cv",
        ]

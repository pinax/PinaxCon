# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
# our new form
class BecasForm(forms.Form):
    nombre_completo = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    que_necesitas = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="¿Qué necesitás?"
    )
    ingresa_el_texto = CaptchaField()

# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template import loader
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages

from .forms import BecasForm

def becas(request):
    form_class = BecasForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'nombre_completo')
            contact_email = request.POST.get(
                'email')
            form_content = request.POST.get('que_necesitas')

            # Email the profile with the
            # contact information
            template = loader.get_template('becas_email.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "[BECAS]Nueva beca requerida",
                content,
                "no-reply@python.org.ar",
                ['pyconar@listas.bitson.com.ar'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.add_message(request, messages.INFO, u"""¡Gracias por tu solicitud!, nos pondremos en contacto a la brevedad para
 informarte de los pasos a seguir""")

            return redirect('becas')
        else:
            messages.add_message(request, messages.ERROR, u"""Por favor completa los campos correctamente""")

    return render(request, 'becas.html', {
        'form': form_class,
    })


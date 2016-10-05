# -*- coding: utf-8 -*-
from account.decorators import login_required
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

@login_required
def attendee_create(request):
    try:
        return redirect(request.user.attendee)
    except ObjectDoesNotExist:
        pass

    if request.method == "POST":
        try:
            attendee = Attendee.objects.get(invite_email=request.user.email)
            found = True
        except Attendee.DoesNotExist:
            attendee = None
            found = False
        form = AttendeeForm(request.POST, request.FILES, instance=attendee)

        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.user = request.user
            if not found:
                attendee.invite_email = None
            attendee.save()
            messages.success(request, u"¡Te registraste exitosamente a la pyconAR te esperamos!.")
            return redirect("dashboard")
    else:
        form = AttendeeForm(initial={"name": request.user.get_full_name()})
    return render(request, "attendee/attendee_create.html", {
        "attendee_form": form,
    })


@login_required
def attendee_edit(request, pk=None):
    if pk is None:
        try:
            attendee = request.user.attendee
        except Attendee.DoesNotExist:
            return redirect("attendee_create")
    else:
        if request.user.is_staff:
            attendee = get_object_or_404(Attendee, pk=pk)
        else:
            raise Http404()

    if request.method == "POST":
        form = AttendeeForm(request.POST, request.FILES, instance=attendee)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil de asistente actualizado")
            return redirect("dashboard")
    else:
        form = AttendeeForm(instance=attendee)

    return render(request, "attendee/attendee_edit.html", {
        "attendee_form": form,
    })

# -*- coding: utf-8 -*-
from account.decorators import login_required
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template import Context

from .forms import AttendeeForm
from .models import Attendee

@login_required
def attendee_create(request):
    user = request.user

    attendee = getattr(request.user, "attendee", None)

    if attendee is not None:
        messages.error(request, u"Ya te encontrás registrado para la PyconAR.")
        return redirect("dashboard")

    if request.method == "POST":
        form = AttendeeForm(request.POST, request.FILES)

        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.user = user
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

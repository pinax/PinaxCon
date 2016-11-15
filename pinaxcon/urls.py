from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views
from pinaxcon import views
from pinaxcon.attendees import views as attendee_views

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^agenda/$", TemplateView.as_view(template_name="agenda.html"), name="agenda"),
    url(r"^becas/$", views.becas, name="becas"),
    url(r"^schedule.json$", views.schedule_json, name="schedule_json"),
    url(r"^diversidad/$", TemplateView.as_view(template_name="declaracion_diversidad.html"), name="diversidad"),
    url(r"^codigo-conducta/$", TemplateView.as_view(template_name="codigo_conducta.html"), name="codigo-de-conducta"),
    url(r"^forma-parte/$", TemplateView.as_view(template_name="forma_parte.html"), name="forma-parte"),
    url(r"^alojamiento/$", TemplateView.as_view(template_name="alojamiento.html"), name="alojamiento"),
    url(r"^organizadores/$", TemplateView.as_view(template_name="organizadores.html"), name="organizadores"),
    url(r"^sponsors/$", TemplateView.as_view(template_name="sponsors.html"), name="sponsors"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^attendee/", include("pinaxcon.attendees.urls")),
    url(r"^teams/", include("symposion.teams.urls")),

    url(r"^boxes/", include("pinax.boxes.urls")),
    url(r'^captcha/', include('captcha.urls')),
    url(r"^", include("pinax.pages.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

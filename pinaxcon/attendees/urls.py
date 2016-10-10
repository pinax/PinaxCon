from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


from . import views

urlpatterns = [
    url(r"^create/$", views.attendee_create, name="attendee_create"),
    url(r"^edit/(?:(?P<pk>\d+)/)?$", views.attendee_edit, name="attendee_edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from .models import Role, Volunteer, Pet, Event, EventRegistration, Donation

# Register your models here.
admin.site.register(Role)
admin.site.register(Volunteer)
admin.site.register(Pet)
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(Donation)

from django.contrib import admin
from app1.models import Movie,Ticket
# Register your models here.
class Movieadmin(admin.ModelAdmin):
    pass
class Ticketadmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, Movieadmin)
admin.site.register(Ticket, Ticketadmin)

from django.contrib import admin
from .models import Connection, Job, Todo, Status, Interaction

# Register your models here.
admin.site.register(Connection)
admin.site.register(Job)
admin.site.register(Todo)
admin.site.register(Status)
admin.site.register(Interaction)

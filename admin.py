from django.contrib import admin

# Register your models here.
from .models import Todo,AssignedTask


admin.site.register(Todo)
admin.site.register(AssignedTask)
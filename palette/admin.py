from django.contrib import admin
from .models import Drawing

# Register your models here.
class DrawingAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Drawing, DrawingAdmin)
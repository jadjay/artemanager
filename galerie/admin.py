from django.utils.translation import gettext_lazy as _

from django.contrib import admin

# Register your models here.

from .models import pictures


class picturesAdmin(admin.ModelAdmin):
    list_display = ('reference','name','sold')

admin.site.register(pictures,picturesAdmin)

#admin.site.register(Consumption)


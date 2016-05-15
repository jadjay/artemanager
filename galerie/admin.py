from django.utils.translation import gettext_lazy as _

from django.contrib import admin

# Register your models here.

from .models import pictures,themes


class picturesAdmin(admin.ModelAdmin):
    list_display = ('reference','name','sold','theme')

admin.site.register(pictures,picturesAdmin)

class themesAdmin(admin.ModelAdmin):
    list_display = ('name','parent')

admin.site.register(themes,themesAdmin)
#admin.site.register(Consumption)


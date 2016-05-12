from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class pictures(models.Model):
    reference = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    fichier = models.ImageField(upload_to='fichiers/')
    sold = models.BooleanField(default="False")
    price = models.DecimalField(default="0.00", max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(categories, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Photographie')
        verbose_name_plural = _('Photographies')

class categories(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

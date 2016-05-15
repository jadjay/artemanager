from django.utils.translation import gettext_lazy as _

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import pictures, themes
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.

def test(request):
    return render_to_response('test.html', context_instance=context)

def default(request):
    picturesList = pictures.objects.all
    themesList = themes.objects.all
    for theme in themesList:
        if not theme.parent:

    context = { 
                'picturesList': picturesList,
                'themesList': themesList,
                'language': request.LANGUAGE_CODE,
                'flag': "galerie/flag/%s.png" % request.LANGUAGE_CODE,
            }
    return render(request, 'default.html', context)

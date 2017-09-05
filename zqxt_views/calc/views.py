from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    return render(request, 'home.html')


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

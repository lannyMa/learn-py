from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    # return HttpResponseRedirect("/home")
    # return HttpResponseRedirect("https://www.baidu.com/")
    return redirect(reverse('home', args=[]))

def home(request):
    return HttpResponse("home page")
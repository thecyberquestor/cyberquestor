from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def intro(request):
    #return HttpResponse("Hi, this is CyberQuestor. Here you will find interesting topics")
    #return HttpResponse(template.render(context, request))
    return render(request, "index.html")
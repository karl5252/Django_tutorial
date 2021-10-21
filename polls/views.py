from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("uh oh you saw me")

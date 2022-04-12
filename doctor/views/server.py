from django.shortcuts import render
import json

def server(request):
    data = "hello,world"
    return render(request, "server.html", locals())
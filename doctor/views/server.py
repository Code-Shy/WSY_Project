from django.shortcuts import render


def server(request):
    data = "hello,world"
    return render(request, "server.html", locals())
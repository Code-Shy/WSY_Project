from django.http import JsonResponse
from doctor.models.customer import Customer


def getinfo_web(request):
    user = Customer.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'password': user.password,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
    })


def getinfo_app(request):
    user = Customer.objects.all()[0]
    return JsonResponse({
        'result':"success",
        'username':user.username,
        'email':user.email,
        'phone':user.phone,
    })


def getinfo(request):
    platform = request.GET.get('platform')

    if platform == "app":
        return getinfo_app(request)
    else:
        return getinfo_web(request)
from django.http import JsonResponse
from doctor.models.customer import Customer

def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    email = data.get("email", "").strip()

    if Customer.objects.filter(username=username).exists():
        return JsonResponse({
            'result':'用户名已存在'
        })

    Customer.objects.create(username=username, password=password, name="未实名", email=email, phone="0")

    return JsonResponse({
        'result':"success",
    })


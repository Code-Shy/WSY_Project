from django.urls import path,include
from doctor.views.index import index
from doctor.views.server import server
from doctor.views.login import login
from doctor.views.user import user
from doctor.views.getinfo import getinfo

urlpatterns = [
    path('', index, name="index"),
    path('server/', server, name="server"),
    path('login/', login, name="login"),
    path('user/', user, name='user'),
    path('getinfo/', getinfo, name="getinfo"),
]
from django.urls import path
from . import views

app_name = 'account_app'

urlpatterns = [

    path('singin' , views.SingIn , name='singin'),
    path('singup' , views.SingUp , name='singup'),
    path('logout' , views.Logout , name='logout'),
    path('edit' , views.Edit , name='edit'),
]
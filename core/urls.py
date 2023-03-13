from django.urls import path
from .views import home, products, exit, citas, login

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path('citas/', citas, name='citas'),
    path('login/', login, name='login'),
]
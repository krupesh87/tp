from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from . import views
from .views import *

# from django.contrib import views
from .views import LoginUser, Signup, index
from django.conf.urls.static import static

urlpatterns = [


    path('', index, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('orders', order_customer.as_view()),
    path('donate', Donate),
    path('myaccount', myaccount),
    path('changepassword', user_change_pass, name='changepass'),
    path('certificate', certi),
    path('blogs', blog),
    path('logout', LogoutUser),
    path('ser', services),
    path('cart', cart.as_view(), name='cart'),
    path('payment', payment, name='payment'),
    path('check-out', Checkout),
    path('search', search, name='search'),
    path('plants', plants.as_view(), name='products'),
    path('login/', LoginUser, name='login'),
    path('signup', Signup, name='signup'),
    # email
    path(r'^account_activation_sent/$', account_activation_sent,
         name='account_activation_sent'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         activate, name='activate'),
    path(r'^account_activation_sent/$', account_activation_sent,
         name='account_activation_sent'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         activate, name='activate'),
]

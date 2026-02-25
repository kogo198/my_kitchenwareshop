from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products/', views.products, name='products'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hostels/', views.hostels, name='hostels'),
    path('add-hostel/', views.add_hostel, name='add_hostel'),
    path('payment/', views.payment, name='payment'),
    path('api/hostels/', views.api_hostels, name='api_hostels'),
]

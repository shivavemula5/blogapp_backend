from django.urls import path 
from payments import views

urlpatterns = [
    path('create-checkout-session/',views.StripeCheckoutView.as_view(),name='checkout')    
]

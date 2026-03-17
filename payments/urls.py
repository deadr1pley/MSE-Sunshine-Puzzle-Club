from django.urls import path
from .views import premium_page, create_checkout_session, payment_success

urlpatterns = [
    path('premium/', premium_page, name='premium_page'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('success/', payment_success, name='payment_success'),
]
from django.urls import path
from .views import premium_page, create_checkout_session

urlpatterns = [
    path('premium/', premium_page, name='premium_page'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
]
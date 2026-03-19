import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.models import UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def premium_page(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'payments/premium.html', {
        'profile': profile,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })


@login_required
def create_checkout_session(request):
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment_success'))
        cancel_url = request.build_absolute_uri(reverse('premium_page'))

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'sek',
                        'product_data': {
                            'name': 'Premium Membership',
                        },
                        'unit_amount': 5000,
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return redirect(checkout_session.url, code=303)

    return redirect('premium_page')


@login_required
def payment_success(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile.is_premium = True
    profile.save()

    return render(request, 'payments/success.html')
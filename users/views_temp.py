
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from random import randint
from .utils import sendmail

# example
# def index(request):
#     return render(request, "users/index.html")

# Create your views here.

def about_us(request):
    return render(request, "users/about-us.html")

def add_service(request):
    return render(request, "users/add-service.html")

def all_services(request):
    return render(request, "users/all-services.html")

def book_service(request):
    return render(request, "users/book-service.html")

def categories(request):
    return render(request, "users/categories.html")

def chat(request):
    return render(request, "users/chat.html")

def contact_us(request):
    return render(request, "users/contact-us.html")

def edit_service(request):
    return render(request, "users/edit-service.html")

def faq(request):
    return render(request, "users/faq.html")

def index_2(request):
    return render(request, "users/index-2.html")

def index(request):
    return render(request, "users/index.html")

def my_services_inactive(request):
    return render(request, "users/my-services-inactive.html")

def my_services(request):
    return render(request, "users/my-services.html")

def notifications(request):
    return render(request, "users/notifications.html")

def privacy_policy(request):
    return render(request, "users/privacy-policy.html")

def provider_availability(request):
    return render(request, "users/provider-availability.html")

def provider_bookings(request):
    return render(request, "users/provider-bookings.html")

def provider_dashboard(request):
    return render(request, "users/provider-dashboard.html")

def provider_payment(request):
    return render(request, "users/provider-payment.html")

def provider_reviews(request):
    return render(request, "users/provider-reviews.html")

def provider_settings(request):
    return render(request, "users/provider-settings.html")

def provider_subscription(request):
    return render(request, "users/provider-subscription.html")

def provider_wallet(request):
    return render(request, "users/provider-wallet.html")

def search(request):
    return render(request, "users/search.html")

def service_details(request):
    return render(request, "users/service-details.html")

def term_condition(request):
    return render(request, "users/term-condition.html")

def user_bookings(request):
    return render(request, "users/user-bookings.html")

def user_chat(request):
    return render(request, "users/user-chat.html")

def user_dashboard(request):
    return render(request, "users/user-dashboard.html")

def user_payment(request):
    return render(request, "users/user-payment.html")

def user_reviews(request):
    return render(request, "users/user-reviews.html")

def user_settings(request):
    return render(request, "users/user-settings.html")

def user_wallet(request):
    return render(request, "users/user-wallet.html")


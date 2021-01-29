
from django.contrib import admin
from django.urls import path
from . import views

# example path('login-page', views.login_page, name='login-page')

urlpatterns = [
    path('about-us', views.about_us, name='about-us'),
	path('add-service', views.add_service, name='add-service'),
	path('all-services', views.all_services, name='all-services'),
	path('book-service', views.book_service, name='book-service'),
	path('categories', views.categories, name='categories'),
	path('chat', views.chat, name='chat'),
	path('contact-us', views.contact_us, name='contact-us'),
	path('edit-service', views.edit_service, name='edit-service'),
	path('faq', views.faq, name='faq'),
	path('index-2', views.index_2, name='index-2'),
	path('index', views.index, name='index'),
	path('my-services-inactive', views.my_services_inactive, name='my-services-inactive'),
	path('my-services', views.my_services, name='my-services'),
	path('notifications', views.notifications, name='notifications'),
	path('privacy-policy', views.privacy_policy, name='privacy-policy'),
	path('provider-availability', views.provider_availability, name='provider-availability'),
	path('provider-bookings', views.provider_bookings, name='provider-bookings'),
	path('provider-dashboard', views.provider_dashboard, name='provider-dashboard'),
	path('provider-payment', views.provider_payment, name='provider-payment'),
	path('provider-reviews', views.provider_reviews, name='provider-reviews'),
	path('provider-settings', views.provider_settings, name='provider-settings'),
	path('provider-subscription', views.provider_subscription, name='provider-subscription'),
	path('provider-wallet', views.provider_wallet, name='provider-wallet'),
	path('search', views.search, name='search'),
	path('service-details', views.service_details, name='service-details'),
	path('term-condition', views.term_condition, name='term-condition'),
	path('user-bookings', views.user_bookings, name='user-bookings'),
	path('user-chat', views.user_chat, name='user-chat'),
	path('user-dashboard', views.user_dashboard, name='user-dashboard'),
	path('user-payment', views.user_payment, name='user-payment'),
	path('user-reviews', views.user_reviews, name='user-reviews'),
	path('user-settings', views.user_settings, name='user-settings'),
	path('user-wallet', views.user_wallet, name='user-wallet')
]

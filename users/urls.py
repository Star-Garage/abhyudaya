"""sarkaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))a
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
# Accounts:
	path('user-reg', views.user_reg, name='user-reg'),
	path('registration', views.registration, name='registration'),
	path('login', views.login, name='login'),
	path('login-evaluate', views.login_evaluate, name='login-evaluate'),
	path('log-out', views.log_out, name='log-out'),
# General:
	path('index', views.index, name='index'),
	path('categories', views.categories, name='categories'),
    path('about-us', views.about_us, name='about-us'),
# Categories:
	path('s-computers', views.s_computers, name='s-computers'),
	path('s-appliances', views.s_appliances, name='s-appliances'),
	path('s-moverspackers', views.s_moverspackers, name='s-moverspackers'),
	path('s-design', views.s_design, name='s-design'),
	path('s-development', views.s_development, name='s-development'),
	path('s-projects', views.s_projects, name='s-projects'),
	path('s-educationals', views.s_educationals, name='s-educationals'),
	path('s-tradesmen', views.s_tradesmen, name='s-tradesmen'),
	path('s-cleaning', views.s_cleaning, name='s-cleaning'),
	path('s-saloon', views.s_saloon, name='s-saloon'),
	path('s-artists', views.s_artists, name='s-artists'),
	path('s-constructions', views.s_constructions, name='s-constructions'),
	path('s-immigration', views.s_immigration, name='s-immigration'),
# Sub-categories:
	#Appliances:
	path('app-ac', views.app_ac, name='app-ac'),
	path('app-geyser', views.app_geyser, name='app-geyser'),
	path('app-refrigerator', views.app_refrigerator, name='app-refrigerator'),
	path('app-ro', views.app_ro, name='app-ro'),
	path('app-tv', views.app_tv, name='app-tv'),
	path('app-washingmachine', views.app_washingmachine, name='app-washingmachine'),
	#Artists:
	path('content-writers', views.content_writers, name='content-writers'),
	path('make-up', views.make_up, name='make-up'),
	path('mehendi', views.mehendi, name='mehendi'),
	path('painters', views.painters, name='painters'),
	path('photographers', views.photographers, name='photographers'),
	path('sketch', views.sketch, name='sketch'),
	#Computers:
	path('assessories', views.assessories, name='assessories'),
	path('repairs-upgrades', views.repairs_upgrades, name='repairs-upgrades'),
	path('recovery-protection', views.recovery_protection, name='recovery-protection'),
	path('support-maintenance', views.support_maintenance, name='support-maintenance'),
	#Construction:
	path('crack-repair', views.crack_repair, name='crack-repair'),
	path('flooring', views.flooring, name='flooring'),
	path('interior-design', views.interior_design, name='interior-design'),
	path('light-fitting', views.light_fitting, name='light-fitting'),
	path('paint', views.paint, name='paint'),
	path('planning-organizing', views.planning_organizing, name='planning-organizing'),
	path('plaster', views.plaster, name='plaster'),
	path('plumbing', views.plumbing, name='plumbing'),
	path('rcc', views.rcc, name='rcc'),
	path('reborn-rennovation', views.reborn_rennovation, name='reborn-rennovation'),
	path('water-proofing', views.water_proofing, name='water-proofing'),
	#Design:
	path('logo', views.logo, name='logo'),
	path('flyer-banner', views.flyer_banner, name='flyer-banner'),
	path('poster', views.poster, name='poster'),
	path('brochure', views.brochure, name='brochure'),
	path('leaflet-pamphlet', views.leaflet_pamphlet, name='leaflet-pamphlet'),
	path('visiting-card', views.visiting_card, name='visiting-card'),
	path('invitation-card', views.invitation_card, name='invitation-card'),
	path('stationary', views.stationary, name='stationary'),
	path('packaging', views.packaging, name='packaging'),
	path('social-posts', views.social_posts, name='social-posts'),
	path('webs', views.webs, name='webs'),
	path('apps', views.apps, name='apps'),
	#Development:
	path('app-dev', views.app_dev, name='app-dev'),
	path('electrical-computer', views.electrical_computer, name='electrical-computer'),
	path('iot-electronic', views.iot_electronic, name='iot-electronic'),
	path('mechanical', views.mechanical, name='mechanical'),
	path('pcbdesign-dev', views.pcbdesign_dev, name='pcbdesign-dev'),
	path('web-dev', views.web_dev, name='web-dev'),
	#Education:
	path('career-consult', views.career_consult, name='career-consult'),
	path('ebooks-notes', views.ebooks_notes, name='ebooks-notes'),
	path('ppt', views.ppt, name='ppt'),
	path('report-thesis', views.report_thesis, name='report-thesis'),
	path('resume', views.resume, name='resume'),
	path('st-projects', views.st_projects, name='st-projects'),
	#Immigrations:
	path('bookings', views.bookings, name='bookings'),
	path('coaching', views.coaching, name='coaching'),
	path('passport', views.passport, name='passport'),
	path('spouse-visa', views.spouse_visa, name='spouse-visa'),
	path('st-abroad', views.st_abroad, name='st-abroad'),
	path('visitor', views.visitor, name='visitor'),
	#Tradesmen:
	path('carpenters', views.carpenters, name='carpenters'),
	path('electricians', views.electricians, name='electricians'),
	path('plumbers', views.plumbers, name='plumbers'),

# Provider-home:
	path('my-services-inactive', views.my_services_inactive, name='my-services-inactive'),
	path('my-services', views.my_services, name='my-services'),
	path('provider-availability', views.provider_availability, name='provider-availability'),
	path('provider-bookings', views.provider_bookings, name='provider-bookings'),
	path('provider-dashboard', views.provider_dashboard, name='provider-dashboard'),
	path('provider-payment', views.provider_payment, name='provider-payment'),
	path('provider-reviews', views.provider_reviews, name='provider-reviews'),
	path('provider-settings', views.provider_settings, name='provider-settings'),
	path('provider-subscription', views.provider_subscription, name='provider-subscription'),
	path('provider-wallet', views.provider_wallet, name='provider-wallet'),
	path('edit-service', views.edit_service, name='edit-service'),
# Customer-home:
	path('customer-bookings', views.customer_bookings, name='customer-bookings'),
	path('customer-chat', views.customer_chat, name='customer-chat'),
	path('customer-dashboard', views.customer_dashboard, name='customer-dashboard'),
	path('customer-payment', views.customer_payment, name='customer-payment'),
	path('customer-reviews', views.customer_reviews, name='customer-reviews'),
	path('customer-settings', views.customer_settings, name='customer-settings'),
	path('customer-wallet', views.customer_wallet, name='customer-wallet'),
# General:
	path('contact-us', views.contact_us, name='contact-us'),
	path('faq', views.faq, name='faq'),
	path('privacy-policy', views.privacy_policy, name='privacy-policy'),
	path('term-condition', views.term_condition, name='term-condition'),
	path('search', views.search, name='search'),
# Others
	path('add-service', views.add_service, name='add-service'),
	path('all-services', views.all_services, name='all-services'),
	path('book-service', views.book_service, name='book-service'),
	path('chat', views.chat, name='chat'),
	path('notifications', views.notifications, name='notifications'),
	path('splus', views.splus, name='splus'),
# Update:
	path('update-profile', views.update_profile, name='update-profile'),
	path('ex', views.ex, name='ex'),
]

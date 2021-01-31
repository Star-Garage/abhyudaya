
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
from random import randint
from .utils import send_mail

###########################################################################################################################################################
# <<< Accounts
def user_reg(request):
    return render(request, "users/account/user-reg.html")

def registration(request):
    role=request.POST['role']
    email=request.POST['email']
    username=request.POST['username']
    password=request.POST['password']
    repassword=request.POST['password']
    uid=User.objects.create(email=email, password=password, role=role, username=username)
    if role=="Provider" and password==repassword:
        pid=Provider.objects.create(user_id=uid)
        send_mail("Confirmation mail", "Welcome to My World", "the.meetpatell@gmail.com",[email])
        s_msg="Successfully Registered"
        return render(request, "users/account/login.html", {'s_msg': s_msg})
    elif role=="Customer" and password==repassword:
        cid=Customer.objects.create(user_id=uid)
        send_mail("Confirmation mail", "Welcome to My World", "the.meetpatell@gmail.com",[email])
        s_msg="Successfully Registered"
        return render(request, "users/account/login.html", {'s_msg': s_msg})
    else:
        f_msg="Registration Failed"
        return render(request, "users/account/register.html", {'f_msg': f_msg})

def login(request):
    return render(request, "users/account/login.html")

def login_evaluate(request):
    role=request.POST['role']
    email=request.POST['email']
    password=request.POST['password']
    uid=User.objects.get(email=email)
    if uid:
        if role=="Provider":
            if uid.password==password:
                pid=Provider.objects.get(user_id=uid)
                print("------> ", uid.email)
                request.session['username']=uid.username
                request.session['id']=pid.id
                request.session['email']=uid.email
                request.session['role']=uid.role
                context={
                    'uid':uid,
                    'pid':pid,
                }
                return render(request, "users/index.html", {'context':context})
            else:
                f_msg="Registration Failed"
                return render(request, "users/account/login.html", {'f_msg': f_msg})

        elif role=="Customer":
            if uid.password==password:
                cid=Customer.objects.get(user_id=uid)
                print("------> ", uid.email)
                request.session['username']=uid.username
                request.session['id']=cid.id
                request.session['email']=uid.email
                request.session['role']=uid.role
                context={
                    'uid':uid,
                    'cid':cid,
                }
                return render(request, "users/index.html", {'context':context})
            else:
                f_msg="Registration Failed"
                return render(request, "account/login.html", {'f_msg': f_msg})

        else:
            return render(request, "account/login.html")
    else:
        return render(request, "users/account/user-reg.html")

def log_out(request):
    if "email" in request.session:
        del request.session['username']
        del request.session['email']
        del request.session['id']
        return render(request, "users/account/login.html")
    else:
        return render(request, "users/account/login.html")
# Accounts >>>
###########################################################################################################################################################

# <<< General
def index(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/index.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/index.html", {'context': context})
        else:
            return render(request, "users/index.html")
    else:
        return render(request, "users/index.html")

def categories(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/categories.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/categories.html", {'context': context})
        else:
            return render(request, "users/categories.html")
    else:
        return render(request, "users/categories.html")

def about_us(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/about-us.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/about-us.html", {'context': context})
        else:
            return render(request, "users/about-us.html")
    else:
        return render(request, "users/about-us.html")
# General >>>

###########################################################################################################################################################

# <<< Categories
def s_appliances(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-appliances.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-appliances.html", {'context': context})
        else:
            return render(request, "users/services/s-appliances.html")
    else:
        return render(request, "users/services/s-appliances.html")

def s_artists(request): 
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-artists.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-artists.html", {'context': context})
        else:
            return render(request, "users/services/s-artists.html")
    else:
        return render(request, "users/services/s-artists.html")

def s_computers(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-computers.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-computers.html", {'context': context})
        else:
            return render(request, "users/services/s-computers.html")
    else:
        return render(request, "users/services/s-computers.html")

def s_constructions(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-constructions.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-constructions.html", {'context': context})
        else:
            return render(request, "users/services/s-constructions.html")
    else:
        return render(request, "users/services/s-constructions.html")

def s_design(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-design.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-design.html", {'context': context})
        else:
            return render(request, "users/services/s-design.html")
    else:
        return render(request, "users/services/s-design.html")

def s_development(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-development.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-development.html", {'context': context})
        else:
            return render(request, "users/services/s-development.html")
    else:
        return render(request, "users/services/s-development.html")

def s_educationals(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-educationals.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-educationals.html", {'context': context})
        else:
            return render(request, "users/services/s-educationals.html")
    else:
        return render(request, "users/services/s-educationals.html")

def s_immigration(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-immigration.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-immigration.html", {'context': context})
        else:
            return render(request, "users/services/s-immigration.html")
    else:
        return render(request, "users/services/s-immigration.html")

def s_projects(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-projects.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-projects.html", {'context': context})
        else:
            return render(request, "users/services/s-projects.html")
    else:
        return render(request, "users/services/s-projects.html")

def s_tradesmen(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/services/s-tradesmen.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/services/s-tradesmen.html", {'context': context})
        else:
            return render(request, "users/services/s-tradesmen.html")
    else:
        return render(request, "users/services/s-tradesmen.html")

def s_cleaning(request):
    return render(request, "users/services/s-cleaning.html")

def s_moverspackers(request):
    return render(request, "users/services/s-moverspackers.html")

def s_saloon(request):
    return render(request, "users/services/s-saloon.html")
# Categories >>>

###########################################################################################################################################################

# <<< sub-categories

#    #Appliances:
def app_ac(request):
    return render(request, "users/servicepage/appliances/app-ac.html")

def app_geyser(request):
    return render(request, "users/servicepage/appliances/app-geyser.html")

def app_refrigerator(request):
    return render(request, "users/servicepage/appliances/app-refrigerator.html")

def app_ro(request):
    return render(request, "users/servicepage/appliances/app-ro.html")

def app_tv(request):
    return render(request, "users/servicepage/appliances/app-tv.html")

def app_washingmachine(request):
    return render(request, "users/servicepage/appliances/app-washingmachine.html")

#    #Artists:
def content_writers(request):
    return render(request, "users/servicepage/artists/content-writers.html")

def make_up(request):
    return render(request, "users/servicepage/artists/make-up.html")

def mehendi(request):
    return render(request, "users/servicepage/artists/mehendi.html")

def painters(request):
    return render(request, "users/servicepage/artists/painters.html")

def photographers(request):
    return render(request, "users/servicepage/artists/photographers.html")

def sketch(request):
    return render(request, "users/servicepage/artists/sketch.html")
    
#    #Computers:
def assessories(request):
    return render(request, "users/servicepage/computer/assessories.html")

def recovery_protection(request):
    return render(request, "users/servicepage/computer/recovery-protection.html")

def repairs_upgrades(request):
    return render(request, "users/servicepage/computer/repairs-upgrades.html")

def support_maintenance(request):
    return render(request, "users/servicepage/computer/support-maintenance.html")

#    #Constructions:
def crack_repair(request):
    return render(request, "users/servicepage/construction/crack-repair.html")

def flooring(request):
    return render(request, "users/servicepage/construction/flooring.html")

def interior_design(request):
    return render(request, "users/servicepage/construction/interior-design.html")

def light_fitting(request):
    return render(request, "users/servicepage/construction/light-fitting.html")

def paint(request):
    return render(request, "users/servicepage/construction/paint.html")

def planning_organizing(request):
    return render(request, "users/servicepage/construction/planning-organizing.html")

def plaster(request):
    return render(request, "users/servicepage/construction/plaster.html")

def rcc(request):
    return render(request, "users/servicepage/construction/rcc.html")

def reborn_rennovation(request):
    return render(request, "users/servicepage/construction/reborn-rennovation.html")

def water_proofing(request):
    return render(request, "users/servicepage/construction/water-proofing.html")

def plumbing(request):
    return render(request, "users/servicepage/construction/plumbing.html")

#    #Design:
def logo(request):
    return render(request, "users/servicepage/design/logo.html")

def flyer_banner(request):
    return render(request, "users/servicepage/design/flyer-banner.html")

def brochure(request):
    return render(request, "users/servicepage/design/brochure.html")

def leaflet_pamphlet(request):
    return render(request, "users/servicepage/design/leaflet-pamphlet.html")

def poster(request):
    return render(request, "users/servicepage/design/poster.html")

def visiting_card(request):
    return render(request, "users/servicepage/design/visiting-card.html")

def invitation_card(request):
    return render(request, "users/servicepage/design/invitation-card.html")

def stationary(request):
    return render(request, "users/servicepage/design/stationary.html")

def packaging(request):
    return render(request, "users/servicepage/design/packaging.html")

def social_posts(request):
    return render(request, "users/servicepage/design/social-posts.html")

def webs(request):
    return render(request, "users/servicepage/design/webs.html")

def apps(request):
    return render(request, "users/servicepage/design/apps.html")

#    #Development:
def app_dev(request):
    return render(request, "users/servicepage/development/app-dev.html")

def electrical_computer(request):
    return render(request, "users/servicepage/development/electrical-computer.html")

def iot_electronic(request):
    return render(request, "users/servicepage/development/iot-electronic.html")

def mechanical(request):
    return render(request, "users/servicepage/development/mechanical.html")

def pcbdesign_dev(request):
    return render(request, "users/servicepage/development/pcbdesign-dev.html")

def web_dev(request):
    return render(request, "users/servicepage/development/web-dev.html")
    #Educationals:

def career_consult(request):
    return render(request, "users/servicepage/educationals/career-consult.html")

def ebooks_notes(request):
    return render(request, "users/servicepage/educationals/ebooks-notes.html")

def ppt(request):
    return render(request, "users/servicepage/educationals/ppt.html")

def report_thesis(request):
    return render(request, "users/servicepage/educationals/report-thesis.html")

def resume(request):
    return render(request, "users/servicepage/educationals/resume.html")

def st_projects(request):
    return render(request, "users/servicepage/educationals/st-projects.html")
    
#    #Immigration
def bookings(request):
    return render(request, "users/servicepage/immigration/bookings.html")

def coaching(request):
    return render(request, "users/servicepage/immigration/coaching.html")

def passport(request):
    return render(request, "users/servicepage/immigration/passport.html")

def spouse_visa(request):
    return render(request, "users/servicepage/immigration/spouse-visa.html")

def st_abroad(request):
    return render(request, "users/servicepage/immigration/st-abroad.html")

def visitor(request):
    return render(request, "users/servicepage/immigration/visitor.html")
    
#    #Tradesmen:
def carpenters(request):
    return render(request, "users/servicepage/tradesmen/carpenters.html")

def electricians(request):
    return render(request, "users/servicepage/tradesmen/electricians.html")

def plumbers(request):
    return render(request, "users/servicepage/tradesmen/plumbers.html")

# sub-categories >>>

###########################################################################################################################################################

# <<< Provider-home
def my_services_inactive(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/my-services-inactive.html",{'context':context})

def my_services(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/my-services.html",{'context':context})

def provider_availability(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-availability.html",{'context':context})

def provider_bookings(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-bookings.html", {'context': context})

def provider_dashboard(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-dashboard.html", {'context': context})

def provider_payment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-payment.html",{'context':context})

def provider_reviews(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-reviews.html",{'context':context})

def provider_settings(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-settings.html",{'context':context})

def provider_subscription(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-subscription.html",{'context':context})

def provider_wallet(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Provider.objects.get(user_id=uid)
        context={
                    'pid':pid,
                    'uid':uid,
        }
        return render(request, "users/provider/provider-wallet.html",{'context':context})
# Provider-home >>>

###########################################################################################################################################################

# <<< Customer-home
def customer_bookings(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-bookings.html", {'context':context})

def customer_chat(request):
    return render(request, "users/customer/customer-chat.html")

def customer_dashboard(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-dashboard.html", {'context':context})

def customer_payment(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-payment.html", {'context':context})

def customer_reviews(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-reviews.html", {'context':context})

def customer_settings(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-settings.html", {'context':context})

def customer_wallet(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-wallet.html", {'context':context})
# Customer-home >>>

###########################################################################################################################################################

# <<< General
def contact_us(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/contact-us.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/contact-us.html", {'context': context})
        else:
            return render(request, "users/contact-us.html")
    else:
        return render(request, "users/contact-us.html")

def splus(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/splus.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/splus.html", {'context': context})
        else:
            return render(request, "users/splus.html")
    else:
        return render(request, "users/splus.html")

def privacy_policy(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/privacy-policy.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/privacy-policy.html", {'context': context})
        else:
            return render(request, "users/privacy-policy.html")
    else:
        return render(request, "users/privacy-policy.html")

def term_condition(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Provider":
            pid=Provider.objects.get(user_id=uid)
            context={
                'uid':uid,
                'pid':pid,
            }
            return render(request, "users/term-condition.html", {'context': context})
        elif uid.role=="Customer":
            cid=Customer.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request, "users/term-condition.html", {'context': context})
        else:
            return render(request, "users/term-condition.html")
    else:
        return render(request, "users/term-condition.html")
        
def search(request):
    return render(request, "users/search.html")
# General >>>

###########################################################################################################################################################

# <<< Others
def add_service(request):
    return render(request, "users/add-service.html")

def all_services(request):
    return render(request, "users/all-services.html")

def book_service(request):
    return render(request, "users/book-service.html")

def notifications(request):
    return render(request, "users/notifications.html")

def chat(request):
    return render(request, "users/chat.html")

def edit_service(request):
    return render(request, "users/edit-service.html")


# Others >>>

###########################################################################################################################################################

# <<< Update
def update_profile(request):
    email=request.session['email']
    if "email" in request.session:
        uid=User.objects.get(email=email)
        cid=Customer.objects.get(user_id=uid)
        cid.name=request.POST['name']
        cid.gender=request.POST['gender']
        cid.address=request.POST['address']
        cid.state=request.POST['state']
        cid.country=request.POST['country']
        cid.pincode=request.POST['pincode']
        cid.city=request.POST['city']
        cid.save(   )
        context={
                    'cid':cid,
                    'uid':uid,
        }
        return render(request, "users/customer/customer-settings.html", {'context':context})
    else:
        return render(request, "users/customer/customer-settings.html")
# Update >>>

def i_inquiry(request):
    i_fname=request.POST['i_fname']
    i_lname=request.POST['i_lname']
    i_email=request.POST['i_email']
    i_contact=request.POST['i_contact']
    i_msg=request.POST['i_msg']
    inq=iInquiry.objects.create(i_email=i_email, i_fname=i_fname, i_lname=i_lname, i_contact=i_contact, i_msg=i_msg )
    return render(request, "users/contact-us.html")

def ex(request):
    return render(request, "users/ex.html")


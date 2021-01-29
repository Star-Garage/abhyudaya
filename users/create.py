from glob import glob
 
url_template = """
from django.contrib import admin
from django.urls import path
from . import views

# example path('login-page', views.login_page, name='login-page')

urlpatterns = [
    {url_patterns}
]
"""

views_template = """
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from random import randint
from .utils import sendmail

# example
# def index(request):
#     return render(request, "users/index.html")

# Create your views here.
{functions}
"""

path_template = "path('{url}', views.{func}, name='{name}')"
func_template = """
def {func}(request):
    return render(request, "users/{url}.html")
"""

path = './templates/users/*.html'
files = glob(path)
files = [ file.split("\\")[-1].split(".")[0] for file in files ]

urls = []
funcs = []

for file in files:
    url = file
    func = file.replace("-","_")
    name = file

    urls.append(path_template.format(
        url=url,
        func=func,
        name=name
    ))

    funcs.append(func_template.format(
        func=func,
        url=url
    ))

with open("url_temp.py","w+") as file:
    content = url_template.format(
        url_patterns=",\n\t".join(urls)
    )
    file.write(content)

with open("views_temp.py","w+") as file:
    content = views_template.format(
        functions = "".join(funcs)
    )
    file.write(content)
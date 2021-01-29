import re

from glob import glob

#static_re=re.compile(r'(assets((/[a-zA-Z0-9-]+)*(/.[a-zA-Z0-9-]+)+)([a-z.A-Z0-9-])([a-z.A-Z0-9-])+)')
url_re=re.compile(r'(")([A-Za-z0-9-_]+)(.html)(")')
path="./templates/users/user/*.html"


paths=glob(path)

for file in paths:
    with open(file,"r", encoding="utf8") as filer:
        content = filer.read()
        #content = static_re.sub(r"{% static 'users/$1' %}",content)
        content = url_re.sub(r""" "{% url '\g<2>' %}" """, content)
    
    with open(file,"w+", encoding="utf8") as filew:
        filew.write(content)
[![Build Status](https://dev.azure.com/TeamBloom/Bloom-Learn/_apis/build/status/BethanyJep.BloomLearn?branchName=refs%2Fpull%2F18%2Fmerge)](https://dev.azure.com/TeamBloom/Bloom-Learn/_build/latest?definitionId=4&branchName=refs%2Fpull%2F18%2Fmerge)

## Installation

install virtual environment

```
python -m venv myvenv
```

Activate virtual environment

```
myenv\Scripts\activate
```

Upgrade pip
```
python -m pip install --upgrade pip
```

install requirements
```
pip install -r requirements.txt
```

new project in django
```'
django-admin.exe startproject <projectName>
```

creating db
```
python manage.py migrate
```

running the app (port 127.0.0.1:8000)
```
python manage.py runserver
#if it fails
python manage.py runserver 0:8000
```

create a new application
```
python manage.py startapp <appName>
```

# Django models

update model to database
```'
python manage.py makemigrations <modelName>
```

migration error?
```
python manage.py migrate --run-syncdb    
```

## Django Admin

registering models to django admin
```
from .models import <modelName>
admin.site.register(<modelName>)
```

create a super user to access the admin
```
python manage.py createsuperuser
```

## create a .gitignore file

## using gunicorn
```
pip install waitress
waitress-serve --listen=*:8000 <appName>.wsgi:application
```

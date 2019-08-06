## check for django version
python -m django --version

## Creating a project
django-admin startproject mysite

## start server
```
python manage.py runserver
# could add port after, default is 8000

# If you want to change the server’s IP, pass it along with the port. 
# For example, to listen on all available public IPs 
# (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:
python manage.py runserver 0:8000


Hot Reload ✅
But some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.
```

# Projects vs. apps
#### What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. 
#### A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

## create app
```
python manage.py startapp polls
```

## view in app
```
# in the polls/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# in polls/urls.py set url config
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]



# mysite/urls.py (include)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
#### The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

#### check for result
python manage.py runserver  
Go to http://localhost:8000/polls/ 

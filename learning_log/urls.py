"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin   # import the functions and modules 
from django.urls import include, path # that manages the URLs for the admin site. 

#  Include set of URL patterns from the apps in the project.
urlpatterns = [
    path('admin/', admin.site.urls), # includes the module admin site, defines all the URLs that can be requested from the admin site.
    path('', include('learning_logs.urls'), name= 'index'), # includes the URL patterns defined in the learning_logs app.
    
]

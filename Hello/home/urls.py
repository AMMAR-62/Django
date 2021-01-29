"""Hello URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views


admin.site.site_header = "LearningWeb Admin"
admin.site.site_title = "LearningWeb Admin Portal"
admin.site.index_title = "Welcome to LearningWeb"


urlpatterns = [
    path("", views.index, name="home"),
    path("django", views.django, name="django"),
    path("flask", views.flask, name="flask"),
    path("JS", views.JS, name="JS"),
    path("React_JS", views.reactJS, name="React JS"),
    path("Ang_JS", views.AngJS, name="Ang JS"),
    path("Next_JS", views.NextJS, name="Next JS"),
    path("Forms", views.Forms, name="Forms"),
]

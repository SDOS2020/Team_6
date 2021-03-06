"""base URL Configuration

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
from users.views import UserHandler, UserCompleteProfile,MentorCreation, MentorMatching
from project.views import ProjectHandler
from classes.views import ClassHandler, ClassById, PostHandler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/user/', UserHandler.as_view()),
    path('api/project/', ProjectHandler.as_view()),
    path('api/user/complete/', UserCompleteProfile.as_view()),
    path('api/mentor/apply/', MentorCreation.as_view()),
    path('api/mentor/matches/', MentorMatching.as_view()),
    # path('api/class/', Class.as_view()),
    path('api/class/', ClassHandler.as_view()),
    path('api/class/id/', ClassById.as_view()),
    path('api/class/post/', PostHandler.as_view()),
]

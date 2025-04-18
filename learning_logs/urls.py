"""
URL configuration for learnig_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, EntryViewSet, NoticiaViewSet

router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'noticias', NoticiaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='learning_logs/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('api/', include(router.urls)),
]

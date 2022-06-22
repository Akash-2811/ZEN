from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name="home"), 
    #name=home => give same name which is use in html file in {% url 'home' %} 
    path('/session', views.session, name="session"),
]
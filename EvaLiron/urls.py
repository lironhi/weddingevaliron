from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexfr, name='index'),
    path('fr', views.indexfr),
    #path('login', views.login, name='login'),
    #path('invitation', views.f_login),
    #path('added', views.f_addinvite),
    path('contactfr', views.contactfr),
    path('he', views.indexhe),
]
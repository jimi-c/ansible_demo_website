from django.conf.urls import url, include
from django.views.generic.base import TemplateView

from main import views as main_views

urlpatterns = [
    url(r'^login$',         main_views.login,         name='login'),
    url(r'^logout$',        main_views.logout,        name='logout'),
    url(r'^register_user$', main_views.register_user, name='register_user'),
    url(r'^private_page$',  main_views.private_page,  name='private_page'),
    url(r'^$',              main_views.index,         name='home'),
]

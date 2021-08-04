from django.contrib import admin
from django.urls import path, re_path
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    re_path(r'^lists/new$', views.new_list, name='new_list'),
    re_path(r'^lists/one-list-in-the-world/$',
            views.view_list, name='view_list'),
    path('admin/', admin.site.urls),
]

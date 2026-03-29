from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.welcome),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('logout/', views.user_logout),
    path('save/',views.add_marksheet),
    path('list/', views.marksheet_list),
    path('delete/<int:id>/',views.delete_marksheet),
    path('edit/<int:id>/',views.edit_marksheet),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    # path('set/', views.setCookies),
    # path('get/', views.getCookies),
]

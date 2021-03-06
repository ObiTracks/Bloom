from django.urls import path
from .views  import views_user, views_c_login

urlpatterns = [
    # BASE URLS
    path('', views_user.home_page, name='home'),
    path('profile', views_user.profilePage, name='profile'),

    # CRUD URLS
    path('create_reservation/<str:tk>/<str:pk>/', views_user.createReservation,name='create_reservation'),
    path('delete/<str:pk>/', views_user.deleteReservation, name='delete'),

    # LOGIN URLS
    path('register', views_c_login.registerPage, name='register'),
    path('login', views_c_login.loginPage, name='login'),
    path('logout', views_c_login.logoutUser, name='logout'),
    path('profile', views_c_login.profilePage, name='profile'),

    # LISTS URLS
    path('reservations', views_user.reservationsPage, name='reservations'),
   

]
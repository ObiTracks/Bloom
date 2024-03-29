"""BloomV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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



urlpatterns = [

    # CRUD views
    path('joinrequest-send/<int:place_pk>',  views.sendjoin_request , name="send-join-request"),
    path('joinrequest-approve/<str:joinrequest_pk>',  views.approvejoin_request , name="approve-join-request"),
    path('joinrequest-reject/<str:joinrequest_pk>',  views.rejectjoin_request, name="reject-join-request"),

]

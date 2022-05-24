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
import siteApp
from siteApp.views import *
import mgmtApp


urlpatterns = [
    path('', views.dashboard_view, name="member-dashboard"),
    path('community', views.community_view, name="member-community"),
    # path('amenity', views.amenity_view, name="member-amenity"),
    path('amenity/<str:pk>', views.amenity_view, name="member-amenity"),
    path('profile', siteApp.views.landingpage_view, name="member-profilepage"),

    # ENDPOINT VIEWS
    path('joinrequest-send/<str:place_pk>',  siteApp.views.sendjoin_request , name="send-join-request"),

    
]

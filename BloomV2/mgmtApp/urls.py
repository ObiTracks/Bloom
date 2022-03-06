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
from . import crud_views


urlpatterns = [
    path('dashboard', views.dashboard_view, name="dashboard"),
    path('amenities', views.amenities_view, name="amenities"),
    path('amenities/<str:pk>/', views.amenity_view, name="amenity"),
    # path('amenities/amenity', views.amenityobject_view, name="amenity"),

    # path('members', views.memberhub_view, name="memberhub"),
    # path('members/member', views.memberobject_view, name="member"),

    # CRUD views
    path('newamenity/<str:place_id>/', crud_views.new_amenity_view, name="new-amenity"),
    path('newplace', crud_views.new_place, name="new-place"),

]

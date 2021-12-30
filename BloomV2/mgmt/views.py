from django.shortcuts import render

# Create your views here.


def dashboard_view(request):
    page_title = "Main Dashboard"
    context = {'page_title': page_title}
    template_name = '../templates/pages/dashboard.html'
    return render(request, template_name, context)


def amenityhub_view(request):
    page_title = "Amenity Hub"
    context = {'page_title': page_title}
    template_name = '../templates/pages/amenityhub.html'
    return render(request, template_name, context)


def amenityobject_view(request):
    page_title = "Amenity Name"
    page_subtitle = "Amenities"
    context = {'page_title': page_title, 'page_subtitle': page_subtitle}
    template_name = '../templates/pages/amenityobject.html'
    return render(request, template_name, context)

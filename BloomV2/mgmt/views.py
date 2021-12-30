from django.shortcuts import render

# Create your views here.


def dashboard(request):
    page_title = "Main Dashboard"
    context = {'page_title': page_title}
    template_name = '../templates/pages/dashboard.html'
    return render(request, template_name, context)

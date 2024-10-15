from django.shortcuts import render

def render_autorization(request):
    return render(request = request, template_name = "autorization_app/autorization.html")

def render_registration(request):
    return render(request = request, template_name = "autorization_app/registration.html")


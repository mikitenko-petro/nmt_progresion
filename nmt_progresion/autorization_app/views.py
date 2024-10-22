from django.shortcuts import render
from .models import User 

def render_autorization(request):
    users = User.objects.all().values()
    return render(request = request, template_name = "autorization_app/autorization.html", context = {"users": users})

def render_user(request, id):
    user = User.objects.get(id = id)
    return render(request = request, template_name = "autorization_app/user.html", context = {"user": user})


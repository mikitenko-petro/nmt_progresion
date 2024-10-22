from django.urls import path
from autorization_app.views import render_autorization, render_user

urlpatterns = [
    path('autorization/', render_autorization),
    path('user/<slug:id>', render_user)

]
from django.contrib.auth import get_user_model
from django.shortcuts import render


def home(request):
    user = get_user_model()
    users = user.objects.all()
    context = {'users': users}
    return render(request, "home.html", context=context)

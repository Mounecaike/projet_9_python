from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé. Tu peux te connecter.")
            return redirect("accounts:login")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

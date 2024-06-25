from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def account_signin(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        context = {}

        signin_form = AuthenticationForm(request, data=request.POST)
        if request.method == "POST":
            try:
                if signin_form.is_valid():
                    username = signin_form.cleaned_data.get("username")
                    password = signin_form.cleaned_data.get("password")
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, f"Welcome back, {user}")
                        return redirect("index")
            except ValidationError as e:
                messages.error(request, f"Error: {' '.join(e.messages)}")

        context.update({
            "signin_form": signin_form,
            "title_tag": "Secure Login",
            "meta_description": "Log in to your Sibia account to access personalized healthcare solutions, AI-driven insights, and SDG research for improving community health.",
            "meta_keywords": "Sibia, login, secure access, healthcare account, medical AI, personalized healthcare, community health, SDG research",
        })
        return render(request, "account_signin.html", context)


@login_required
def account_signout(request):
    print(f"{request.user} logged out!")
    logout(request)
    return redirect("account_signin")

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import RegistrationForm
from .models import RegisteredUser


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@permission_classes((AllowAny,))
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the provided credentials match the specific user
        if username != 'usertask' or password != 'usertasktask':
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

        # If the credentials are valid, create a token for the user
        user = authenticate(username=username, password=password)
        if not user:
            return render(request, 'login.html', {'error': 'Authentication failed'})

        # Get or create a token for the user
        token, _ = Token.objects.get_or_create(user=user)

        # Redirect to the 'register/' page upon successful login
        return redirect('/dashboard/')

    # If it's not a POST request, render the empty login form
    return render(request, 'login.html')


def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    
    # If user is not logged in, render the template with the button
    return render(request, 'logout.html', {'show_button': True})


@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form is valid. Data saved.")
            # Create a new instance of the form after successful registration
            form = RegistrationForm()
            return redirect('/dashboard')
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


@permission_classes((AllowAny,))
def dashboard_view(request):
    registered_users = RegisteredUser.objects.all()
    return render(request, 'dashboard.html', {'registered_users': registered_users})
# this will solve your isseue

@permission_classes((AllowAny,))
def edit_user(request, user_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegistrationForm(instance=user)

    return render(request, 'edit.html', {'form': form})

@permission_classes((AllowAny,))
def delete_user(request, user_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('dashboard')

    return render(request, 'delete.html', {'user': user})
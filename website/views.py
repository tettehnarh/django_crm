from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Homepage view function


def home(request):
    # Retrieve all records
    records = Record.objects.all()
    if request.method == 'POST':
        # If the request is POST, handle login attempt
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log in the user
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            # If authentication fails, display error message
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        # If the request is GET, render the homepage with records
        return render(request, 'home.html', {'records': records})

# Logout view function


def logout_user(request):
    # Logout the user
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

# User registration view function


def register_user(request):
    if request.method == 'POST':
        # If the request is POST, handle user registration
        form = SignUpForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the user
            form.save()
            # Authenticate and log in the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered and logged in')
            return redirect('home')
    else:
        # If the request is GET, render the registration form
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


# Delete record view function


def delete_record(request, pk):
    if request.user.is_authenticated:
        # If the user is authenticated, delete the specified record
        record_to_delete = Record.objects.get(id=pk)
        record_to_delete.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        # If the user is not authenticated, redirect to the homepage
        messages.error(request, 'You must be logged in to delete a record')
        return redirect('home')

# Add record view function


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        # If the user is authenticated, handle adding a new record
        if request.method == 'POST':
            if form.is_valid():
                # If the form is valid, save the new record
                form.save()
                messages.success(request, 'Record added successfully')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        # If the user is not authenticated, redirect to the homepage
        messages.error(request, 'You must be logged in to add a record')
        return redirect('home')

# Update record view function


def update_record(request, pk):
    if request.user.is_authenticated:
        # If the user is authenticated, handle updating an existing record
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                # If the form is valid, save the updated record
                form.save()
                messages.success(request, 'Record updated successfully')
                return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        # If the user is not authenticated, redirect to the homepage
        messages.error(request, 'You must be logged in to update a record')
        return redirect('home')

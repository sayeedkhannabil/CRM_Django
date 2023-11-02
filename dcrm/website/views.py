from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddRecordForm, AddCaseForm
from .models import Record, Case

def home(request):
    records = Record.objects.all()
    cases = Case.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate Person
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login Person
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In - Please Try Again...'))
            return redirect('home')

    return render(request, 'home.html',{'records': records, 'cases': cases})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered!'))
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up the record by primary key (pk) and pass it to the template.
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, ('Please log in to view user records.'))
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, ('User Record Has Been Deleted!'))
        return redirect('home')
    
    else:
        messages.success(request, ('Please log in to delete user records.'))
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, ('Record Has Been Added!'))
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, ('Please log in to add user records.'))
        return redirect('home')
    

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def customer_case(request, pk):
    if request.user.is_authenticated:
        # Look up the record by primary key (pk) and pass it to the template.
        customer_case = Case.objects.get(id=pk)
        return render(request, 'case.html', {'customer_case':customer_case})
    else:
        messages.success(request, ('Please log in to view user cases.'))
        return redirect('home')


def delete_case(request, pk):
    if request.user.is_authenticated:
        delete_it = Case.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, ('User Case Has Been Deleted!'))
        return redirect('home')
    
    else:
        messages.success(request, ('Please log in to delete user cases.'))
        return redirect('home')

def add_case(request):
    form = AddCaseForm(request.POST, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_case = form.save()
                messages.success(request, ('Case Has Been Added!'))
                return redirect('home')
        return render(request, 'add_case.html', {'form':form})
    else:
        messages.success(request, ('Please log in to add user cases.'))
        return redirect('home')


def update_case(request, pk):
    if request.user.is_authenticated:
        current_case = Case.objects.get(id=pk)
        form = AddCaseForm(request.POST, request.FILES or None, instance=current_case)
        if form.is_valid():
            form.save()
            messages.success(request, "Case Has Been Updated!")
            return redirect('home')
        return render(request, 'update_case.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')



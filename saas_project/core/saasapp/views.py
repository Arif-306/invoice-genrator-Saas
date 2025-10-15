from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Invoice, Plan, Subscription
import uuid
from django.utils import timezone

# Home
def home(request):
    return render(request, 'home.html')

# Pricing
def pricing(request):
    plans = Plan.objects.all()
    return render(request, 'pricing.html', {'plans': plans})

# Register (expects password1/password2 in template)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  # if register form has email
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not password1:
            messages.error(request, 'Please provide username and password.')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'register.html')

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'login.html')

# Logout
def logout_user(request):
    logout(request)
    return redirect('home')

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    invoices = Invoice.objects.filter(user=request.user)
    # try fetching subscription if exists
    subscription = Subscription.objects.filter(user=request.user).first()
    total_users = User.objects.count()
    return render(request, 'dashboard.html', {
        'invoices': invoices,
        'subscription': subscription,
        'total_users': total_users
    })

# Create Invoice (single correct version)
@login_required(login_url='login')
def create_invoice(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        amount = request.POST.get('amount')
        description = request.POST.get('description', '')
        date = request.POST.get('date')  # expects YYYY-MM-DD from form
        plan_name = request.POST.get('plan_name', 'N/A')  # optional

        # basic validation
        if not client_name or not amount or not date:
            messages.error(request, 'Please fill all required fields.')
            return redirect('create_invoice')

        # create a unique invoice_number (UUID short)
        invoice_number = str(uuid.uuid4()).split('-')[0].upper()

        invoice = Invoice.objects.create(
            invoice_number=invoice_number,
            user=request.user,
            client_name=client_name,
            plan_name=plan_name,
            amount=amount,
            description=description,
            date=date,
            date_issued=timezone.now().date()
        )

        messages.success(request, 'Invoice created successfully!')
        return redirect('invoice_detail', invoice_id=invoice.id)

    return render(request, 'create_invoice.html')

# Invoice detail
@login_required(login_url='login')
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    return render(request, 'invoice_detail.html', {'invoice': invoice})
# settings.py me:
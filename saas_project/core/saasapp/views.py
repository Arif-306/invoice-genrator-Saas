from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Invoice

# ---------- Home Page ----------
def home(request):
    return render(request, 'home.html')

# ---------- Pricing Page ----------
def pricing(request):
    return render(request, 'pricing.html')

# ---------- User Registration ----------
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    
    return render(request, 'register.html')

# ---------- User Login ----------
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    
    return render(request, 'login.html')

# ---------- User Logout ----------
def logout_user(request):
    logout(request)
    return redirect('home')

# ---------- Dashboard ----------
@login_required(login_url='login')
def dashboard(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'invoices': invoices})

# ---------- Create Invoice ----------
@login_required(login_url='login')
def create_invoice(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')

        Invoice.objects.create(
            user=request.user,
            customer_name=customer_name,
            amount=amount,
            due_date=due_date
        )
        messages.success(request, 'Invoice created successfully!')
        return redirect('dashboard')

    return render(request, 'create_invoice.html')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice
from django.contrib.auth.decorators import login_required

@login_required
def create_invoice(request):
    if request.method == "POST":
        client_name = request.POST['client_name']
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['date']

        invoice = Invoice.objects.create(
            client_name=client_name,
            amount=amount,
            description=description,
            date=date,
            user=request.user
        )
        
        return redirect('invoice_detail', invoice_id=invoice.id)

    return render(request, 'create_invoice.html')


@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, user=request.user)
    return render(request, 'invoice_detail.html', {'invoice': invoice})




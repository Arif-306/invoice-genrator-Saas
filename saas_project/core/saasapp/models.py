from django.db import models
from django.contrib.auth.models import User

# -------------------------------
# 🔹 PLAN MODEL
# -------------------------------
class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# -------------------------------
# 🔹 SUBSCRIPTION MODEL
# -------------------------------
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"


# -------------------------------
# 🔹 INVOICE MODEL
# -------------------------------
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    plan_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    date_issued = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client_name}"

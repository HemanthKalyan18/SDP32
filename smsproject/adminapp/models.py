from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username


class Stock(models.Model):
    ticker_symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=255)
    market_capitalization = models.DecimalField(max_digits=15, decimal_places=2)
    dividend_yield = models.DecimalField(max_digits=5, decimal_places=2)
    beta = models.DecimalField(max_digits=6, decimal_places=2)
    week_52_high = models.DecimalField(max_digits=10, decimal_places=2)
    week_52_low = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "stock_table"

    def __str__(self):
        return self.company_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # Unique user ID
    username = models.CharField(max_length=50, unique=True)  # Unique username
    email = models.EmailField(max_length=100, blank=False, unique=True)  # User's email address
    password = models.CharField(max_length=128, blank=False, default="kalyan")  # Hashed password
    date_of_birth = models.DateField(null=False, blank=False)  # Date of birth
    mobile_number = models.CharField(max_length=15, null=False, blank=False)  # Mobile number

    class Meta:
        db_table = "user_table"

    def __str__(self):
        return self.username

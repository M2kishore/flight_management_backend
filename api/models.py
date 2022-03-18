from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.forms import CharField
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone

# Create your models here.
COUNTRY_CODE_CHOICES = (
    ("91", "+91"),
    ("44", "+44"),
)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    mobile_number = models.IntegerField(primary_key=True, unique=True)
    country_code = models.CharField(
        max_length=10, choices=COUNTRY_CODE_CHOICES, default=COUNTRY_CODE_CHOICES[0][0]
    )
    dob = models.DateField(default=datetime.date.today, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    
class Flight(models.Model):
    flight_id = models.CharField(primary_key=True)
    arrival_time = models.TimeField(default=datetime.now().time)
    departure_time = models.TimeField(default=datetime.now().time)
    destination = models.CharField(max_length=100)
    duration = models.TimeField(default=datetime.now().time)
    no_of_seats = models.IntegerField()
    airline_name = models.CharField(max_length=100)
    airport_location = models.CharField(max_length=100)
    available_seats = models.IntegerField()
    type = models.CharField(max_length=100)

SEAT_TYPE_CHOICES = 
class Seat(models.Model):
    flight_id = models.ForeignKey(Flight,null=False,blank=False)
    seat_id = models.CharField(primary_key=True)
    class_type = models.CharField(max_length=100)
    type_of_seat = models.
# class Ticket(models.Model):
#     pnr = models.CharField(max_length=100)
#     passenger_id = models.ForeignKey(User,on_delete=models.CASCADE)
#     flight_id = models.ForeignKey()
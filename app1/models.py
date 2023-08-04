from django.db import models
from django.urls import reverse


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    photo = models.ImageField(upload_to="images")

    designation = models.CharField(max_length=100)

    email_address = models.EmailField(max_length=100, unique=True)

    phone_number = models.CharField(max_length=12, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """
        Return the absolute URL for this employee.
        """
        return reverse("employee-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.first_name

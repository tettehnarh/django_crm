from django.db import models

# Create your models here.


class Record(models.Model):
    # Model fields
    # Automatically set the current datetime when the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        # String representation of the model instance
        return f"{self.first_name} {self.last_name}"

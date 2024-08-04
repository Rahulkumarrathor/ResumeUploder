from django.db import models

# Create your models here.
STATE_CHOICE = (

     ('Andhra Pradesh', 'Andhra Pradesh'),
     ('Arunachal Pradesh', 'Arunachal Pradesh'),
     ('Assam', 'Assam'),
     ('Bihar', 'Bihar'),
     ('Chhattisgarh', 'Chhattisgarh'),
     ('Delhi', 'Delhi'),
     ('Goa', 'Goa'),
     ('Gujarat', 'Gujarat'),
     ('Haryana', 'Haryana'),
     ('Himachal Pradesh', 'Himachal Pradesh'),
     ('Jharkhand', 'Jharkhand'),
     ('Karnataka', 'Karnataka'),
     ('Kerala', 'Kerala'),
     ('Madhya Pradesh', 'Madhya Pradesh'),
     ('Maharashtra', 'Maharashtra'),
     ('Meghalaya',  'Meghalaya'),
     ('Mizoram', 'Mizoram'),
     ('Nagaland', 'Nagaland'),
     ('Odisha', 'Odisha'),
     ('Punjab', 'Punjab'),
     ('Rajasthan', 'Rajasthan'),
     ('Sikkim', 'Sikkim'),
     ('Tamil Nadu', 'Tamil Nadu'),
     ('Telangana', 'Telangana'),
     ('Tripura',  'Tripura'),
     ('Uttar Pradesh', 'Uttar Pradesh'),
     ('Uttarakhand', 'Uttarakhand'),
     ('West Bengal', 'West Bengal'),
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob =models.DateField(auto_now_add=False,auto_now=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(max_length=100, choices=STATE_CHOICE)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimage',blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)


from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Ranchi', 'Ranchi'),
    ('Mumbai', 'Mumbai'),
    ('Dhanbad','Dhanbad'),
    ('Banglore', 'Banglore')

]
class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred job Locations', choices=JOB_CITY_CHOICES,
                                         widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Resume
        fields = [ 'name', 'dob', 'gender', 'locality', 'city', 'pin',
                   'state', 'mobile', 'email',  'job_city', 'profile_image', 'my_file' ]
        labels = {'name': 'Full Name', 'dob': 'Date of Birth','pin': 'Pin Ccde', 'mobile': 'Mobile No.',
                  'profile_image': 'Profile Image', 'my_file': 'Document', 'email': 'Email ID'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),



        }
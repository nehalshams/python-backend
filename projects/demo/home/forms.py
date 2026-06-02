from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        #     'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        #     'phone_number': forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        # }
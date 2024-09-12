from django import forms
from .models import Student , Class
from django.forms import ModelForm
import datetime

class collegedetail(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    class Meta:
        model = Student
        fields = '__all__' 
        widgets = {
            'date_of_birth': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'})
        }
        

        
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth is not None:
            cutoff_date  = datetime.date(1980,1,1)
            # Check if the date of birth is in the past
            if date_of_birth >= datetime.date.today()  :
                raise forms.ValidationError("Invaid date of birth.")
            if date_of_birth<cutoff_date:
                raise forms.ValidationError('invalid date')
        return date_of_birth

class Standard(forms.ModelForm):
    class Meta:
        model= Class
        fields = '__all__'

# class fees(forms.ModelForm):
#     class Meta:
#         model = Fees
#         fields = '__all__'
#         widgets = {
#             'payment_date': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'})
#         }
        
from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name','number','address','email','dateofjoining','duration','fee','room_number')
from platform import mac_ver

from django import forms
from .models import People_model

class people_form(forms.Form):
    name=forms.CharField(max_length=200)
    vacation_plan= forms.CharField(max_length=100)
    visa_status = forms.CharField(max_length=100)


class Activity_form(forms.Form):
    Activity_Name=forms.CharField(max_length=200)
    type=forms.CharField(max_length=10)
    Add_people=forms.CharField(max_length=20)
    customer=forms.CharField(max_length=20)
    Description=forms.CharField(max_length=200)

class people_detail_form(forms.Form):
    name = forms.CharField(max_length=200)
    vacation_plan = forms.CharField(max_length=100)
    visa_status = forms.CharField(max_length=100)
    selectto = forms.CharField(max_length=200)
    selectfrom = forms.CharField(max_length=200)


class Activity_detail_form(forms.Form):
    Activity_Name = forms.CharField(max_length=200)
    Activity_type = forms.CharField(max_length=100)
    selectto = forms.CharField(max_length=200)
    selectfrom = forms.CharField(max_length=200)
    customer=forms.CharField(max_length=20)
    Description=forms.CharField(max_length=2500)

class settings_form(forms.Form):
    Project_Allocated=forms.CharField(max_length=10)

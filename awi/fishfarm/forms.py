from django import forms
from django.forms import ModelForm
from django.db.models import fields
from .models import *

class edit_form(forms.ModelForm):
    class Meta:
        model=log_in
        fields = "__all__"

class delete_form(forms.ModelForm):
    class Meta:
        model= Feedback
        fields = "__all__"
#！、usr/bin/env python
#-*- coding:utf-8 -*-
from django.forms import ModelForm
from .models import Student,State

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class StateForm(ModelForm):
    class Meta:
        model=State
        # field='__all__'
        exclude=['username']#quchu
from xml.dom import ValidationErr
from django import forms
from django.forms import ModelForm
from pydantic import ValidationError
from .models import  absenceReport,FormMaster
from django.contrib.auth.models import User 

class StudentForm(ModelForm): 
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'id': 'password'})
    ) 

    confirm_password = forms.CharField(
        label='Confirm Password',  
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'id': 'c_password'})
    ) 

    phone = forms.CharField(
        label='Phone number', 
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-pill'})
    )

    parent_number = forms.CharField(
        label='Parent number',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-pill'})
    )

    parent_mail = forms.EmailField(
        label='Parent email', 
        widget=forms.EmailInput(attrs={'class': 'form-control rounded-pill'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-pill'})
        }



class AbsenceReport(ModelForm):
    class Meta: 
        model=absenceReport
        fields=("Student_Name","Student_Class","Parent_Name","reason","proveFile",)

        labels={
            'Student_Name':'',
            'reason':'', 
            'proveFile':'Child Pic', 
        
            # 'name':''
        }

        widgets={
            'Student_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name',}),
            'Student_Class':forms.TextInput(attrs={'class':'form-control','placeholder':'Student CLass',}),
            'Parent_Name':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Parent Name',}), 
            'reason':forms.Textarea(attrs={'class':'form-control mt-4','placeholder':'Reason','style':'height:100px'}),  
            'proveFile':forms.FileInput(attrs={'placeholder':'Prove File'}) ,
            # 'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'})  
        }


    def clan_HandleinvalidIndexNumber(self):
        stu_indexNumber=self.cleaned_data.get('stu_indexNumber') 
        if len(stu_indexNumber)!=10:
            raise ValidationError('Index Number is not up')
        return stu_indexNumber


class LoginForm(forms.Form):
    indexNumber = forms.CharField(label='Index Number')
    password = forms.CharField(widget=forms.PasswordInput())
    

class FormMasterForms(forms.ModelForm):
    class Meta:
        model=FormMaster
        fields="__all__"

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control',}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control','max-length':'10'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'picture':forms.TextInput(attrs={'class':'form-control'})
            
        }
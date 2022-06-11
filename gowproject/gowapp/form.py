from django import forms
from gowapp.models import Student
from gowapp.models import Studimg
from gowapp.models import Empp  # auto validation purpose

class StudimgForm(forms.ModelForm):
    class Meta:
        model=Studimg
        fields="__all__"

class StudForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class uploadform(forms.Form):
    firstname=forms.CharField(label="enter first name",max_length="22")
    lastname=forms.CharField(label="enter last name",max_length="22")
    email=forms.EmailField(label="Enter Email")
    file=forms.FileField()

# for auto validation purpose
class EmppForm(forms.ModelForm):
    class Meta:
        model=Empp
        fields="__all__"
        
        
        


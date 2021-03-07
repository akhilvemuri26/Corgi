from django import forms
from django.contrib.auth.models import User
from corgiapp.models import UserProfileInfo, HealthInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pictures', 'dog_breed')
class HealthForm(forms.ModelForm):
    class Meta():
        model = HealthInfo
        fields = ('symptom1', 'symptom2', 'symptom3')

from django import forms
from .models import Profile
from django.contrib.auth.models import User

# user update form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']





# profile form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'sex', 'Dob', 'place_of_birth', 'marital_status', 'course', 'contact_address', 'phone', 'academic_qualifications', 'next_of_kin', 'next_of_kin_phone', 'session', 'disability']
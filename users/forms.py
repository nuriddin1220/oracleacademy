from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['designation', 'bio', 'age', 'experience_years',
                  'projects', 'address', 'workplace', 'phone_number', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

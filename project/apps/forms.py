from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']



class UserEditForm(forms.ModelForm):
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(render_value=False),
        required=False,
        help_text="Leave blank if you don't want to change the password."
    )
    
    current_password_display = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={'readonly': 'readonly', 'value': '********'}),  # Placeholder for current password
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'new_password']  # Only username, email, and new password

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        if self.cleaned_data['new_password']:
            user.set_password(self.cleaned_data['new_password'])  # Hash and set new password
        if commit:
            user.save()
        return user

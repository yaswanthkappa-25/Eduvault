from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="College Email ID",
        widget=forms.EmailInput(attrs={
            "placeholder": "yourname@college.edu",
            "autocomplete": "email",
        })
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"].strip().lower()
        user.username = user.email

        if commit:
            user.save()

        return user

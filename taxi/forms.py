from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        required=True,
        validators=[RegexValidator(regex=r"^[A-Z]{3}\d{5}$",)]
    )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = (
            UserCreationForm.Meta.fields
            + ("first_name", "last_name", "license_number")
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        required=True,
        validators=[RegexValidator(regex=r"^[A-Z]{3}\d{5}$", )]
    )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = ("license_number",)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"

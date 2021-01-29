from django import forms
from django.core import validators


class CreateProductForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام و نام خانوادگی خود را وارد کنید"}),
        label="نام و نام خانوادگی",
        validators=[
            validators.MaxLengthValidator(200, "نام و نام خانوادگی نمیتواند بیشتر از 200 کاراکتر باشد")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد کنید"}),
        label="ایمیل",
        validators=[
            validators.EmailValidator(200, "ایمیل نمیتواند بیشتر از 200 کاراکتر باشد")
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "لطفا متن نطر خود را وارد کنید"}),
        label="متن نطر",
    )

    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

from django import forms
from django.core import validators


class NewUserOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )


class SendRequestForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام و نام خانوادگی خود را وارد کنید"}),
        label="نام و نام خانوادگی",
        validators=[
            validators.MaxLengthValidator(500, "نام و نام خانوادگی نمیتواند بیشتر از 200 کاراکتر باشد")
        ]
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا تلفن خود را وارد کنید"}),
        label="تلفن",
        validators=[
            validators.MaxLengthValidator(15, " تلفن نمیتواند بیشتر از 15 کاراکتر باشد")
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد کنید"}),
        label="ایمیل",
        validators=[
            validators.EmailValidator(500, "ایمیل نمیتواند بیشتر از 200 کاراکتر باشد")
        ]
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا آدرس خود را وارد کنید"}),
        label="آدرس",
        validators=[
            validators.MaxLengthValidator(1000, "آدرس نمیتواند بیشتر از 1000 کاراکتر باشد")
        ]
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام شهر خود را وارد کنید"}),
        label="شهر",
        validators=[
            validators.MaxLengthValidator(500, "نام شهر نمیتواند بیشتر از 500 کاراکتر باشد")
        ]
    )

    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا کد پستی خود را وارد کنید"}),
        label="کد پستی",
        validators=[
            validators.MaxLengthValidator(25, "کد پستی نمیتواند بیشتر از 25 کاراکتر باشد")
        ]
    )

from django import forms
from django.contrib.auth.models import User
from django.core import validators


class EditPanelForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام   خود را وارد کنید"}),
        label="نام  ",
        validators=[
            validators.MaxLengthValidator(150, "نام و نام خانوداگی نمیتواند بیشتر از 150 کاراکتر باشد")
        ]
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا  نام خانوادگی خود را وارد کنید"}),
        label=" نام خانوادگی ",
        validators=[
            validators.MaxLengthValidator(150, "نام و نام خانوداگی نمیتواند بیشتر از 150 کاراکتر باشد")
        ]
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا شماره تلفن خود را وارد کنید"}),
        label="شماره تلفن ",
        validators=[
            validators.MaxLengthValidator(150, "شماره تلفن نمیتواند بیشتر از 15 کاراکتر باشد")
        ]
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "لطفا آدرس خود را وارد کنید"}),
        label="آدرس "
    )

    # image = forms.ImageField(label="تصویر")


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}),
        label="نام کاربری"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را وارد کنید"}),
        label="رمز عبور"
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_user_exists = User.objects.filter(username=user_name).exists()
        if not is_user_exists:
            raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است")

        return user_name


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}),
        label="نام کاربری"
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد کنید"}),
        label="ایمیل",
        validators=[
            validators.EmailValidator("ایمیل وارد شده معتبر نمی باشد")
        ])

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را وارد کنید"}),
        label="رمز عبور"
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را تکرار کنید"}),
        label="تکرار رمز عبور"
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exists_by_username = User.objects.filter(username=username).exists()

        if is_exists_by_username:
            raise forms.ValidationError("نام کاربری زیر قبلا ثبت شده است.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exists_by_email = User.objects.filter(email=email).exists()
        if is_exists_by_email:
            raise forms.ValidationError("ایمیل وارد شده قبلا ثبت شده است.")
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("رمز های عبور مغایرت دارند")
        return password

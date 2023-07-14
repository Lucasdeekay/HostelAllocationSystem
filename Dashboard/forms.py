from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your username',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'required': '',
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username or not password:
            raise forms.ValidationError("Field cannot be empty")


class RegisterForm(forms.Form):
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    matric_no = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Matric No',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'required': '',
                'class': 'form-control',
            }
        )
    )
    gender = forms.CharField(
        widget=forms.Select(
            choices=[
                ('M', 'Male'),
                ('F', 'Female'),
            ],
            attrs={
                'required': '',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'required': '',
                'class': 'form-control'
            }
        )
    )
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'required': '',
                'class': 'form-control'
            }
        )
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        last_name = cleaned_data.get('last_name')
        first_name = cleaned_data.get('first_name')
        matric_no = cleaned_data.get('matric_no')
        email = cleaned_data.get('email')
        gender = cleaned_data.get('gender')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not last_name or not first_name or not matric_no or not gender or not email or not password or not confirm_password:
            raise forms.ValidationError("Field cannot be empty")


class ForgotPasswordForm(forms.Form):
    user_id = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Matric No/Staff Id',
                'required': '',
                'class': 'input',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(ForgotPasswordForm, self).clean()
        user_id = cleaned_data.get('user_id')
        email = cleaned_data.get('email')
        if not user_id or not email:
            raise forms.ValidationError("Field cannot be empty")


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'required': '',
                'class': 'input',
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not password or not confirm_password:
            raise forms.ValidationError("Field cannot be empty")


class UpdatePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Old Password',
                'required': '',
                'class': 'input',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter New Password',
                'required': '',
                'class': 'input',
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm New Password',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        old_password = cleaned_data.get('old_password')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not old_password or not password or not confirm_password:
            raise forms.ValidationError("Field cannot be empty")

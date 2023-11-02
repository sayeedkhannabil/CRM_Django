# Import necessary modules and classes for the user registration form.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Case

# Define a custom user registration form that inherits from UserCreationForm.
class SignupForm(UserCreationForm):
    # Define additional fields for the form (email, first name, and last name).
    email = forms.EmailField(label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))

    class Meta:
        # Specify the model (User) and the fields to be included in the form.
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Customize widget attributes and labels for the 'username' field.
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        # Customize widget attributes and labels for the 'password1' field.
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        # Customize widget attributes and labels for the 'password2' field.
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# CREATE ADD RECORD FORM

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "City", "class": "form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "State", "class": "form-control"}), label="")
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Zip Code", "class": "form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)


# CREATE ADD CASE FORM
class AddCaseForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Case.STATUS_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), initial='pending', label="Status")
    pdf_file = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}))
    
    class Meta:
        model = Case
        fields = ('status', 'pdf_file')


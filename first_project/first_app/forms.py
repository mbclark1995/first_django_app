from django import forms
from django.contrib.auth.models import User
from django.core import validators
# import directory.file import MyModel
from first_app.models import UserProfileInfo

########### ALWAYS ALWAYS ALWAYS put the word "Form" at the end of naming a form class


# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)

##### Making your own validator properly
# For Validation...
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Must start with z")

# def verify_email(value1, value2):
#     if value1 != value2:
#         raise forms.ValidationError("Emails must match.")




##### Making validator rather than using builtin
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Bot kind ain't allowed in these parts.")
    #     return  botcatcher




class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again.")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                  widget = forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0, "No bots buddy."),])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verified_email = all_clean_data['verify_email']
        if email != verified_email:
            raise forms.ValidationError("Emails must match.")


    ##### Making validator rather than using builtin
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Bot kind ain't allowed in these parts.")
    #     return  botcatcher

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ("username", "email")


# Creating a legit new user form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")

class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.URLField(required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")


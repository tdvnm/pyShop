from django import forms

class contactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "your naem plx"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "your eMale plx"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class" : "form-control",
                "placeholder" : "your content plx"
            }
        )
    )

def clean_email(self):
    email = self.cleaned_data.get("email")
    if not "gmail.com" in email:
        raise forms.ValidationError("has to have gmail.com in email")
    return email

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    

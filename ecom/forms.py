from django import forms

class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"placeholder":"Your full name"
				}
				)
			)
	email = forms.EmailField(
	
		widget=forms.EmailInput(
			attrs={
				"class": "form-control",
				"placeholder":"Your Email"
				}
				)
	
		)
	content = forms.CharField(
	
		widget=forms.Textarea(
			attrs={
				"class": "form-control",
				"placeholder":"Your Message"
				}
				)
	
			
			)
	
	hobby = forms.CharField(
	
		widget=forms.Textarea(
			attrs={
				"class": "form-control",
				"placeholder":"Your Message"
				}
				)
	
	
	
			)	
	
	
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("email has to be gmail")
		return email	
		
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	
class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.CharField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
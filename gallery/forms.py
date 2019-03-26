from django import forms
from .models import Image,Profile
class GalleryLetterForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date']
        widgets = {
            'profile': forms.CheckboxSelectMultiple(),
        }  
class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	image = forms.ImageField(label = 'Image Field')         
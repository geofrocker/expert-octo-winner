from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post

class PostForm(forms.ModelForm):
	product_Name = forms.CharField(
	    widget=forms.TextInput(attrs={'class': 'form-control'}),
	    max_length=30,
	    required=False)
	description = forms.CharField(
	    widget=forms.TextInput(attrs={'class': 'form-control'}),
	    max_length=30,
	    required=False)
	category = forms.CharField(
	    widget=forms.TextInput(attrs={'class': 'form-control'}),
	    max_length=50,
	    required=False)
	price = forms.CharField(
	    widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter amount e.g 5000'}),
	    max_length=75,
	    required=False)
	
	location = forms.CharField(
	    widget=forms.TextInput(attrs={'class': 'form-control','id': 'id_location'}),
	    max_length=50,
	    required=False)
	phone = forms.CharField(
	    widget=forms.TextInput(attrs={'class': 'form-control'}),
	    max_length=50,
	    required=False)
	class Meta:
		model=Post
		fields=[
			"product_Name",
			"description",
			"category",
			"price",
			"country",
			"location",
			"phone",
			"image"	

		]
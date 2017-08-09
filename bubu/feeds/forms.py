from django import forms
from .models import Feed


class FeedForm(forms.ModelForm):

    post = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control flat','rows':'3', 'name':'post', 'id':'standalone', 'placeholder':'What is on your mind!','label':''}),
        required=True)
    
    class Meta:
        model = Feed
        fields = ['post', 'photo',]

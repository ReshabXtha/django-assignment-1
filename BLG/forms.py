from django import forms
from BLG.models import Blog


class AddBlogsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

from django import forms
from faceInImage.models import pic

class picForm(forms.ModelForm):
    class Meta:
        model = pic
        fields = ('picture',)
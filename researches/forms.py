
from django import forms
from django import forms
from researches.models import Research


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields=['title','content','image']


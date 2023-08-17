from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
  class Meta:
    model = Articles
    fields=['title','anons','fullText','date']
    
    widgets = {
      "title": TextInput(attrs={
        'class':'form-control',
        'placeholder':'Title'
      }),
      "anons": TextInput(attrs={
        'class':'form-control',
        'placeholder':'Description'
      }),
      "fullText": Textarea(attrs={
        'class':'form-control',
        'placeholder':'Text'
      }),
      "date": DateTimeInput(attrs={
        'class':'form-control',
        'placeholder':'Date'
      })
    }
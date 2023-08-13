from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError

from .models import Men, Category


# class AddMen(forms.Form):
#     title = forms.CharField(max_length=100, label='Заголовок')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':"10"}))
#     is_published = forms.BooleanField(required=False, initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')
class AddMen(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Начальника тут нет'

    class Meta:
        model = Men
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Начальника, длина далека')
        return title


class ContactForm(forms.Form):
    name = forms.CharField(label='имя', max_length=100)
    email = forms.EmailField(label='email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
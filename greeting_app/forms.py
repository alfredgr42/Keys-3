from django import forms
from .models import UserName

class UserNameForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите ваше имя',
            'id': 'userName'
        }),
        label="Ваше имя"
    )
    
    class Meta:
        model = UserName
        fields = ['name']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('❌ Имя не может быть пустым!')
        if len(name.strip()) < 2:
            raise forms.ValidationError('❌ Имя должно содержать минимум 2 символа!')
        if len(name.strip()) > 50:
            raise forms.ValidationError('❌ Имя слишком длинное (максимум 50 символов)!')
        return name.strip().title()

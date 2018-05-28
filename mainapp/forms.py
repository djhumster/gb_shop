from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'email@example.com', 'class': 'form-control'})
    )
    sender = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Имя', 'class': 'form-control'})
    )
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Тема', 'class': 'form-control'})
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение...', 'class': 'form-control'})
    )

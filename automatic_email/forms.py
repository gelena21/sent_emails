from django import forms
from automatic_email.models import Client, Mailout, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'name', 'comment']


class MailoutForm(forms.ModelForm):
    class Meta:
        model = Mailout
        fields = ['start_date', 'period', 'status', 'message']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']

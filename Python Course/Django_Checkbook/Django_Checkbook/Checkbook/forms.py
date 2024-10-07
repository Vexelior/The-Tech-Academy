from django.forms import ModelForm
from .models import Account, Transaction


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

from django import forms

from stavki.models import Orders, Catalog


class OrderForm(forms.Form):
    choice = forms.ChoiceField()
    order_sum = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bet = Catalog.objects.get(pk=self.initial['id'])
        self.fields['choice'].initial = bet.enemy_f
        self.fields['choice'].choices = [(0, bet.enemy_f), (1, bet.enemy_s)]


class BalanceForm(forms.Form):
    sum = forms.IntegerField()

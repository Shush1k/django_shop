from django import forms
from .models import Order
from localflavor.ru.forms import RUPostalCodeField
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):
    # тут можно прописать определенную форму под каждую страну
    # не совсем понятно конечно как именно выбирать форму
    # нужно ли созавать отдельную форму под это дело?
    postal_code = RUPostalCodeField(label=_('Postal code'))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']

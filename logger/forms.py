from django.forms import Form, BooleanField, RadioSelect


class TrueFalseForm(Form):
    choice = BooleanField(
        widget=RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        initial=False,
        required=False,
        label='Вы уверены, что хотите удалить?')

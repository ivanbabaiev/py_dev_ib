# -*- coding: utf-8 -*-


import crispy_forms.bootstrap as bs3

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from django import forms
from group.models import Group
from students.models import Student


class GroupForm(forms.ModelForm):

    name = forms.CharField(label='Имя группы')  # Имя группы
    captain = forms.ModelChoiceField(Student.objects.none(), label="Староста группы",
                                     required=False, empty_label="")  # Староста группы

    class Meta:
        model = Group
        fields = [
            'name',
            'captain',
        ]

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-7'
    helper.field_class = 'col-sm-7'
    helper.layout = Layout(

            Field('name', css_class='input-sm'),
            bs3.FieldWithButtons('captain',
                 bs3.FieldWithButtons(HTML("""{% if form.instance.captain_id %}
                                              <a id="student_url" href="{% url 'students:edit_student' form.instance.captain_id %}"
                                              type="submit" class="btn btn-success edit_counterparty">
                                              <span class="glyphicon glyphicon-pencil" style="color:white;">
                                              </span> Ред.</a>
                                              {% endif %}""")),
                  wrapper_class='col-xs-3 col-sm-3 col-md-3 col-lg-3',
                  placeholder="Группа",
                  ),

            bs3.FormActions(Submit('purchase', 'Сохранить', css_class='btn btn-success'))
    )

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        try:
            self.fields['captain'].queryset = Student.objects.filter(group=kwargs['instance'])
        except:
            self.fields['captain'].queryset = Student.objects.all()
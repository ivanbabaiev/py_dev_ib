# -*- coding: utf-8 -*-


import crispy_forms.bootstrap as bs3

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from django import forms
# from django.forms import SelectDateWidget
from django.forms.extras import SelectDateWidget

from students.models import Student
from group.models import Group



class StudentForm(forms.ModelForm):

    date_of_birth = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
                                     required=False, label="День рождения")  # День рождения
    group = forms.ModelChoiceField(Group.objects.all(), label="Группа",
                                   required=False, empty_label="")  # Группа

    class Meta:
        model = Student
        fields = [
            'name',
            'surname',
            'father_name',
            'student_card',
            'group',
            'date_of_birth'
        ]

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-7'
    helper.field_class = 'col-sm-7'
    helper.layout = Layout(

        Field('name', css_class='input-sm'),
        Field('surname', css_class='input-sm'),
        Field('father_name', css_class='input-sm'),
        Field('student_card', css_class='input-sm'),
        Field('date_of_birth', datadatepicker='datepicker'),
        bs3.FieldWithButtons('group',
             bs3.FieldWithButtons(HTML("""{% if form.instance.group_id %}
                                          <a  id="group_url" href="{% url 'group:edit_group' form.instance.group_id %}"
                                          type="submit" class="btn btn-success edit_counterparty">
                                          <span class="glyphicon glyphicon-pencil" style="color:white;">
                                          </span> Ред.</a>
                                          {% endif %}""")),
              wrapper_class='col-xs-3 col-sm-3 col-md-3 col-lg-3',
              placeholder="Студент",
              ),

        bs3.FormActions(Submit('purchase', 'Сохранить', css_class='btn btn-success'))
    )

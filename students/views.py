# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt

from logger.forms import TrueFalseForm
from students.models import Student
from students.forms import StudentForm


def student_list(request):
    student_list = Student.objects.all().order_by('name')
    return render(request, 'students/student_list.html', {'student_list': student_list})


@login_required(login_url='/accounts/login/')
def edit_student(request, student_id=None):
    if request.method == 'POST':
        if student_id is None:
            form = StudentForm(request.POST)
        else:
            edit_student = get_object_or_404(Student, id=student_id)
            form = StudentForm(request.POST, instance=edit_student)
        if form.is_valid():
            form.save()
            return redirect(reverse('students:students_list', args={}))
    else:
        if student_id is None:
            form = StudentForm()
        else:
            student = get_object_or_404(Student, id=student_id)
            form = StudentForm(instance=student)
        return render(request, 'students/edit_student.html', {
            'form': form,
        })


@csrf_exempt
@login_required(login_url='/accounts/login/')
def remove_student(request, student_id, instance_type):
    if instance_type == 1:
        instance = get_object_or_404(Student, pk=student_id)
    else:
        raise Http404
    if request.method == 'POST':
        form = TrueFalseForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            if choice:
                instance.delete()
            return redirect(reverse('students:students_list', args={}))
    else:
        form = TrueFalseForm()
    data = dict(form=form, instance_id=student_id, instance=instance, instance_type=instance_type)
    return render_to_response('logger/deletion.html', data)
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from group.forms import GroupForm
from group.models import Group
from logger.forms import TrueFalseForm
from students.models import Student


def group_list(request):
    group_list = Group.objects.all().order_by('name')
    dict = {}
    for group in group_list:
        count = Student.objects.filter(group=group.id).count()
        dict[group.id]=count
    return render(request, 'group/group_list.html', {
        'group_list': group_list,
        'dict': dict,
    })


def group_detail(request, group_id):
    student_list = Student.objects.filter(group=group_id).order_by('name')
    return render(request, 'group/group_detail.html', {'student_list': student_list})


@login_required(login_url='/accounts/login/')
def edit_group(request, group_id=None):
    if request.method == 'POST':
        if group_id is None:
            form = GroupForm(request.POST)
        else:
            edit_group = get_object_or_404(Group, id=group_id)
            form = GroupForm(request.POST, instance=edit_group)
        if form.is_valid():
            form.save()
            return redirect(reverse('group:groups_list', args={}))
    else:
        if group_id is None:
            form = GroupForm()
        else:
            group = get_object_or_404(Group, id=group_id)
            form = GroupForm(instance=group)
        return render(request, 'group/edit_group.html', {
            'form': form,
        })


@csrf_exempt
@login_required(login_url='/accounts/login/')
def remove_group(request, group_id, instance_type):
    if instance_type == 2:
        instance = get_object_or_404(Group, pk=group_id)
    else:
        raise Http404
    if request.method == 'POST':
        form = TrueFalseForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            if choice:
                instance.delete()
            return redirect(reverse('group:groups_list', args={}))
    else:
        form = TrueFalseForm()
    data = dict(form=form, instance_id=group_id, instance=instance, instance_type=instance_type)
    return render_to_response('logger/deletion.html', data)
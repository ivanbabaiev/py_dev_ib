from group.models import Group
from django.contrib import admin
from students.models import Student

class Inline(admin.TabularInline):
    model = Student
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain')
    inlines = [Inline]

admin.site.register(Group, GroupAdmin)
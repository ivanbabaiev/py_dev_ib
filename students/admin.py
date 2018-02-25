from students.models import Student
from django.contrib import admin

class StudAdmin(admin.ModelAdmin):
    search_fields = ('surname', 'name', 'student_card')

admin.site.register(Student, StudAdmin)
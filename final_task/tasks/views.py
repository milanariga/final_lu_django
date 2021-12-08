from django.shortcuts import render
from .forms import (
    StudentForm
)

from .models import Student
from .student_class import Student_class


def add_stud_grades(request):

    form = StudentForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            stud = Student_class(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades']
            )

            # new_student_record = Student(
            #     name=stud.name,
            #     grades=stud.grades,
            #     average_grade=stud.get_average_grades(),
            # )
            #
            # grades = new_student_record.save()

            # form.average_grade = form.save(commit=False)
            form.instance.average_grade = stud.get_average_grades()

            grades = form.save()
            context = {
                'grades': grades
            }

            return render(
                request,
                template_name='student_grades.html',
                context=context
            )
    return render(
        request,
        template_name='student_form.html',
        context={'form':form}
    )


def get_all_students(request):

    students = Student.objects.all()

    context = {
        'students': students,
    }

    return render(
        request,
        template_name='students.html',
        context=context,
    )


def get_student(request, student_id):

    student = Student.objects.get(id=student_id)

    context = {
        'student': student,
    }

    return render(
        request,
        template_name='student.html',
        context=context,
    )


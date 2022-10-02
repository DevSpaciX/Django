from unicodedata import name
from django.views.generic import TemplateView
from groups.models import Student , Group , Teacher


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self , **kwargs):
        students = Student.objects.all()
        groups = Group.objects.all()
        teachers = Teacher.objects.all()
        students_by_group = Student.objects.filter(
            group = Group.objects.get(name="Python_Pro")
        )
        students_by_teacher = Student.objects.filter(
            group__in=Group.objects.filter(id__in=Teacher.objects.filter(name="Alexandra Paper"))
        )
        students_by_age = Student.objects.filter(age__gt=20)
        students_by_teacher_age = Student.objects.filter(
            group = Group.objects.filter(
                id__in=Teacher.objects.filter(age__gt=20)
            ).first()
        )
        email_students = Student.objects.filter(email__icontains = 'gmail.com')

        print(students ,groups, teachers, students_by_group, students_by_teacher, students_by_age,
              students_by_teacher_age, email_students)
        return {}

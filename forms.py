from django.forms import ModelForm
from courses.models import Course, Unit, Lecture

class CourseForm(ModelForm):
    class Meta:
        model = Course

class UnitForm(ModelForm):
    class Meta:
        model = Unit

class LectureForm(ModelForm):
    class Meta:
        model = Lecture



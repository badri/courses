from django.db import models
from django.contrib.auth.models import User
'''
TODO:
1. merge quiz and category with this app.
2. add oembed capability for major providers like vimeo.
3. send bulk email to course members about new unit notifications, quiz, exam, last date, results etc.
4. course level stats, like 
  a. no. of enrollments per day
  b. % pass, % completion
  c. demographics, like which discipline students, which college enrolls most
5. forum integration using Askbot
6. course/unit/lecture locking, where one unit depends on another course/unit/lecture to be finished.
7. still no sense of a student finishing a course, when has a student finished a course?
8. oembed and video integration
'''

class Course(models.Model):
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(_('slug'), unique=True)
    # how to stitch category field from quiz to course app?
    description = models.TextField(_('description'), blank=True, null=True)
    start_date = models.DateField(_('course start date'), auto_now_add=True)
    end_date = models.DateField(_('course end date'), blank=True)
    capacity = models.IntegerField(blank=True)
    syllabus = models.TextField(_('course syllabus'), blank=True, null=True)
    software = models.TextField(_('required software/materials'), blank=True, null=True)
    references = models.TextField(_('Recommended Reference Books'), blank=True, null=True)
    # todo: add good related names
    faculty = models.ManyToManyField(User)
    students = models.ManyToManyField(User)
    

class Unit(models.Model):
    course = models.ForeignKey(Course)
    description = models.TextField(_('description'), blank=True, null=True)

class Lecture(models.Model):
    unit = models.ForeignKey(Unit)
    lecture_date = models.DateField(_('When was the lecture held'))
    description = models.TextField(_('description'), blank=True, null=True)
    # add quiz here, will be a many to many relationship

class Material(models.Model):
    # can be a doc, video, slide. will be embed using open embed api in page.
    # is associated with any course/unit/lecture
    pass

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from courses.fields import PercentField

'''
TODO:
1. merge quiz and category with this app. - category will be converted to django tagging app.
2. add oembed capability for major providers like vimeo. - not needed
3. send bulk email to course members about new unit notifications, quiz, exam, last date, results etc.
4. course level stats, like 
  a. no. of enrollments per day  - new model, maybe merged with CourseProgress
  b. % pass, % completion
  c. demographics, like which discipline students, which college enrolls most
5. forum integration using Askbot - skipped for MVP
6. course/unit/lecture locking, where one unit depends on another course/unit/lecture to be finished. - done
7. still no sense of a student finishing a course, when has a student finished a course?  - new model called CourseProgress
8. oembed and video integration - skipped, instead, django attachments will be used.
9. lecture, unit dates must validate within course dates, if specified.
'''

class Course(models.Model):
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(_('slug'), unique=True)
    # how to stitch category field from quiz to course app?
    description = models.TextField(_('description'), blank=True, null=True)
    start_date = models.DateField(_('course start date'), auto_now_add=True)
    end_date = models.DateField(_('course end date'), blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    syllabus = models.TextField(_('course syllabus'), blank=True, null=True)
    software = models.TextField(_('required software/materials'), blank=True, null=True)
    references = models.TextField(_('Recommended Reference Books'), blank=True, null=True)
    # todo: add good related names
    faculty = models.ManyToManyField(User, related_name='faculty')
    dependent_courses = models.ManyToManyField('self', null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title
    

class Unit(models.Model):
    course = models.ForeignKey(Course)
    description = models.TextField(_('description'), blank=True, null=True)
    start_date = models.DateField(_('unit start date'), auto_now_add=True)
    end_date = models.DateField(_('unit end date'), blank=True, null=True)

class Lecture(models.Model):
    unit = models.ForeignKey(Unit)
    lecture_date = models.DateField(_('When was the lecture held'))
    description = models.TextField(_('description'), blank=True, null=True)
    # add quiz here, will be a many to many relationship

class Material(models.Model):
    # can be a doc, video, slide. will be embed using open embed api in page.
    # is associated with any course/unit/lecture
    limit = models.Q(app_label = 'courses', model = 'course') | models.Q(app_label = 'course', model = 'unit') | models.Q(app_label = 'courses', model = 'lecture')
    content_type = models.ForeignKey(ContentType, limit_choices_to = limit)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

# add a separate model for video links, associated only with Lecture model

class Enrolment(models.Model):
    student = models.ForeignKey(User)
    limit = models.Q(app_label = 'courses', model = 'course') | models.Q(app_label = 'course', model = 'unit') | models.Q(app_label = 'courses', model = 'lecture')
    content_type = models.ForeignKey(ContentType, limit_choices_to = limit)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    completion =  models.PercentField(default=0)
    enrolment_date = models.DateTimeField(_('When was the enrolment made'), , auto_now_add=True)

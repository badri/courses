from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.core.context_processors import csrf
from django.utils import timezone
from quiz.models import *
from courses.models import *
from courses.forms import *
from courses.decorators import professor

def course(request, name):
    course = get_object_or_404(Course, slug=name)
    return render_to_response('courses/course.html', {'course': course })

def course_edit(request, name):
    course = get_object_or_404(Course, slug=name)
    if request.method == 'POST':
        session_form = CourseForm(request.POST, instance=course)
        session_form.save()
        #todo: error handling
        return HttpResponseRedirect(reverse('courses.views.course', args=(course.slug,)))
    else:
        session_form = CourseForm(instance=course)
        c = {'session_form': session_form }
        c.update(csrf(request))
        return render_to_response('courses/session_edit.html', c)
    
@professor
def course_analytics(request, name):
    pass

def unit(request, name):
    pass

def unit_edit(request, name):
    pass

def lecture(request, name):
    pass

def lecture_edit(request, name):
    pass


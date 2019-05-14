from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Course_Category, Course_Materials
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView
from .filters import Course_Mat_Filters
from forum.models import Question



# Create your views here.

# dashboard 
@login_required
def dashboard(request):
    # get all course materials
    course_material = Course_Materials.objects.all()

    # get all course category
    course_category = Course_Category.objects.all()

    # get all forum questions
    questions = Question.objects.all()


    # get latest course materials
    latest_course_material = get_list_or_404(Course_Materials, latest = True)


    # context
    context = {
        'latest_course_material':latest_course_material,
        'course_material':course_material,
        'course_category':course_category,
        'questions':questions
    }

    return render(request, 'dashboard/dashboard.html', context)




class Course_Mat(ListView):
    queryset = Course_Materials.objects.all()
    context_object_name = 'course_materials'
    paginate_by = 5
    template_name = 'dashboard/course_materials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Course_Mat_Filters(self.request.GET, queryset = self.get_queryset())
        return context

    

# Course category
@login_required
def course_cat(request):
    course_category = Course_Category.objects.all()

    # context
    context = {
        'course_category':course_category,
    }
    return render(request, 'dashboard/course_category.html', context)

@login_required
def course_listing(request, id):
    #fetch data
    course_category = get_object_or_404(Course_Category, id = id)
    course_materials = get_list_or_404(Course_Materials, category = course_category)

    # context
    context = {
        'course_materials':course_materials,
        'course_category': course_category
    }
    return render(request, 'dashboard/course_list.html', context)



    


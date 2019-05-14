from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    # path('course_material/', views.course_materials, name = 'course_materials'),
    path('course_material/', views.Course_Mat.as_view(), name = 'course_materials'),
    path('course_category/', views.course_cat, name = 'course_category'),
    path('course_list/<int:id>', views.course_listing, name = 'course_list'),
]

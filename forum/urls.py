from django.urls import path
from . import views
urlpatterns = [
    path('ask/', views.ask_question, name = 'ask_question'),
    path('questions', views.view_questions, name = 'view_questions'),
    path('details/<int:id>/', views.detail_question, name = 'question_detail')
   
]

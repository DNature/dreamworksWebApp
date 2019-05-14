from django import forms
from .models import Question, Answer
from django.contrib.auth import get_user_model

# question ask form
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'Question']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
from django.shortcuts import render, redirect
from .forms import QuestionForm, AnswerForm
from django.contrib import messages
from .models import Question, Answer
from django.shortcuts import get_object_or_404

# Create your views here.

# ask question
def ask_question(request):
    if request.method == 'POST':
        quest_form = QuestionForm(request.POST)
        
        if quest_form.is_valid():
            submit = quest_form.save(commit=False)
            submit.user = request.user
            submit.save()
            messages.success(request, 'Question Posted Successfully')
            return redirect('ask_question')
    else:
        quest_form = QuestionForm()
    context = {
            'quest_form':quest_form,
        } 
    
    return render(request, 'forum/ask.html', context)


# view questions
def view_questions(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'forum/questions.html', context)


def detail_question(request, id):
    question = get_object_or_404(Question, id = id)
    answer = question.answers.all()
    user = request.user

    # answer form
    if request.method == 'POST':
        ans_form = AnswerForm(request.POST)
        
        # check if form is valid
        if ans_form.is_valid():
            submit = ans_form.save(commit=False)
            submit.question = question
            submit.user = user
            submit.save()
            messages.success(request, 'Answer Posted Successfully')
            

    else:
        ans_form = AnswerForm()
        
        
    context = {
        'answer': answer,
        'question': question,
        'ans_form': ans_form
    }
    return render(request, 'forum/detail.html', context)

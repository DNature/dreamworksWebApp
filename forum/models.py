from django.db import models
from django.conf import settings
from django.urls.base import reverse

# Create your models here.

# question model
class Question(models.Model):
    title = models.CharField(max_length = 200)
    Question = models.TextField()
    user = models.ForeignKey(to = settings.AUTH_USER_MODEL,  on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.id })


# answer model
class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers')

    class Meta:
        ordering = ('-created',)


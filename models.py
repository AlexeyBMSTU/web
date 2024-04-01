from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class User1(models.Model):
    user_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.user_id} | {self.title}"
    
class Question(models.Model):
    question_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT )
    def __str__(self)-> str:
        return f"{self.question_id} | {self.title}"

class Answer(models.Model):
    answer_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.answer_id} | {self.title}"
    
class Tag(models.Model):
    tag_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.tag_id} | {self.title}"
    
class FeedBack(models.Model):
    feedback_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.feedback_id} | {self.title}"
    
class Test3(models.Model):
    feedback_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.feedback_id} | {self.title}"



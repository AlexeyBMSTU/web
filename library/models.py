from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AuthorManager(models.Manager):
    def get_alive(self):
        self.filter(user_id = 2)

class User1(models.Model):
    user_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    userID = models.ForeignKey('User1', on_delete=models.PROTECT, null=True)
    objects = AuthorManager()
    class Meta:
        verbose_name_plural = "User1"
    
    def __str__(self)-> str:
        return f"{self.user_id} | {self.title}"
    
class Question(models.Model):
    question_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    author_id = models.ForeignKey('Question', on_delete=models.PROTECT, null=True)
    class Meta:
        verbose_name_plural = "Question"
    def __str__(self)-> str:
        return f"{self.question_id} | {self.title}"

class Answer(models.Model):
    answer_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    questionID = models.ForeignKey('Answer', on_delete=models.PROTECT, null=True)
    class Meta:
        verbose_name_plural = "Answer"
    def __str__(self)-> str:
        return f"{self.answer_id} | {self.title}"
    
class Tag(models.Model):
    tag_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    tagID = models.ForeignKey('Tag', on_delete=models.PROTECT, null=True)
    # class Meta:
    #     verbose_name_plural = "Tag"
    def __str__(self)-> str:
        return f"{self.tag_id} | {self.title}"
    
class FeedBack(models.Model):
    feedback_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    FeedBackRating = models.ForeignKey('FeedBack', on_delete=models.PROTECT, null=True)
    class Meta:
        verbose_name_plural = "FeedBack"
    def __str__(self)-> str:
        return f"{self.feedback_id} | {self.title}"




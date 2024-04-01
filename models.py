from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class AuthorManager(models.Manager):
    def alive(self):
        return self.filter(death_date__isnull=True)



class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    date_written = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', related_name='books')
    def __str__(self)-> str:
        return f"{self.title} | {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)


    objects = AuthorManager()

    def __str__(self)-> str:
        return f"{self.name} {self.surname}"

class Question(models.Model):
    text = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.text} | {self.author}"

class Answer(models.Model):
    question_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    def __str__(self)-> str:
        return f"{self.question_id} | {self.title}"
    
    
#u = User.objects.get(pk=1)
#pushkin = Question(text='wut?', author='Alex')
#pushkin.save()
#Answer.objects.all().delete()
#ans = Answer.objects.all()
#print(ans)
#ans.delete()
n = 0
while(n < 0):
    a = Answer(question_id=n, title='blabla')
    
    #a.save()
    #a.delete()
    n=n+1

class Genre(models.Model):
    name = models.CharField(max_length=256)


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    STATUS_CHOICES = (
        ('m', 'Maintenance'),
        ('a', 'Available'),
        ('t', 'Taken'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    due_data = models.DateField(null=True, blank=True)


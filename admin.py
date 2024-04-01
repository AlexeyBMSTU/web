import django.contrib.admin 
from django.contrib import admin

# Register your models here.
from .models  import Author, Book, BookInstance, Genre, Question, Answer

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Question)
admin.site.register(Answer)


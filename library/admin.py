import django.contrib.admin 
from django.contrib import admin

# Register your models here.
from .models  import User1, Answer, Question, Tag, FeedBack


admin.site.register(Answer)
admin.site.register(User1)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(FeedBack)


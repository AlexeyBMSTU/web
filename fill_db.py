from django.contrib.auth.models import User
from django.db import models
from django.core.management.base import BaseCommand, CommandParser
# Register your models here.
from  library.models import  User1, Answer, Question, Tag, FeedBack, Test3

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arg', help='Something helpful')
    
    #help = 'run to me'

    def handle(self, *args, **kwargs):
        #print('pleeeese')
        print (kwargs['arg'])
        #users1 = User1(question_id=1, title='blabla') # ссылка по id
        #answers = Answer(question_id=2, title='blabla') # ссылка по id
        #questions = Question(question_id=2, title='blabla') # ссылка по id
        #tag = Tag(question_id=2, title='blabla') # ссылка по id
        #feedback = FeedBack(question_id=2, title='blabla') # ссылка по id
                       # Answer.objects.filter(question_id=1).delete()
                       # Answer.objects.filter(question_id=2).delete()
        temp = int(kwargs['arg'])
        
        #if temp == 0:
          #  print('Error')
            # for i in range(temp*200):
                # User1.objects.filter(question_id=i).delete()
                # Answer.objects.filter(question_id=i).delete()
                # Question.objects.filter(question_id=i).delete()
                # Tag.objects.filter(question_id=i).delete()
                # FeedBack.objects.all().delete()
        #else:

        for i in range(temp):
            users1 = User1(user_id=i, title='User') # ссылка по id
            users1.save()

        for i in range(temp*10):
            questions = Question(question_id=i, title='Question', text='How to open the Browser? Pleese') # ссылка по id
            questions.save()

        for i in range(temp*100):
            answers = Answer(answer_id=i, title='Answer', text='I am understand your problem...') # ссылка по id
            answers.save()

        for i in range(temp):
            tags = Tag(tag_id=i, title='Tag') # ссылка по id
            tags.save()

        for i in range(temp*200):
            feedback = FeedBack(feedback_id=i, title='FeedBack') # ссылка по id
            feedback.save()
        for i in range(temp*200):
            test = Test3(feedback_id=i, title='FeedBack') # ссылка по id
            test.save()
             



    #    match kwargs['arg']:
     #       case '10':
      #          for (int i = 0;)
       #     case 'clear':
        #        Answer.objects.filter(question_id=1).delete()
         #       Answer.objects.filter(question_id=2).delete()









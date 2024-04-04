from django.contrib.auth.models import User
from django.db import models
from django.core.management.base import BaseCommand, CommandParser
# Register your models here.
from  library.models import  User1, Answer, Question, Tag, FeedBack

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arg', help='Something helpful')
    
    #help = 'run to me'

    def handle(self, *args, **kwargs):
        #print('pleeeese')
        print (kwargs['arg'])

                       # Answer.objects.filter(question_id=1).delete()
                       # Answer.objects.filter(question_id=2).delete()
        temp = int(kwargs['arg'])
    
            # for i in range(temp*200):
                # User1.objects.filter(question_id=i).delete()
                # Answer.objects.filter(question_id=i).delete()
                # Question.objects.filter(question_id=i).delete()
                # Tag.objects.filter(question_id=i).delete()
                # FeedBack.objects.all().delete()


        for i in range(temp):
            #userID = User.objects.get(pk=i)
            users1 = User1(user_id=i, title='User') # ссылка по id
            users1.save()

        for i in range(temp*10):
            #u = User.objects.get(pk=i)
            questions = Question(question_id=i, title='Question', text='How to open the Browser? Pleese') # ссылка по id
            questions.save()

        for i in range(temp*100):
            #questionID = User.objects.get(pk=i)
            answers = Answer(answer_id=i, title='Answer', text='I am understand your problem...') # ссылка по id
            answers.save()

        for i in range(temp):
            #tagsID = User.objects.get(pk=i)
            tags = Tag(tag_id=i, title='Tag') # ссылка по id
            tags.save()
            #Tag.objects.bulk_create(tags)
        

        for i in range(temp*200):
            #feedbackRating = User.objects.get(pk=i)            
            feedback = FeedBack(feedback_id=i, title='FeedBack') # ссылка по id
            feedback.save()

             



    #    match kwargs['arg']:
     #       case '10':
      #          for (int i = 0;)
       #     case 'clear':
        #        Answer.objects.filter(question_id=1).delete()
         #       Answer.objects.filter(question_id=2).delete()









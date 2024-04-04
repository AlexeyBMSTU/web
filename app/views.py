from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from library.models import User1, Question, Answer, Tag, FeedBack, AuthorManager

# Create your views here.

questions = [
        {
               'id': i,
              'title': f'Question № {i}',
          'content': f'Long lorem ipsum {i}',
          'page_id': i+i+i+i
        }for i in range(1,30)
    ]

user = [{

    'id':i
} for i in range(1,10)
]

def paginate(objects, page, per_page=5):
    paginator = Paginator(objects, per_page)
   
    return paginator.page(page)

def index(request):
    
    page = request.GET.get('page', 1)
    return render(request, template_name='index.html', context={'questions': paginate(questions, page)})

def question(request, question_id):

    #posts = Question.objects.all()
    page = request.GET.get('page', 1)
    return render(request, template_name='question.html', context={'questions': paginate(questions, page)})

def ask(request):
    
    return render(request, template_name='ask.html')

def base(request):
    
    return render(request, template_name='base.html')

def signup(request):
    
    return render(request, template_name='signup.html')

def login(request):
    us = User1.objects.all()
    
    return render(request, template_name='login.html', context={'user': us.filter(user_id=2)})

def indextag(request):
    page = request.GET.get('page', 1)
    # return render(request, template_name='indextag.html', context={'question': paginate(questions, page=1), 'p1' : p1})
    return render(request, template_name='indextag.html', context={'questions': paginate(questions, page)})


def pageNotFound(request, exception):
    return render(request, template_name='404.html', status=404)
def handler500(request):
    return render(request, template_name='500.html', status=500)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
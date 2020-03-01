from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    myname = "Nguyen Manh Tien"
    taisan = ["dt","tivi"]
    contex = {"name": myname , "taisan": taisan}
    return render(request,"polls/index.html",contex)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"ds_quest": list_question}
    return render(request,"polls/question_list.html",context)

def detailView(request,Question_id):
    q = Question.objects.get(pk=Question_id)
    return render(request,"polls/detail_question.html",{"qs":q})

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk = data)
    except:
        HttpResponse('khoi khong co choice')
    c.vote = c.vote +1
    c.save()
    return render(request,"polls/resutl.html",{"q":q})

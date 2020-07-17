from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.


def say(require):
    return HttpResponse("Hello Dora, Welcome!")


def index(request):
    myname = "Dora"
    listname = ["Dora", "Uri", "Selina", "Shin", "Rowan", "Barry"]
    return render(request, "polls/index.html", {"name": myname, "listname": listname})


def viewquestion(request):
    list_question = Question.objects.all()
    context = {"dsname": list_question}
    return render(request, "polls/question.html", context)


def viewlist(request):
    list_question = Question.objects.all()
    content = {"listquestion": list_question}
    return render(request, "polls/detail.html", content)


def viewanswer(request):
    list_answer = Choice.objects.all()
    content = {"listanswer": list_answer}
    return render(request, 'polls/answer.html', content)


def detailView(request, question_id):
    c = get_list_or_404(Choice, question_id=question_id)
    print(c)
    q = Question.objects.get(pk=question_id)
    print(q)
    return render(request, 'polls/detail_question.html', {'as': c, 'qs': q})


def login(request):
    namepage = "Page Login"
    return render(request, 'polls/login.html', {"namepage": namepage})


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("You have to choose answer!!")
    c.votes = c.votes + 1
    c.save()
    return render(request, 'polls/result.html', {"result": q})

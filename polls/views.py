from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.utils import timezoneex
from .models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You are looking at results %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from webapp.models import Choice, Poll, Answer
from django.views.generic import View, TemplateView, RedirectView, FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode


class CreateAnswer(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        return render(request, 'create_answer', context={'choices': choice}, {'polls': poll})

    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        


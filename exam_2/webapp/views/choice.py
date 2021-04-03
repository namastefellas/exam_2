from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from webapp.models import Choice, Poll
from django.views.generic import View, TemplateView, RedirectView, FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import ChoiceForm

class ChoiceCreate(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse('details_poll', kwargs={'pk': self.kwargs.get('pk')})
    
    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        form.instance.poll = poll
        poll.save()
        return super().form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return context


class ChoiceEdit(UpdateView):
    form_class = ChoiceForm
    model = Choice
    template_name = 'choice/choice_update.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('details_poll', kwargs={'pk': self.object.poll.pk})


class ChoiceDelete(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse_lazy('details_poll', kwargs={'pk': self.object.poll.pk})
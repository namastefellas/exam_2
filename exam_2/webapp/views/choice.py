from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from webapp.models import Choice
from django.views.generic import View, TemplateView, RedirectView, FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode


class ChoiceCreate(CreateView):
    pass


class ChoiceEdit(UpdateView):
    pass


class ChoiceDelete(DeleteView):
    pass
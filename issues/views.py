# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class UserListView(TemplateView):
    template_name = 'userlist.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context


class UserDetailView(TemplateView):
    template_name = 'userdetail.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        return context


class IssueListView(TemplateView):
    template_name = 'issuelist.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        return context


class IssueDetailView(TemplateView):
    template_name = 'issuedetail.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        return context

from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from front.forms import ContactForm
from django.http import HttpResponse, Http404
import datetime

header_title = 'blef'
nav_menu = ['me', 'portfolio', 'resume', 'contact']


def index(request):
    index_context = {
        'header_title': header_title,
        'nav_menu': nav_menu,
        'active': 'home',
    }
    return render(request, "front/index.html", index_context)


class MeView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['header_title'] = header_title
        context['nav_menu'] = nav_menu
        context['active'] = 'me'

        return self.render_to_response(context)

    template_name = "front/me.html"

me_index = MeView.as_view()
me = me_index


class ContactView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['header_title'] = header_title
        context['nav_menu'] = nav_menu
        context['active'] = 'me'

        contact_form = ContactForm()
        context['form'] = contact_form

        return self.render_to_response(context)

    template_name = "front/contact.html"

contact_index = ContactView.as_view()
contact = contact_index


class ResumeView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['header_title'] = header_title
        context['nav_menu'] = nav_menu
        context['active'] = 'resume'

        return self.render_to_response(context)

    template_name = "front/resume.html"

resume_index = ResumeView.as_view()
resume = resume_index


class PortfolioView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['header_title'] = header_title
        context['nav_menu'] = nav_menu
        context['active'] = 'portfolio'

        return self.render_to_response(context)

    template_name = "front/portfolio.html"

portfolio_index = PortfolioView.as_view()
portfolio = portfolio_index
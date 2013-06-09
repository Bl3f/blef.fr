from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from front.forms import ContactForm
from django.http import HttpResponse, Http404
import datetime

header_title = 'blef'


def index(request):
    index_context = {
        'header_title': header_title,
        'nav_menu': ['home', 'experience', 'resume', 'contact'],
    }
    return render(request, "front/index.html", index_context)


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['header_title'] = header_title

        return self.render_to_response(context)

    template_name = "front/home.html"

home_index = HomeView.as_view()
home = home_index


class ContactView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['header_title'] = header_title

        contact_form = ContactForm()
        context['form'] = contact_form

        return self.render_to_response(context)

    template_name = "front/contact.html"

contact_index = ContactView.as_view()
contact = contact_index
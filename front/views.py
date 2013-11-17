from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from front.forms import ContactForm
from blefpointfr.settings.base import ADMINS

header_title = 'blef'
nav_menu = ['me', 'portfolio', 'resume', 'contact']


def index(request):
    index_context = {
        'header_title': header_title,
        'nav_menu': nav_menu,
        'active': 'home',
    }
    return render(request, "front/index.html", index_context)


def workip(request):
    context = []

    return render(request, "front/workip.html", context)


class BlefView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(BlefView, self).get_context_data()
        context['header_title'] = header_title
        context['nav_menu'] = nav_menu
        return context


class MeView(BlefView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['active'] = 'me'

        return self.render_to_response(context)

    template_name = "front/me.html"

me_index = MeView.as_view()
me = me_index


class ContactView(BlefView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['active'] = 'contact'

        contact_form = ContactForm()
        context['form'] = contact_form

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['active'] = 'contact'
        recipients = [mail for name, mail in ADMINS]

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(subject, message, email, recipients)

        else:
            contact_form = ContactForm(request.POST)
            context['form'] = contact_form

        return self.render_to_response(context)

    template_name = "front/contact.html"

contact_index = ContactView.as_view()
contact = contact_index


class ResumeView(BlefView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['active'] = 'resume'

        return self.render_to_response(context)

    template_name = "front/resume.html"

resume_index = ResumeView.as_view()
resume = resume_index


class PortfolioView(BlefView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['active'] = 'portfolio'

        return self.render_to_response(context)

    template_name = "front/portfolio.html"

portfolio_index = PortfolioView.as_view()
portfolio = portfolio_index
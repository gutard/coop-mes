# -*- coding: utf-8 -*-

from django.template import RequestContext
from ionyweb.website.rendering.utils import render_view
from django.contrib.auth.views import login, logout
from django.contrib.formtools.wizard.views import SessionWizardView
from .forms import AccountForm
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import get_current_site
from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect


# from ionyweb.website.rendering.medias import CSSMedia, JSMedia, JSAdminMedia
MEDIAS = (
    # App CSS
    # CSSMedia('page_account.css'),
    # App JS
    # JSMedia('page_account.js'),
    # Actions JSAdmin
    # JSAdminMedia('page_account_actions.js'),
    )

def index_view(request, page_app):
    return render_view('page_account/index.html',
                       { 'object': page_app },
                       MEDIAS,
                       context_instance=RequestContext(request))


def login_view(request, page_app):

    return login(request)


def login(request, template_name='page_account/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = '/'

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    return render_view(template_name,
        context,
        MEDIAS,
        context_instance=RequestContext(request))


def logout_view(request, page_app):

    return logout(request)


def inscription_view(request, page_app):

    return render_view('page_account/inscription.html',
        {},
        MEDIAS,
        context_instance=RequestContext(request))


inscription_forms = (
    ('account', AccountForm),
)

class InscriptionView(SessionWizardView):

    def get_template_names(self):
        return {
            'account': 'page_account/account.html'
        }[self.steps.current]

    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('/')

    def render_to_response(self, context, **response_kwargs):
        assert response_kwargs == {}
        return render_view(self.get_template_names(),
            context,
            MEDIAS,
            context_instance=RequestContext(self.request))

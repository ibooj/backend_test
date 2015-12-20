from django.views.generic.edit import FormView

from sms_handler.forms import SmsForm


class Home(FormView):
    template_name = 'index.html'
    form_class = SmsForm

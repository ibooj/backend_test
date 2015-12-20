import json
from django.views.generic.edit import FormView
from django.http import JsonResponse

from .forms import SmsForm
from .models import ApiLog
from sms_handler import get_handler


class SmsHandler(FormView):
    form_class = SmsForm

    @staticmethod
    def render_to_json_response(context, **response_kwargs):
        l = ApiLog(msg=json.dumps(context))
        l.save()
        response_kwargs['content_type'] = 'application/json'
        return JsonResponse(context, **response_kwargs)

    def form_valid(self, form):
        try:
            sms_handler = get_handler(self.kwargs.get('handler_name', None))
            context = sms_handler.send(**form.cleaned_data)
        except Exception as e:
            context = {'status': 'error', 'error_msg': e.message}
        return self.render_to_json_response(context)

    def form_invalid(self, form):
        return self.render_to_json_response(form.errors)

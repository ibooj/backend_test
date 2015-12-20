from django.conf.urls import url

from sms_handler.views import SmsHandler

urlpatterns = [
    url(r'^(?P<handler_name>[a-z_-]+)/message/$', SmsHandler.as_view(), name='sms_handler'),

]

# -*- coding: utf-8 -*-
from random import randint


class SomeApi(object):
    def send(self, *args, **kwargs):
        if randint(0, 9) % 2:
            response = {'status': 'ok', 'phone': '79149009900'}
        else:
            response = {'status': 'error', 'phone': '79149009900', 'error_code': '­3500',
                        'error_msg': u'Невозможно отправить сообщение указанному абоненту'}
        return response


class SuperApi(object):
    def send(self, *args, **kwargs):
        if randint(0, 9) % 2:
            response = {'status': 'ok', 'phone': '79149009900'}
        else:
            response = {'status': 'error', 'phone': '79149009900', 'error_code': '­3500',
                        'error_msg': u'Невозможно отправить сообщение указанному абоненту'}
        return response

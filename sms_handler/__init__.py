def get_handler(handler_name):
    module_parts = 'sms_handler.handlers'.split('.')
    module = __import__('.'.join(module_parts))
    for module_part in module_parts[1:]:
        module = getattr(module, module_part)
    return getattr(module, ''.join(map(lambda x: x.capitalize(), handler_name.split('-'))))()

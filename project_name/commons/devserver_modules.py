from devserver.modules import DevServerModule


class RequestModule(DevServerModule):
    logger_name = 'request'

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if hasattr(response, "template_name"):
            if not isinstance(response.template_name, basestring):
                for template in response.template_name:
                    self.logger.info('Request template:   %s' % template)
            else:
                self.logger.info('Request template:   %s' % response.template_name)

    def process_exception(self, request, exception):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        self.logger.info('Request function: %s' % self._translate_name(view_func))

    def process_init(self, request):
        pass

    def process_complete(self, request):
        pass

    def _translate_name(self, func):
        name = '<unknown>'

        if hasattr(func, '__name__'):
            name = func.__name__
        elif hasattr(func, '__class__') and hasattr(func.__class__, '__name__'):
            name = func.__class__.__name__

        if hasattr(func, '__module__'):
            module = func.__module__
            name = '%s.%s' % (module, name)

        return name


class LambdaBase(object):
    @classmethod
    def get_handler(cls, *args, **kwargs):
        def handler(event, context):
            return cls(*args, **kwargs).handle(event, context)
        return handler

    def handle(self, event, context):
raise NotImplementedError

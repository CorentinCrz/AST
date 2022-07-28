from providers.aws import Aws
from providers.gcp import Gcp


class Compiler:
    def __init__(self, parser, data, emitter):
        self.parser = parser
        self.data = data
        self.providers = {
            'aws': Aws(emitter),
            'gcp': Gcp(emitter),
        }

    def program(self):
        # self.parser.visit()
        for provider in self.data['providers']:
            data = self.data['providers'][provider]
            emitter = self.providers[provider]
            emitter.provider(data['region'], data.get('project'))

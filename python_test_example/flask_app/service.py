from random import randint

from .model import load_model

print('In service')

class Service:
    def __init__(self):
        print('Init Service')
        self.model = load_model()
        print(f'self.model: {self.model}')

    def predict(self, target: str):
        print('Call predict in service')
        return randint(0, 1000) / 1000.0

    def check_model(self):
        if self.model:
            return True
        return False

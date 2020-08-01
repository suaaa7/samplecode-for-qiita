from random import randint

print('In service')

class Service:
    def __init__(self):
        print('Init Service')

    def predict(self, target: str):
        print('Call predict in service')
        return randint(0, 1000) / 1000.0

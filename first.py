print(__name__)

def add(a, b):
    return a+b
def sub(a,b):
    return a-b

class BusinessCard:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("--------------------")
        print("Name: ", self.name)
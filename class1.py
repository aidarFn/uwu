class Hello:
    def __init__(self, a):
        self.a = a

class NewHello(Hello):
    def __str__(self):
        return 'Hi'

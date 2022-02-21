class Person:
    def __init__(self,fname):
        self.fname = fname

    def talk(self):
        print(f'Hi, I am {self.fname}')


jo = Person('joe hurrie')
jo.talk()
bob = Person('Bob collo')
bob.talk()
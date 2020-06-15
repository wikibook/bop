class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# 위의 두 줄은 Person('Swaroop').say_hi()라고 작성해도 됩니다

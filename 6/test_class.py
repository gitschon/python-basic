class Animal:
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        return 'mau'


class Dog(Animal):
    def voice(self):
        return 'gaw'


class Cow(Animal):
    def voice(self):
        return 'mu'


bobcat = Cat()
print(bobcat.voice())

bigdog = Dog()
print(bigdog.voice())

whitecow = Cow()
print(whitecow.voice())









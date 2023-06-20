class Animal:
    num_instances = 0

    def __init__(self):
        Animal.num_instances += 1

    def voice(self):
        pass

    @staticmethod
    def get_num_instances():
        return Animal.num_instances


class Cat(Animal):
    def voice(self):
        return 'mau'


class Dog(Animal):
    def voice(self):
        return 'gaw'


class Cow(Animal):
    def voice(self):
        return 'mu'

class Pig(Animal):
    def voice(self):
        return 'weee'


bobcat = Cat()
print(bobcat.voice())

bigdog = Dog()
print(bigdog.voice())

whitecow = Cow()
print(whitecow.voice())

bluepig = Pig()
print(bluepig.voice())

print(Animal.get_num_instances())










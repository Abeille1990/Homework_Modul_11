import inspect


class Plant:

    edible = False

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):

    edible = True

class Animal:

    def __init__ (self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food: Plant):
        if food.edible == True:
            print(f'{self.name} съел {food.name} и насытился.') and self.fed == True
        else: print(f'{self.name} не стал есть {food.name}') and self.alive == False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


def introspection_info(obj):

    alldata = dir(obj)
    fullattrs = vars(obj)
    attrs = list(fullattrs.keys())
    methods = []

    for n in alldata:
        if n not in attrs:
            methods.append(n)


    obj_info = {'type': (type(obj)), 'attrs': attrs, 'methods': methods,
                'module': inspect.getmodule(obj),
                'comments': inspect.getcomments(obj),
                'modul_check': inspect.ismodule(obj)}

    print(obj_info)

introspection_info(a1)
introspection_info(p2)

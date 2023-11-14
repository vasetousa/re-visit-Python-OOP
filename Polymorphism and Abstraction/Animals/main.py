from dog import Dog
from cat import Cat
from kitten import Kitten
from tomcat import Tomcat


if __name__ == '__main__':

    d = Dog("Pesho", 10, "male")
    print(d)
    print(d.make_sound())

    c = Cat("Masha", 16, 'female')
    print(c)
    print(c.make_sound())

    t = Tomcat("Shusho", 13)
    print(t)
    print(t.make_sound())

    k = Kitten("Buba", 5)
    print(k)
    print(k.make_sound())

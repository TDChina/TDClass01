# coding=utf8
# Copyright (c) 2017 CineUse


class Person(object):
    name = "baby"
    age = 0
    gender = "unknown"

    def __init__(self):
        print "Person is init..."

    def say_hi(self):
        print "hello, I am %s. I'm %s years old. My gender is %s." % (self.name, self.age, self.gender)


class Employee(Person):

    def __init__(self, name, age, gender):
        super(Employee, self).__init__()
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + str(self.age)

    def work(self):
        print "%s is working..." % self


class DJ(Person):

    def __init__(self, music="doo cii da cii..."):
        super(DJ, self).__init__()
        self.music = music

    def drop_the_beat(self):
        print "uha, let's get it..."
        print self.music


class CompanyDJ(Employee, DJ):

    def __init__(self, name, age, gender, music="Doo cii da cii"):
        super(CompanyDJ, self).__init__(name=name, age=age, gender=gender)

        self.music = music


person_1 = CompanyDJ("Aaron", 31, "male", "Lalalala")
person_1.say_hi()
person_1.work()
person_1.drop_the_beat()
print person_1
pass
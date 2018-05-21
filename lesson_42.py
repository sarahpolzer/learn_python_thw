#is-a versus has-a
#is-a: use is-a when you talk about objects and classes being related to
#each other by a class relationship
#has-a:when you talk about objects and classes that are related only
#because they reference one another

##Animal is-a object 
class Animal(object):
    pass
## Dog is-a Animal
class Dog(Animal):
     def __init___(self,name):
         # has a __init__ that takes self and name params
         self.name=name
## Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        # has a __init__ that takes self and name params
        self.name = name
##  Person is a object
class Person(object):
    def __init__(self,name):
        ## has-a init that takes self and name params
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## person has a salary
        self.salary=salary

## Fish is an object
class Fish(object):
    pass
## Salmon is a fish
class Salmon(Fish):
    pass
##Halibut is a fish
class Halibut(Fish):
    pass
## rover is-a Dog
rover=Dog("Rover")
## satan is a cat
satan=Cat("Satan")
##Mary is a person
mary=Person("Mary")
## Mary has a pet named satan
mary.pet = satan 
## Frank is an employee and has-an attribute name of Frank and attribute salary 
#of 120000
frank = Employee("Frank", 120000)
#Frank has a pet that is-a rover
frank.pet=rover
#flipper is a fish instance
flipper=Fish()
#crouse is a salmon instance
crouse = Salmon()
#harry is a halibut instance
harry=Halibut()
        

    


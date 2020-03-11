from abc import ABC, abstractmethod, abstractproperty

class myAbstractClass1(ABC):

    def __init__(self, personName):
        self.__personName = personName
        
    @property
    def personName(self):
        return self.__personName

    @abstractmethod
    def Greet(self) -> None:
        pass

    # python doesn't allow method overloading
    # def Greet(self, initialMessage):
    #     print(initialMessage + self.personName)

class myImplementedClass1(myAbstractClass1):

    def Greet(self) -> None:
        print("Hello " + self.personName)


if __name__ == "__main__":
    # can't instantiate class with abstract method
    #obj1 = myAbstractClass1("ram")
    obj2 = myImplementedClass1("shyam")
    #print(obj1.Greet())
    #print(obj1.Greet("kya haal hain "))

    obj2.Greet()
    # print(obj2.Greet())
    #print(obj2.Greet("kya haal hain "))

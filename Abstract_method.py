
from abc import ABC, abstractmethod
class Student(ABC):
    def name(self, name):
        print("Student Name: ",name)

    @abstractmethod
    def sport(self,name):
        pass

class studentSport(Student):

    def sport(self,name):
            print('Our student is ready to play {}!'.format(name))

obj = studentSport()
obj.name("Jesse")
obj.sport("Basketball")

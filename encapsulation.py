
# Base or Parent Class
class A:

    # Public method
    def method1(self):
        print("Public Method")
        
    # Protected method
    def _method1(self):
        print("Protected Method")

    # PRivate method
    def __method1(self):
        print("Private Method")

    
    def Help(self):
        self.method1()
        self._method1()
        self.__method1()

# object to call and display output of encapsulated methods
obj = A()
obj.Help()

            


    

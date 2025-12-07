# class employe:
#     def __init__(self, name, sallery, location):
        
#         self.name=name
#         self.sallery=sallery
#         self.location=location


# obj1=employe("Shubhasis",1500000,"INDIA")
# print(obj1.name,obj1.sallery,obj1.location)


class calculator :
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"The square  is {self.num*self.num}")
    def cube(self):
        print(f"The cube  is {self.num*self.num*self.num}")
    def rootsquare(self):
        print(f"The squareroot  is {self.num**1/2}")
    
  
                    
    
obj2=calculator(10)
obj2.square()
obj2.cube()
obj2.rootsquare()
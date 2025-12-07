# class demo:
#     a=4

    
# obj=demo  
# print(obj.a) 
# obj.a=1
# print(obj.a)


from random import randint
class Train:
 
    def __init__(self,trainno):
        self.trainno=trainno
    
    def book( self,fro, to ):
        print(f"The tran no {self.trainno} is running on time for {fro} to {to} ")
    def status(self):
        print(f"The train no {self.trainno} ticket is booked succesfully")
    def price(self,fro, to):
        print(f"The booking amount of tran no {self.trainno} {fro} to {to} is {randint(222 , 1000)}")

p=Train(22564)
p.book("kolkata","Newdelhi")
p.status()
p.price("kolkata","Newdelhi")


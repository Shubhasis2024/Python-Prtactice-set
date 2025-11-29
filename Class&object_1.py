class car:
    model="SUV"
    brand="Toyota"
    price="1200000"

    def fun(self ):
        print(f"The brand is{self.brand} and the price of car is {self.price}")

# fortuner=car()
# fortuner.name=(input("Enter car name :"))
# print(fortuner.name,fortuner.model,fortuner.price)

mycar=car()
mycar.brand=(input("Enter brand name"))
# print("brand name",mycar.brand)
# print(mycar.price)
mycar.fun()
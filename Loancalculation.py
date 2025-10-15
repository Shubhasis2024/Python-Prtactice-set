princpal_amount=int(input("Enter the main amount :"))
insterest=int(input("Enter interest rate:"))
time=int(input("Enter time duration :"))

total_interest=(princpal_amount*insterest*time)/100
print("Total insterest on principal :",total_interest)
pricipal_insterst=(princpal_amount+total_interest)
print("Total ammount is with intetest :",pricipal_insterst)

month=int(input("Enter emi months:"))
totalemi=pricipal_insterst/month
print("Your emi would be :",totalemi)

print("Your first emi will be :",totalemi)
secondemi=((pricipal_insterst-totalemi)/month)
print("Your second emi will be :",secondemi)
thridemi=((pricipal_insterst-secondemi)/month)
print("Your third emi will be :",thridemi)

# print("Your fourth emi will be :",)
# print("Your fifth emi will be :",)


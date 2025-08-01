#list is same like a array in python language and list are immutable 
Deatils=["Shubhasis,0125,Kolkata,Mumbai,2025,Whisky"]

print(Deatils[0])
Deatils[0]="Mr.Ghosh"
print(Deatils[0])
print(Deatils[0:4])#slicing in list 

Deatils.append("Beer")
print(Deatils)#Before sort print
Deatils.sort()
print(Deatils)# after sort function 
Deatils.reverse()#Reverse function 
print(Deatils)
Value=[10,20,30,40,50,100,200]
Value.insert(1,15)# insert data into list at any location of list 
print(Value)
Value.pop(1) #Pop one date from on list and print it another list 
print(Value)
# marks ={
#     "Name":"Shubh",
#     "place":"Kolkata",
#     "Dept":"QA_Automation",
#     10385:"Empcode",
#     "Package":3.6,
# }

# # print(type(marks))
# # print(marks["Name"],[10385],["Package"])
# # print(marks.keys())
# # print(marks.values())
# #  marks.update({"place":Mumbai})
# #  print(marks)

# print(marks.get("Name"))
# print(marks.get("Dept"))

# s=set()
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)
# data=int(input("Enter the number here :"))
# s.add(data)

# print(s)

s={}
data1=input("Enter name :")
data2=input("Enter languagr:")
s.update({data1:data2})
print(s)
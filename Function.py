# def AVG():
#     num1=float(input("Enter here no."))
#     num2=float(input("Enter here no."))
#     average=((num1+num2)/2)
#     print(average)

# AVG()

# def alert(name,ending):
#     print("Good Day ,"+  name +  ending)
#     return "ok"

# alert("Shubh","Thank you")
# alert("Raj","Thanks ")
# alert("Vicky","Thank you so much ")
# a=alert("Raj","Thanks ")
# print(a)

def alert2(name,ending="Thanks"):
    print(f"Good Day,{name},{ending}")

alert2("Tora","Thank you")
alert2("Sonu")
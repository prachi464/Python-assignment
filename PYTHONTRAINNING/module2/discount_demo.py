quantity=int(input("Enter the number of purchase"))
price=99
if quantity<10:
    print(" No discount")
elif quantity<20:
    dis=10/100
elif quantity<50:
    dis=20/100
elif quantity<100:
    dis=30/100
elif quantity>=100:
    dis=40/100
dis=dis*price
print("the amount of discount is:",dis)
total=price*quantity-dis
print("total amount after discount",total)
pocket=int(input("Enter the number of pocket"))
if pocket==0:
    print("Pocket is green")
if 1<=pocket<=10:
    if pocket%2==0:
        print("pockets are black")
    else :
        print("pockets are Red")
elif 11<=pocket<=18:
    if pocket%2==0:
        print("pockets are Red")
    else :
        print("pockets are Black")
elif 19<=pocket<=28:
    if pocket%2==0:
        print("pockets are black")
    else :
        print("pockets are Red")
elif 29<=pocket<=36:
    if pocket%2==0:
        print("pockets are Red")
    else :
        print("pockets are Black")
else :
    print("Error Occured")

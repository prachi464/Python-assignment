datastore={'office':{'medical':[
    {'room-number':100,'use':'reception','sq-ft':50,'price':75},
    {'room-number':101,'use':'waiting','sq-ft':250,'price':75},
    {'room-number':102,'use':'examination','sq-ft':125,'price':150},
    {'room-number':103,'use':'examination','sq-ft':125,'price':150},
    {'room-number':104,'use':'office','sq-ft':150,'price':100}]
    ,'parking':{'location':'premium','style':'covered','price':750}}}
def change_price(datastore):
    a=input("Enter amount that should be change:")
    r=int(input("enter room number"))
    for x in range(0,5):
        if r==datastore['office']['medical'][x]['room-number']:
            datastore['office']['medical'][x]['price']=a
            break
    print(datastore)
change_price(datastore)

def delrm(datastore):
    r=int(input("enter room number"))
    for x in range(0,5):
        if r==datastore['office']['medical'][x]['room-number']:
            del datastore['office']['medical'][x]
            break
    print(datastore)
delrm(datastore)
def add(datastore):
    r=int(input("enter thr room number"))
    s=input("enter use")
    t=int(input("enter sq-ft"))
    u=int(input("enter price"))
    for x in range(0,5):
        datastore['office']['medical'].append([{'room-number':r,'use':s,'sq-ft':t,'price':u}])
    print(datastore)
add(datastore)
    

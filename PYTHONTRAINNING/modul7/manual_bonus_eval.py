class contact:
   
    def __init__(self,name,phone_no,email):
        self.name=name
        self.phone_no=phone_no
        self.email=email
        print(name,phone_no,email)
        dict1={'name':name,'phone_no':phone_no,'email':email}
    def __repr__(self):
        return '%s,%s,%s' %(self.name,self.phone_no,self.email)
        
c1=contact('prachi','789789','hsdjkadh')
c2=contact('khdd','578637846','dhajkdh')
dict1={'1':c1,'2':c2}
print(dict1)
dict1={'1':c1,'2':c2}
def lookup():
    name=input("enter the ID")
    for i in dict1.keys():
        if name==i:
            print(dict1[i])
lookup()
def delete():
    name=input("enter the ID")
    for i in dict1.keys():
        if name==i:
            del dict1[i]
            print(dict1)
delete()
def change():
    name=input("enter the IDffff")
    for i in dict1.keys():
        if name==i:
            name=input("enter name")
            phoneno=input("enter phoneno")
            email=input("enter email")
            dict1[i]=name,phoneno,email
            print(dict1[i])
            print(dict1)
change()
        
        
        

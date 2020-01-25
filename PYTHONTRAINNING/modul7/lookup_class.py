class contact:
   
    def lookup(self,name,phone_no,email):
        self.name=name
        self.phone_no=phone_no
        self.email=email
        print(name,phone_no,email)

        name=input("enter your name")
        phone_no=input("enter your phone no")
        email=input("enter your email")
        dict1={'name':name,'phone_no':phone_no,'email':email}
        print(dict1)
def main():
    c=contact()
    c.lookup('prachi','75785678','bhjasgfa')

main()
        
        

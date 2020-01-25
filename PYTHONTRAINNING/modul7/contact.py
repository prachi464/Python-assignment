class contact:
    def __init__(self,name,phone_no,email):
        self.name=name
        self.phone_no=phone_no
        self.email=email
        print(name,phone_no,email)
    def _setname(self,name):
        self.name=name
    def _setphone_no(self,phone_no):
        self.phone_no=phone_no
    def _setemail(self,email):
        self.email=email
    def _getname(self):
        return self.name
    def _getphone_no(self):
        return self.phone_no
    def _getemail(self):
        return self.email
    def __str__(self):
        return self.name,self.phone_no,self.email
def main():
    c=contact('prachi','75785678','bhjasgfa')
    
    print("",c._getname())
    print("",c._getphone_no())
    print("",c._getemail())
    print(c.__str__())
main()
        
        
        
        
    

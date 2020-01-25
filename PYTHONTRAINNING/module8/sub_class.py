from Automobilee import Automobilee
class Car(Automobilee):
    def __init__(self,make,model,mileage,price,doors):
        self.__doors=doors
        Automobilee.__init__(self,make,model,mileage,price)
    def set_doors(self,doors):
        self.__doors=doors
    def get_doors(self):
        return self.__doors
class Truck(Automobilee):
    def __init__(self,make,model,mileage,price,drive_type):
        self.__drive_type=drive_type
        Automobilee.__init__(self,make,model,mileage,price)
    def set_drive_type(self,drive_type):
        self.__drive_type=drive_type
    def get_drive_type(self):
        return self.__drive_type
class SUV(Automobilee):
    def __init__(self,make,model,mileage,price,pass_cap):
        self.__pass_cap=pass_cap
        Automobilee.__init__(self,make,model,mileage,price)
    def set_pass_cap(self,pass_cap):
        self.__pass_cap=pass_cap
    def get_pass_cap(self):
        return self.__pass_cap
def main():
    c=Car('2000','ODI','56.000','770000','4')
    print("make",c.get_make())
    print("model",c.get_model())
    print("mileage",c.get_mileage())
    print("price",c.get_price())
    print("doors",c.get_doors())
    print('\n')
    t=Truck('20001','truck','88.99','777700','2')
    print("make",t.get_make())
    print("model",t.get_model())
    print("mileage",t.get_mileage())
    print("price",t.get_price())
    print("drivetype",t.get_drive_type())
    print('\n')
    s=SUV('2002','SUV','66.99','44000','2')
    print("make",s.get_make())
    print("model",s.get_model())
    print("mileage",s.get_mileage())
    print("price",s.get_price())
    print("passcap",s.get_pass_cap())
main()
    
        
        

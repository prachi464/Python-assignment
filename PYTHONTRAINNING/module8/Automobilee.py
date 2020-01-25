class Automobilee:
    def __init__(self,make,model,mileage,price):
        self.__make=make
        self.__model=model
        self.__mileage=mileage
        self.__price=price
    def set_make(self,make):
        self.__make=make
    def set_model(self,model):
        self.model=model
    def set_mileage(self,mileage):
        self.__mileage=mileage
    def set_price(self,price):
        self.__price=price
    def get_make(self):
        
        return self.__make
    def get_model(self):
        
        return self.__model
    def get_mileage(self):
        
        return self.__mileage
    def get_price(self):
        
        return self.__price
def main():
    a=Automobilee('55','5555','5555','7777')
    print("",a.get_make())
    print("",a.get_model())
    print("",a.get_mileage())
    print("",a.get_price())
main()
        

    
    

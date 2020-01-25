class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
        print(color,mileage)
    def __str__(self):
        return f'a{self.color}car'
c=Car('red',123)

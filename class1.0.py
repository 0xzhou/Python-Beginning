class Calculator_1:
    name='Casio'
    price=25
    def __init__(self,name,price,hight,width,weight): # constructor
        self.name=name
        self.price=price
        self.hight=hight
        self.width=width
        self.weight=weight
        self.add(1,1) # a indicator
    def add(self,x,y): # 'self'-keyword
        result=x+y
        print(result)
    def show(self):
        print(self.name,'\n',self.price)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x//y)

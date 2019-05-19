class Calculator:
    name='Casio'
    price=25
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

cal_1=Calculator() # create a new Calculator type
cal_1.show()
        

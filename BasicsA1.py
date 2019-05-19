for value in range(100):
    print(value)
# automatically change the line?

x=float( input("Please enter a number:"))
print("The square of that number is", x*x)

name=["Cleese","John"] #Lists are written with brackets and can (naturally) be nested
print(name[0],name[1]) # indexing
salaries=["$1000","$3000","$2221","$4000","$50000"]
print(salaries[0:4])   # slicing

person={'first name':"Mingyuan",'last name':"Zhou",'occupation':"student"} #Disctioneries are written with braces and elements aren't ordered
person['last name']="Guo" #indexing the element with key(name)
print(person)

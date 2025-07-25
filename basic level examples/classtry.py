class stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
obj=stud("Ram",'21')
obj.display()
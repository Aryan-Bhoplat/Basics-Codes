class car:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def display(self):
        print(f"Name:{self.name}\nCost:{self.cost}\n")
car1=car('Mercedes','1,73,00,000')
car2=car('BMW','1,82,00,000')
car3=car('Audi','1,32,00,000')

car1.display()
car2.display()
car3.display()
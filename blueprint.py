class Car():
    def __init__(self,model,color,company):
        self.model = model
        self.color = color
        self.company = company
    def start(self):
        print('started')
    def stop(self):
        print('stopped')
    def gear(self,geartype):
        print('gear changed')

audi = Car("C123","wine","Audi")
audi.start()
print("car details:")
print(audi.model)
print(audi.color)
print(audi.company)
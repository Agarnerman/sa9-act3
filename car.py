class Car:
	def __init__(self,make,model,color,price):
		self.make = make
		self.model = model
		self.color = color
		self.price = price
		self.mileage = 0
	def set_price(self,p):
		self.price = p
	def paint(self,c):
		self.color = c
	def show_car_info(self):
		print(f'Make: {self.make}\nModel: {self.model}\nColor: {self.color}\nPrice: ${self.price:g}\nMileage:{self.mileage:g} miles')
	def travel(self,distance):
		self.mileage = distance
		print(f'Car is travelling for {distance:g} miles')

car1 = Car('Porsche','718 Cayman GTS 4.0','Black',87400)
car2 = Car('Toyota','Corolla','Red',20075)

car1.show_car_info()
car2.show_car_info()
car1.paint('Gold')
car2.paint('White')
car1.travel(7500)
car2.travel(5000)
car1.set_price(77000)
car2.set_price(15000)
car1.show_car_info()
car2.show_car_info() 
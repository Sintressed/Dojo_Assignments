class car(object):
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print 'price: ' + str(self.price)
        print 'speed: ' + str(self.speed)
        print 'fuel: ' + str(self.fuel)
        print 'mileage: ' + str(self.mileage)
        print 'tax: ' + str(self.tax)
bugatti = car(11000000,'full',12,14).display_all()

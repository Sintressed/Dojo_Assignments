class product(object):
    def __init__(self,price,weight,name,brand,status):
        self.price = price
        self.weight = weight
        self.name = name
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = 'Sold'
        return self
    def add_tax(self):
        print self.price
        input_tax = raw_input("What is the tax?")
        self.price = self.price +(self.price * int(input_tax))
        print self.price
        return self
    def why_return(self):
        input_defected = raw_input("Is the item defective?")
        input_new = raw_input("Is the item still like new?")
        input_opened = raw_input("Has the product been opened")
        if input_defected == '1':
            self.price = 0
        elif input_new == '1':
            self.status = 'For Sale'
        elif input_opened == '1':
            self.status = 'Used'
            self.price = self.price - (self.price * .20)
        else:
            print 'no'
        return self
    def display_info(self):
        print 'price: ' + str(self.price)
        print 'weight: '+ str(self.weight)
        print 'name: ' + str(self.name)
        print 'brand: ' +str(self.brand)
        print 'status: ' + str(self.status)

mango = product(2,15,'Mango','butt','For Sale').why_return().display_info()

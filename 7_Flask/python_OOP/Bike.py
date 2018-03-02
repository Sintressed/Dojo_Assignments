class bike(object):
    print 'ran class'
    def __init__(self,price,maxs,miles):
        self.price = int(price)
        self.p = int(price)
        self.max_speed = int(maxs)
        self.miles = int(miles)
    def displayinfo(self):
        print 'price is ' + str(self.max_speed)
        print 'max speed it '+ str(self.max_speed)
        print ' Miles are '+ str(self.miles)
        return self
    def ride(self):
        print 'Riding'
        self.miles = self.miles + 10
        return self       
    def reverse(self):
        self.miles = self.miles - 10
        print self.p
        if self.miles < self.p:
            print 'lowest'
            self.miles = self.miles + 10
            print self.miles
        else:
            print 'stay the same'
            print self.miles
        return self


        


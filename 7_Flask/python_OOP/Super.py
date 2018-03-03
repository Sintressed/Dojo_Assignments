
class animal(object):
    def __init__(self,name):
        self.name = name
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print self.health
        return self
class dog(animal):
    def __init__(self,name):
        super(dog, self).__init__(name) 
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name)
        self.health = 170
    def display_health(self):
        print 'I am a dragon, my health is',super(dragon, self).display_health()
        return self
    def fly(self):
        self.health -= 10
        return self
class human(animal):
    def __init__(self,name):
        super(human, self).__init__(name)
        self.health = 150
    def display_health(self):
        super(human, self).display_health()
print dog('marley').walk().walk().walk().run().run().display_health()
print dragon('joey').fly().display_health()
print human('bob').display_health()


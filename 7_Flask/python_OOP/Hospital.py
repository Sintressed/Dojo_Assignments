class patient(object):
    count = 0
    def __init__(self,id,name,allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        patient.count +=1
        #print self.id,self.name,self.allergies,self.bed_number,patient.count
class hospital(object):
    def __init__(self,h_name,capacity):
        self.list = {}
        self.hospital = h_name
        self.capacity = capacity
        for count in range(0,capacity):
            self.list[count] = ''
        
    def admit(self,name):
        self.name = name
        #print self.list
        a = 0
        self.len = len(self.list)
        for x in range(0,self.len):
            #print len(self.list)
            #print x
            if self.list[x] == '':
                self.list[x] = self.name
                break
            else:
                a +=1
            if a == len(self.list):
                print 'hospital full'
                break
        #print self.list
        return self
    def discharge(self,name):
        for l in range(0,self.len):
            if self.list[l] == name:
                self.list[l] = ''
                print name, ' removed, bed ',l,' is now available'
                break
            else:
                print 'name not in database'
                break
        return self
    def show_list(self):
        print self.list
        return self

patient(1,'Joey','hayfever')
hospital('joesyburg hospital',3).admit('jane').admit('janna').discharge('jane').admit('hola').admit('hello').show_list()
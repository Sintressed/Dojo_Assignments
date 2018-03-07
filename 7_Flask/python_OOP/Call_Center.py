class call(object):
    def __init__(self,id,name,cell,time,reason):
        num = 0
        self.caller_id = id
        self.name = name
        self.phone_number = cell
        self.time = time
        self.reason = reason
        num += 1
    def display_all(self):
        print '*id:',self.caller_id,'*name:',self.name,'*phone number:',self.phone_number,'*time:',self.time,'*reason:',self.reason
        return self
class call_center(object):
    def __init__(self):
        self.list = []
        self.queue_size()
    def add_call(self,add):
        self.list.append(add)
    def queue_size(self):
        print len(self.list)
        return self
    def remove(self,remove):
        self.list.remove(remove)
        return self        
    def info(self):
        call.display_all()
call(12,'jessica',5097141984,'10:00','pregnant').display_all()
call_center().queue_size().info()


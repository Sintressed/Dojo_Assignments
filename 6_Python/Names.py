def part_1():
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    for count in range(0,4):
        print students[count]['first_name'],students[count]['last_name']
        continue
def part_2():
    print 'running part 2!'
    users = {
        'Students': [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }
    num = 0
    char = 0
    x = ''
    for star in range (0,2):
        #---------------------
        if star == 0:
            x = 'Students'
        elif star == 1:
            x = 'Instructors'
        #---------------------      
        for nul in range(0,len(users[x])):
            num = num + 1
            char = 0
            for ch in range(0,len(users[x][nul]['first_name'])):
                char = char + 1
                continue
            for ch in range(0,len(users[x][nul]['last_name'])):
                char = char + 1
                continue
            print num,'-',users[x][nul]['first_name'],users[x][nul]['last_name'],'-',char
#part_1()
part_2()
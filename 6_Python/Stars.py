#part 1 (not called)
def draw_stars():
    print 'running part 1'
    x = input()
    for count in range(0,len(x)):
        a = ''
        for ran in range(0,x[count]):
            a = a + '*'
            continue
        print a
#draw_stars()

#part 2(called)
def draw_stars1():
    print 'running part 2'
    x = input('insert a list please:  ')
    for count in range(0,len(x)):
        a = ''
        b = ''
        c = []
        if type(x[count]) == int:
            for ran in range(0,x[count]):
                a = a + '*'
                continue
            print a
        elif type(x[count]) == str:
            for ran in range(0,len(x[count])):
                char = (x[count])[0].lower() 
                b = b + char
                continue
            print b
draw_stars1()
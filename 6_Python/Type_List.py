l = input()
x = 0
y = 0
addNum = 0
addString = ''
def string():
    print 'this list is full of only strings!'
    print 'string: ', addString
def integer():
    print 'This List Is full of only Integers!'
    print 'sum',addNum
def neither():
    print 'You have entered a mixed list'
    print 'string: ',addString 
    print 'sum: ',addNum
for count in range(0,len(l)):
    if type(l[count]) == str and type(l[count]) != int:
        addString = addString +  ' ' + l[count] 
        x = x + 1
        y=y-1
    elif type(l[count]) == int and type(l[count])  != str:
        addNum = addNum + l[count]
        y = y + 1
        x=x-1
if x == len(l) and y != len(l):
        string()
elif y == len(l) and x != len(l):
        integer()
else:
    neither()

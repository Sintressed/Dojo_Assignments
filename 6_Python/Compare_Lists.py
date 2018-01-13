l1 = input('list one please! ')
l2 = input('list two please! ')
x = 0
for count in range(0,len(l1)):
    if len(l1) != len(l2):
        print 'list not same'
        break
    if l1[count] == l2[count]:
        x = x + 1
    else:
        print('list not same')
        break
if x == len(l1):
    print 'List was the same!'
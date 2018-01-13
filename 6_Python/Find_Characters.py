l = input('insert a word list')
char = input('insert a character')
x = ''
y = []
for count in range(0,len(l)):
    x = l[count]
    for element in range(0,len(x)):
        if x[element].find(char):
            continue
        else:
            y.append(l[count]) 
            break
            
print y
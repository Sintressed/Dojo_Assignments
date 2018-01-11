x = input()
print(type(x))
def yes():
    if x >= 100:
        print 'thats a big number!'
    elif x < 100:
        print 'thats a small number!'
        
def no():
        if len(x) >= 50:
            print 'Long Sentence'
        elif len(x) < 50:
            print 'Short Sentence'
def maybe():
    if len(x) >= 10:
        print 'Big List!'
    elif len(x) < 10:
        print 'Small List!'

if type(x) == int:
    yes()
elif type(x) == str:
    no()
elif type(x) == list:
    maybe() 


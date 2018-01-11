
#odd numbers from 1 to 1,000
for count in range(1,1000):
    if count % 2 != 0 :
        print count  
    
#multiples of 5 to 1,000
for multiple in range(5,1001):
    if multiple % 5 == 0:
        print multiple

#sum of all values in list
a = [1, 2, 5, 10, 255, 3]
print sum(a[0:6])

 # average of values in list 
b = [1, 2, 5, 10, 255, 3]
print (sum(b[0:6]) / len(b))
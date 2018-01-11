words = "It's thanksgiving day. It's my birthday,too!"
print str.replace(words,"day", "month")
a = [2,54,-2,7,12,98]
print  min(a),max(a)
b = ["hello",2,54,-2,7,12,98,"world"]
c = (b[0])
d = (b[len(b)-1])
print c,d
new_List = [c,d]
print new_List
e = [19,2,54,-2,7,12,98,32,10,-3,6]
e.sort()
f = (len(e)/2)
n_l = [e[0:f]] + e[f:]
print n_l
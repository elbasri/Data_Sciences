""" 
o1 = 0
o2 = 1
t1 = o1 + o2

o21 = 3
o22 = 3
t2 = o21 + o22

imp1 = 1 - (o1/t1)**2 - (o2/t1)**2
imp2 = 1 - (o21/t2)**2 - (o22/t2)**2

t = t1 + t2

totalimp = imp1 * t1/t + imp2 * t2/t """

#print(totalimp)



def totalimpurity(o1, o2, o21, o22):
    t1 = o1 + o2
    t2 = o21 + o22
    imp1 = 1 - (o1/t1)**2 - (o2/t1)**2
    imp2 = 1 - (o21/t2)**2 - (o22/t2)**2

    t = t1 + t2

    totalimp = imp1 * t1/t + imp2 * t2/t

    return totalimp

o1 = 0
o2 = 2
o21 = 3
o22 = 2
print(totalimpurity(o1, o2, o21, o22))

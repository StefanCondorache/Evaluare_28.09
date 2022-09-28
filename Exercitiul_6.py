import math
def triunghi():
    a=int(input('a= '))
    b=int(input('b= '))
    c=int(input('c= '))
    d=int(input('d= '))
    list2=[]
    if a+b>c and a+c>b and c+b>a and (a>0 and b>0 and c>0):
        sp1=(a+b+c)/2
        abc=True
        val1='perimetru abc= '+str(a+b+c)+' aria abc= '+str(math.sqrt(sp1*(sp1-a)*(sp1-b)*(sp1-c)))
        list2.append(val1)
    else:
        abc=False
        list2.append('nimic')
    if a+b>d and a+d>b and d+b>a and (a>0 and b>0 and d>0):
        sp2=(a+b+d)/2
        abd=True
        val2='perimetru abd= '+str(a+b+d)+' aria abd '+str(math.sqrt(sp2*(sp2-a)*(sp2-b)*(sp2-d)))
        list2.append(val2)
    else:
        abd=False
        list2.append('nimic')
    if a+d>c and a+c>d and c+d>a and (a>0 and d>0 and d>0):
        sp3=(a+d+c)/2
        adc=True
        val3='perimetru adc= '+str(a+d+c)+' aria adc '+str(math.sqrt(sp3*(sp3-a)*(sp3-d)*(sp3-c)))
        list2.append(val3)
    else:
        adc=False
        list2.append('nimic')
    if d+b>c and d+c>b and c+b>d and (d>0 and b>0 and d>0):
        sp4=(d+b+c)/2
        dbc=True
        val4='perimetru dbc= '+str(d+b+c)+' aria dbc '+str(math.sqrt(sp4*(sp4-d)*(sp4-b)*(sp4-c)))
        list2.append(val4)
    else:
        dbc=False
        list2.append('nimic')
    list1=[abc,abd,adc,dbc]
    valg=''
    for i,j in enumerate(list1):
        if j:
            valg+=list2[i]+'\n'
    return valg
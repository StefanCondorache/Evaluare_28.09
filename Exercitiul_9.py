import math
def inaltime():
    a=float(input('a: '))
    b=float(input('b: '))
    c=float(input('c: '))
    if a+b>c and a+c>b and c+b>a and (a>0 and b>0 and c>0):
        sp=(a+b+c)/2
        A=math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        ha=(2*A)/a
        hb=(2*A)/b
        hc=(2*A)/c
        return 'inaltimea a = ', ha,\
            'inaltimea b = ', hb,\
            'inaltimea c = ', hc
    else:
        return 'nu poate fi creat un triunghi'
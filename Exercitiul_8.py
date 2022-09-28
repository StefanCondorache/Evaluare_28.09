import math
def mediane():
    a=float(input('a: '))
    b=float(input('b: '))
    c=float(input('c: '))
    if a+b>c and a+c>b and c+b>a and (a>0 and b>0 and c>0):
        ma=0.5*math.sqrt(2*b**2+2*c**2-a**2)
        mb=0.5*math.sqrt(2*a**2+2*c**2-b**2)
        mc=0.5*math.sqrt(2*b**2+2*a**2-c**2)
        return 'mediana a = ',ma,\
            'mediana b = ',mb,\
            'mediana c = ',mc
    else:
       return 'nu poate fi creat un triunghi'
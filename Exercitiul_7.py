def calcul():
    def maxim(x,y):
        if x>=y:
            return x
        else:
            return y
    def minim(x,y):
        if x<=y:
            return x
        else:
            return y
    a1=float(input('a1: '))
    a2=float(input('a2: '))
    a3=float(input('a3: '))
    a4=float(input('a4: '))
    a5=float(input('a5: '))
    a6=float(input('a6: '))
    a7=float(input('a7: '))
    a8=float(input('a8: '))
    a9=float(input('a9: '))
    a10=float(input('a10: '))
    S=maxim(minim(a1,a2),maxim(a3,a4))+minim(maxim(a5,a6),minim(a7,a8))
    T=minim(a1,a2)+minim(a3,a4)+minim(a5,a6)+minim(a7,a8)+minim(a9,a10)+maxim(a1,a2)+maxim(a3,a4)+maxim(a5,a6)+maxim(a7,a8)+maxim(a9,a10)
    return 'suma S= ', S,\
        'suma T= ', T
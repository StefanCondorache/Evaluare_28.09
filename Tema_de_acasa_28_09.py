n = int(input('numar = '))
b = int(input('baza = '))
def verific(x,y):
    if y>0 and y<=9 and n>=0:
        for i in [int(j) for j in str(x)]:
            if i < y:
                val = True
            else:
                val = False
                print(x,'nu este scris corect in baza',y)
                break
        if val:
            print(x,'este scris corect in baza',y)
        return val
    else:
        print('baza nu apartine intervalului [1,9]')
        return False

def calcul():
    z = int(input('nr2 in baza aleasa = '))
    Suma,Diferenta_1,Diferenta_2,Produsul='','','',''
    list1=[]
    if z>=0 and verific(n,b) and verific(z,b):
        S=int(str(n),b)+int(str(z),b)
        P=int(str(n),b)*int(str(z),b)
        if int(str(n),b)>=int(str(z),b):
            Sc1=int(str(n),b)-int(str(z),b)
            while Sc1>0:
                list1.append(Sc1%b)
                Sc1//=b
            else:
                for i in list1[::-1]:
                    Diferenta_1+=str(i)
                Diferenta_1=int(Diferenta_1)
                list1=[]
        else:
            Sc2=int(str(z),b)-int(str(n),b)
            while Sc2>0:
                list1.append(Sc2%b)
                Sc2//=b
            else:
                for i in list1[::-1]:
                    Diferenta_2+=str(i)
                Diferenta_2=int(Diferenta_2)
                list1=[]
        while S>0:
            list1.append(S%b)
            S//=b
        else:
            for i in list1[::-1]:
                Suma+=str(i)
            Suma=int(Suma)
            list1=[]
        while P>0:
            list1.append(P%b)
            P//=b
        else:
            for i in list1[::-1]:
                Produsul+=str(i)
            Produsul=int(Produsul)
            list1=[]
        Raspuns=''
        Raspuns='suma = '+str(Suma)+'\n'+'scaderea nr1 = '+str(Diferenta_1)+'\n'+'scaderea nr2 = '+str(Diferenta_2)+'\n'+'produsul = '+str(Produsul)
        return Raspuns
    else:
        return 'nu au fost indeplinite cerintele'
    
print(verific(n,b))
print(calcul())
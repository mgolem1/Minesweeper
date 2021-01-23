##class PrikazIgre(object):
import random
global mine_values
global n
def prikaziPocetakIgre(self):
     print()
     print('='*19)
     print('*'*3+' MineSweeper '+'*'*3)
     print('='*19)
     print()
     print('''
MAIN MENU
*********
->Za instrukcije kako igrati igru, pritisnite tipku 'I'
-> Za početak igre, pritisnite tipku 'P'
''')

def PrikaziPolje():
    n=9
    mine_values=[[0for y in range(n)] for x in range(n)] 
    
 
    print()
    print("\t\t\tMINESWEEPER\n")
 
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)
 
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
         
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|") 
 
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
    print()
def postavi_mine():
    n=10
    broj_mina=10
    broj = [[0 for y in range(n)] for x in range(n)] 
    brojac=0
    while brojac<broj_mina:
        val=random.randint(0, n*n-1)
        r=val//n
        col=val%n
        if broj[r][col]!=-1:
            brojac=brojac+1
            broj[r][col]=-1
def postavi_vrijednosti():
    n=10
     
    numbers = [[0 for y in range(n)] for x in range(n)] 
    
 
    
    for r in range(n):
        for col in range(n):
 
            
            if numbers[r][col] == -1:
                continue
 
            # provjeri gore  
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # provjeri gore    
            if r < n-1  and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # provjeri ljevo
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r] = numbers[r] + 1
            # provjeri desno
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # provjeri gore-ljevo    
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # provjeri gore-desno
            if r > 0 and col < n-1 and numbers[r-1][col+1]== -1:
                numbers[r][col] = numbers[r][col] + 1
            # provjeri dolje-ljevo 
            if r < n-1 and col > 0 and numbers[r+1][col-1]== -1:
                numbers[r][col] = numbers[r][col] + 1
            # provjeri dolje-desno
            if r < n-1 and col< n-1 and numbers[r+1][col+1]==-1:
                numbers[r][col] = numbers[r][col] + 1

def Odabir():
    br=[x for x in range(1,10)]
    while True:
        odg=int(input('Odaberite brojeve polja (najprije stupac pa redak): '))
        if odg>99 or odg<11 :
            odg=int(input('Odaberite brojeve polja (najprije stupac pa redak): '))
        else:
            Odabran(odg[0],odg[1])

def lokacija(a,b,c):
    return c[a][b]

def Odabran(a,b):
    matrica=postavi_vrijednosti()
    v=lokacija(a,b,matrica)
    matrica[a][b]=v
    
    
    
   
prikaziPocetakIgre()
PrikaziPolje()
postavi_vrijednosti
postavi_mine()
    

    

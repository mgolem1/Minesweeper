import random, copy, replit

class Polje():
    
    def lokacija(r, c, b):
    return b[r][c]
    
    def postaviMine(b):
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        currentRow = b[r]
        if not currentRow[c] == '*':
            currentRow[c] = '*'
        else:
            Polje.postaviMine(b)

    def updateVrijednosti(rn,c,b):
        #Row above.
        if rn-1 > -1:
            r = b[rn-1]
        
            if c-1 > -1:
                if not r[c-1] == '*':
                    r[c-1] += 1

            if not r[c] == '*':
                r[c] += 1

            if 9 > c+1:
                if not r[c+1] == '*':
                    r[c+1] += 1

        #Same row.    
        r = b[rn]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

        #Row below.
        if 9 > rn+1:
            r = b[rn+1]

            if c-1 > -1:
                if not r[c-1] == '*':
                    r[c-1] += 1

            if not r[c] == '*':
                r[c] += 1

            if 9 > c+1:
                if not r[c+1] == '*':
                    r[c+1] += 1


    def nule(r,c,k,b):   
        #Row above
        if r-1 > -1:
            row = k[r-1]
            if c-1 > -1: row[c-1] = Polje.okacija(r-1, c-1, b)
            row[c] = Polje.lokacija(r-1, c, b)
            if 9 > c+1: row[c+1] = Polje.lokacija(r-1, c+1, b)

        #Same row
        row = k[r]
        if c-1 > -1: row[c-1] = Polje.lokacija(r, c-1, b)
        if 9 > c+1: row[c+1] = Polje.lokacija(r, c+1, b)

        #Row below
        if 9 > r+1:
            row = k[r+1]
            if c-1 > -1: row[c-1] = Polje.lokacija(r+1, c-1, b)
            row[c] = Polje.lokacija(r+1, c, b)
            if 9 > c+1: row[c+1] = Polje.lokacija(r+1, c+1, b)

    def provjeraNule(k,b,r,c):
        oldGrid = copy.deepcopy(k)
        Polje.nule(r, c, k, b)
        if oldGrid == k:
            return
        while True:
            oldGrid = copy.deepcopy(k)
            for x in range (9):
                for y in range (9):
                    if Polje.lokacija(x, y, k) == 0:
                        Polje.nule(x, y, k, b)
            if oldGrid == k:
                return

    def printPolje(b):
        replit.clear()
        print('    A   B   C   D   E   F   G   H   I')
        print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
        for r in range (0, 9):
            print(r,'║',Polje.lokacija(r,0,b),'║',Polje.lokacija(r,1,b),'║',Polje.lokacija(r,2,b),'║',Polje.lokacija(r,3,b),'║',Polje.lokacija(r,4,b),'║',Polje.lokacija(r,5,b),'║',Polje.lokacija(r,6,b),'║',Polje.lokacija(r,7,b),'║',Polje.lokacija(r,8,b),'║')
            if not r == 8:
                print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
        print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝') 
        
class Controller():
    
    def marker(r,c,k):
        k[r][c] = '°'
        Polje.printPolje(k)

    def odabir(b,k):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        while True:
            izbor = input('Izaberi kvadratić npr.F2 ili postavi minu npr. mE4: ').lower()
            if len(izbor) == 3 and izbor[0] == 'm' and izbor[1] in letters and izbor[2] in numbers:
                c, r = (ord(izbor[1]))-97, int(izbor[2])
                Controller.marker(r, c, k)
                Play.play(b,k)
                break
            elif len(izbor) == 2 and izbor[0] in letters and izbor[1] in numbers:
                return (ord(izbor[0]))-97, int(izbor[1])
            else:
                Controller.odabir(b,k)

class PrikazIgre():
    def igra():
        
        print()
        print('='*19)
        print('*'*3+' MineSweeper '+'*'*3)
        print('='*19)
        print()
        print('''
    
    ----------------------------------------
    -> Za upute igre, pritisnite tipku 'I'
    -> Za početak igre, pritisnite tipku 'P'
    ----------------------------------------
    
    ''')

        unos=input('Upiši ovdje: ').upper()
        if unos.upper()=='I':
            replit.clear()
            print(open('upute.txt','r').read())
            input('Stisni [enter] kad si spreman igrati. ')
        elif unos.upper()!='P':
            replit.clear()
            PrikazIgre.igra()

        b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        for n in range (0, 10):
            Polje.postaviMine(b)
        for r in range (0, 9):
            for c in range (0, 9):
                value = Polje.lokacija(r, c, b)
                if value == '*':
                    Polje.updateVrijednosti(r, c, b)

        Polje.printPolje(k)
        Play.play(b,k)
        
class Play():

    def play(b,k):
        c, r = Controller.odabir(b, k)
        v = Polje.lokacija(r, c, b)
        if v == '*':
            Polje.printPolje(b)
            print('Igra gotova!')
            opetigraj = input('Ponovo igraj? (D/N): ').lower()
            if opetigraj.lower() == 'd':
                replit.clear()
                PrikazIgre.igra()
            else:
                quit()
        k[r][c] = v
        if v == 0:
            Polje.provjeraNule(k, b, r, c)
        Polje.printPolje(k)
        ostatakKvadratica=0
        for x in range (0, 9):
            row = k[x]
            ostatakKvadratica += row.count(' ')
            ostatakKvadratica += row.count('°')
        if ostatakKvadratica == 10:
            Polje.printPolje(b)
            print('Pobjeda!')
            opetigraj = input('Ponovo igraj? (D/N): ')
            opetigraj = opetigraj.lower()
            if opetigraj == 'd':
                replit.clear()
                PrikazIgre.igra()
            else:
                quit()
        Play.play(b,k)

def main():
    PrikazIgre.igra()

main()

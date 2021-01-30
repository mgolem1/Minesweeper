import random, copy, replit

##b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
##k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#dohvacanje lokacije
def lokacija(r, c, b):
    return b[r][c]
##def postaviMine(b):
##        r = random.randint(0, 8)
##        c = random.randint(0, 8)
##        currentRow = b[r]
##        if not currentRow[c] == '*':
##            currentRow[c] = '*'
##        else:
##            postaviMine(b)
class Polje():

    
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
            if c-1 > -1: row[c-1] = lokacija(r-1, c-1, b)
            row[c] = lokacija(r-1, c, b)
            if 9 > c+1: row[c+1] = lokacija(r-1, c+1, b)

        #Same row
        row = k[r]
        if c-1 > -1: row[c-1] = lokacija(r, c-1, b)
        if 9 > c+1: row[c+1] = lokacija(r, c+1, b)

        #Row below
        if 9 > r+1:
            row = k[r+1]
            if c-1 > -1: row[c-1] = lokacija(r+1, c-1, b)
            row[c] = lokacija(r+1, c, b)
            if 9 > c+1: row[c+1] = lokacija(r+1, c+1, b)

    def provjeraNule(k,b,r,c):
        oldGrid = copy.deepcopy(k)
        Polje.nule(r, c, k, b)
        if oldGrid == k:
            return
        while True:
            oldGrid = copy.deepcopy(k)
            for x in range (9):
                for y in range (9):
                    if lokacija(x, y, k) == 0:
                        Polje.nule(x, y, k, b)
            if oldGrid == k:
                return

    def printPolje(b):
        replit.clear()
        print('    A   B   C   D   E   F   G   H   I')
        print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
        for r in range (0, 9):
            print(r,'║',lokacija(r,0,b),'║',lokacija(r,1,b),'║',lokacija(r,2,b),'║',lokacija(r,3,b),'║',lokacija(r,4,b),'║',lokacija(r,5,b),'║',lokacija(r,6,b),'║',lokacija(r,7,b),'║',lokacija(r,8,b),'║')
            if not r == 8:
                print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
        print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝') 

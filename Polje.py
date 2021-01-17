from kvadratic import Kvadratic
class Polje(object):
    def __init__(self):
        self.oznaceni_kvadratici=-1

    def stvori_polje(self):
        self.prvi_klik=True
        self.flagged_cells = 0
        self.otvoreni_kvadratici=0
        self.je_li_kraj_igre=False
        self.stop_igra=False
        self.field=[]
        
    def get_kvadratic(self,x,y):
        return self.field[x][y]
    
    def otvori_kvadratic(self,x,y):
        if not self.stop_igra:
            if(self.prvi_klik):
                self.prvi_klik=False
            kvadratic=self.get_kvadratic(x,y)
            zadnje_stanje=kvadratic.stanje
            kvadratic.otvoren()
            if(kvadratic.stanje=="otvoren" and zadnje_stanje != kvadratic.stanje):
                self.otvoreni_kvadratici+=1
                if not kvadratic.je_li_mina:
                    broj_mina=self.provjeri_susjede(kvadratic)
            if(kvadratic.stanje=="otvoren"):
                if(kvadratic.je_li_mina):
                    kvadratic.stanje=="otvoren"
                    self.je_li_kraj_igre=True
                    self.stop_igra=True
                else:
                    pass
    def provjeri_susjede(self, kvadratic):
	susjedne_mine = 0
	if susjedne_mine == 0:
        	self.otvori_susjede(kvadratic)
		pass
	return susjedne_mine

    
		

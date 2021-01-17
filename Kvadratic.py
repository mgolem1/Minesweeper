class Kvadratic(object):
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
        self.stanje="zatvoren"
        self.je_li_mina=False

    def otvoren(self):
        if(self.stanje!="oznaceno" and self.stanje!="otvoreno"):
            self.state="otvoreno"
            
    

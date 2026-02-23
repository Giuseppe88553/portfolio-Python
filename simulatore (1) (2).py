#2. Simulatore di Combattimento a Turni
#Descrizione:
#Due o più personaggi combattono a turni, con punti vita, attacchi speciali, difesa, ecc.
#Concetti usati:
#• Classi e oggetti
#• Strutture dati (liste, dizionari)
#• Logica di gioco
# Random (solo random è ok, fa parte della standard library)
#Espandibilità:
#Sistema di livelli, nemici controllati dal computer, strategie AI semplici.

class personaggio:
    def __init__(self,nome,attacco,difesa,puntivita):
        self.nome=nome
        self.attacco= attacco 
        self.difesa= difesa                  # quando e 0 è la massima quando è 1 è la minima
        self.puntivita= puntivita
    def attacca (self,avversario):
        avversario.puntivita-= self.attacco * avversario.difesa
        pass

class guerriero(personaggio):
    def __init__(self,nome):
        super().__init__(nome,20,0.3,100)
        

class arciere(personaggio):
    def __init__(self,nome):
        super().__init__(nome,70,0.6,100)
    
class gioco:
    def __init__(self):
        self.personaggi= []
        self.personaggi.append(guerriero("thor"))
        self.personaggi.append(arciere("robin hood"))
        self.personaggi.append(guerriero("capitan america"))
        self.personaggi.append(arciere("guglielmo tell"))
        pass
    def turno(self):
        for x in self.personaggi:
            
    def stampa_personaggi(self):
        print(self.personaggi)


      





g=guerriero()
a=arciere ()
g.attacca(a)
a.attacca(g)
print(g.puntivita)
print(a.puntivita)


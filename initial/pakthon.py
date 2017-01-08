"""
PAK GANERN

OOP as in Object-Oriented PakGanern
Pakthon este Python2 Edition choz

Andresito de Guzman
"""


class PakGanern:

    def __init__(self):
        self.ie = 'Pak'
        
    def PushMoYan(self, anoKasunod):
        print self.ie + " " + anoKasunod +  "!"

HetoNa = PakGanern()
HetoNa.PushMoYan('Ganern') # Prints "Pak Ganern!"

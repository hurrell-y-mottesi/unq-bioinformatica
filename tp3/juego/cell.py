# coding: utf-8
import pilasengine
import math
import random

class Cell(pilasengine.actores.Actor):
    def iniciar(self, virus, x, y, score=10):
        self.speed = 3
        self.x = x 
        self.y = y
        self.virus = virus
        self.imagen = "bacteria.png"
        self.escala = 0.05
        self.radio_de_colision = 10
        self.score = score
        self.limit_x = (pilas.obtener_area()[0] / 2) - 10
        self.limit_y = (pilas.obtener_area()[1] / 2) - 10
    
    def actualizar(self):
        distance = self.distance()
        if distance < 200 :
            self.scape()
        
        newPosition = self.x - self.speed
        if (-self.limit_x < newPosition ):
            self.x = newPosition
        newPosition = self.x + self.speed
        if (self.limit_x > newPosition ):
            self.x = newPosition
        newPosition = self.y + self.speed
        if (self.limit_y > newPosition ):
            self.y = newPosition
        newPosition = self.y - self.speed
        if (-self.limit_y < newPosition ):
            self.y = newPosition
        
    def scape(self):
        scapes = [self.scapeX, self.scapeY, self.privateScape ]
        random.choice(scapes)()
    
    def distance(self):
        x = self.virus.x
        y = self.virus.y
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
            
    def scapeX(self):
        x = self.virus.x
        self.x = self.x + self.speed if (x - self.x) < 0 else self.x - self.speed

    def scapeY(self):
        y = self.virus.y
        self.y = self.y + self.speed if (y - self.y) < 0 else self.y - self.speed
    
    def privateScape(self):
        self.scapeX()
        self.scapeY()
        
    def changePosition(self, x, y):
        self.x = x
        self.y = y
        
    def scale(self, number):
        self.escala = number
        self.radio_de_colision = self.radio_de_colision * number
        

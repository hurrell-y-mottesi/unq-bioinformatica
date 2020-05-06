# coding: utf-8
import pilasengine

class Virus(pilasengine.actores.Actor):

    def iniciar(self, speed=5, end = False):
        self.speed = speed
        self.imagen = "virus.png"
        self.radio_de_colision = 34
        self.escala= 0.14
        self.limit_x = (pilas.obtener_area()[0] / 2) - 10
        self.limit_y = (pilas.obtener_area()[1] / 2) - 10
        self.end = end
    
    def actualizar(self):
        if self.end:
            return
        if self.pilas.control.izquierda:
            newPosition = self.x - self.speed
            if (-self.limit_x < newPosition ):
                self.x = newPosition
                pilas.camara.x = self.x 
        if self.pilas.control.derecha:
            newPosition = self.x + self.speed
            if (self.limit_x > newPosition ):
                self.x = newPosition
                pilas.camara.x = self.x
        if self.pilas.control.arriba:
            newPosition = self.y + self.speed
            if (self.limit_y > newPosition ):
                self.y = newPosition
                pilas.camara.y = self.y
        if self.pilas.control.abajo:
            newPosition = self.y - self.speed
            if (-self.limit_y < newPosition ):
                self.y = newPosition
                pilas.camara.y = self.y

    def scale(self, number):
        self.escala = number
        self.radio_de_colision = self.radio_de_colision * number


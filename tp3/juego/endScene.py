# coding: utf-8
import pilasengine
import virus
import cell
import random

class EndScene(pilasengine.escenas.Escena):

    def iniciar(self, score= 0):
        self.score = score
        self.init_background()
        self.init_score()

    def init_background(self): 
        fondo = pilas.fondos.Fondo()
        fondo.imagen = pilas.imagenes.cargar('background-end.png')
        self.fondo = fondo
        
    def init_score(self):
        self.scoreText = pilas.actores.Texto("%s"%self.score, x= -15, y= 135)
        self.scoreText.definir_escala(2)
        
        button = pilas.interfaz.Boton("")
        button.imagen_normal = "button-base.png"
        button.imagen_sobre = "button-base.png"
        button.imagen_click = "button-base.png"
        button.definir_escala(1.5)
        button.definir_posicion(490, -88)
        button.conectar(self.goToMenu)
    
    def goToMenu(self):
        menu = pilas.escenas.MenuScene()
        menu.ejecutar()
    
    def ejecutar(self):
        pass
        
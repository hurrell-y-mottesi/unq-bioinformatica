# coding: utf-8
import pilasengine
import virus
import cell
import random

class GameScene(pilasengine.escenas.Escena):

    def iniciar(self, time=30, virusSpeed=3, amountOfCells=20):
        self.virusSpeed = virusSpeed
        self.time = time
        self.amountOfCells = amountOfCells
        self.score = 0
        self.cells = []        
        self.init_background()
        self.init_hud()

    def init_background(self): 
        fondo = pilas.fondos.Fondo()
        fondo.imagen = pilas.imagenes.cargar('background.png')
        pilas.camara.definir_escala(2)
        self.fondo = fondo
        
    def init_hud(self):
        self.scoreText = pilas.actores.Texto("Puntaje: %s"%self.score, x= -375, y= 330)
        self.scoreText.definir_ancho(300)
        self.scoreText.fijo = True
        self.textoTime = pilas.actores.Texto("Tiempo: %s"%self.time, x= 0, y=330)
        self.textoTime.fijo = True

    def removeCell(self, virus, cell):
        cell.eliminar()
        self.score += cell.score
        self.scoreText.texto = "Puntaje: %s"%self.score
        self.cells.append(Cell(pilas, virus=virus, x=random.randint(-499, 499), y=random.randint(-499, 499)))

    def ejecutar(self):
        self.virus = Virus(pilas, speed=self.virusSpeed)

        for i in range(0, self.amountOfCells):
            self.cells.append(Cell(pilas, virus=self.virus, x=random.randint(-499, 499), y=random.randint(-499, 499)))

        pilas.colisiones.agregar(self.virus, self.cells, self.removeCell)
        self.createTask()
        pass
        
    def finishGame(self):
        self.virus.end = True
        pilas.tareas.eliminar_todas()
        end = pilas.escenas.EndScene(score= self.score)
        end.ejecutar()

    def updateTime(self):
        self.time -= 1
        self.textoTime.texto = "Tiempo: %s"%self.time

    def createTask(self):
        pilas.tareas.una_vez(self.time, self.finishGame)
        pilas.tareas.siempre(1, self.updateTime)

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

class MenuScene(pilasengine.escenas.Escena):

    def agregarBaseNitrogenada(self, baseNitrogenada):
        if (len(self.codones) == 4):
            return
        self.codonActual += baseNitrogenada
        self.codonActualTexto.texto = "%s"%self.codonActual
        if (len(self.codonActual) == 3):
            if (self.existeCodon()):
                self.codones.append(self.codonActual)
                self.codonActual = ''
                self.primaraFormaText.texto = ' - '.join(self.codones)

    def agregarAdenina(self):
        self.agregarBaseNitrogenada('A')

    def agregarCitosina(self):
        self.agregarBaseNitrogenada('C')

    def agregarGuanina(self):
        self.agregarBaseNitrogenada('G')

    def agregarUracilo(self):
        self.agregarBaseNitrogenada('U')

    def existeCodon(self):
        return self.allCodones.has_key(self.codonActual)
        
    def init_background(self):
        fondo = pilas.fondos.Fondo()
        fondo.imagen = pilas.imagenes.cargar('menu.png')
        self.fondo = fondo

    def createButton(self, x, y, function, scale=1):
        button = pilas.interfaz.Boton("")
        button.imagen_normal = "button-base.png"
        button.imagen_sobre = "button-base.png"
        button.imagen_click = "button-base.png"
        button.definir_escala(scale)
        button.definir_posicion(x, y)
        button.conectar(function)

    def renderButtons(self):
        self.createButton(-430, 40, self.agregarAdenina)
        self.createButton(-200, 40, self.agregarCitosina)
        self.createButton(-430, -50, self.agregarGuanina)
        self.createButton(-200, -50, self.agregarUracilo)
        self.createButton(400, -280, self.play, 1.8)

    def iniciar(self):
        self.allCodones = {'UUU': { 'name': 'Phe', 'value': 'speed' }, 'UUC': { 'name': 'Phe', 'value': 'speed' }, 'UUA': { 'name': 'Leu', 'value': 'time' }, 'UUG': { 'name': 'Leu', 'value': 'time' }, 'UCU': { 'name': 'Ser', 'value': 'cell' }, 'UCC': { 'name': 'Ser', 'value': 'cell' }, 'UCA': { 'name': 'Ser', 'value': 'cell' }, 'UCG': { 'name': 'Ser', 'value': 'cell' }, 'UAU': { 'name': 'Tyr', 'value': 'speed' }, 'UAC': { 'name': 'Tyr', 'value': 'speed' }, 'UAA': { 'name': 'Stop', 'value': 'time' }, 'UAG': { 'name': 'Stop', 'value': 'time' }, 'UGU': { 'name': 'Cys', 'value': 'cell' }, 'UGC': { 'name': 'Cys', 'value': 'cell' }, 'UGA': { 'name': 'Stop', 'value': 'time' }, 'UGG': { 'name': 'Trp', 'value': 'speed' }, 'CUU': { 'name': 'Leu', 'value': 'time' }, 'CUC': { 'name': 'Leu', 'value': 'time' }, 'CUA': { 'name': 'Leu', 'value': 'time' }, 'CUG': { 'name': 'Leu', 'value': 'time' }, 'CCU': { 'name': 'Pro', 'value': 'time' }, 'CCC': { 'name': 'Pro', 'value': 'time' }, 'CCA': { 'name': 'Pro', 'value': 'time' }, 'CCG': { 'name': 'Pro', 'value': 'time' }, 'CAU': { 'name': 'His', 'value': 'cell' }, 'CAC': { 'name': 'His', 'value': 'cell' }, 'CAA': { 'name': 'Gln', 'value': 'speed' }, 'CAG': { 'name': 'Gln', 'value': 'speed' }, 'CGU': { 'name': 'Arg', 'value': 'time' }, 'CGC': { 'name': 'Arg', 'value': 'time' }, 'CGA': { 'name': 'Arg', 'value': 'time' }, 'CGG': { 'name': 'Arg', 'value': 'time' }, 'AUU': { 'name': 'Ile', 'value': 'cell' }, 'AUC': { 'name': 'Ile', 'value': 'cell' }, 'AUA': { 'name': 'Ile', 'value': 'cell' }, 'AUG': { 'name': 'Met', 'value': 'speed' }, 'ACU': { 'name': 'Thr', 'value': 'time' }, 'ACC': { 'name': 'Thr', 'value': 'time' }, 'ACA': { 'name': 'Thr', 'value': 'time' }, 'ACG': { 'name': 'Thr', 'value': 'time' }, 'AAU': { 'name': 'Asn', 'value': 'cell' }, 'AAC': { 'name': 'Asn', 'value': 'cell' }, 'AAA': { 'name': 'Lys', 'value': 'speed' }, 'AAG': { 'name': 'Lys', 'value': 'speed' }, 'AGU': { 'name': 'Ser', 'value': 'cell' }, 'AGC': { 'name': 'Ser', 'value': 'cell' }, 'AGA': { 'name': 'Arg', 'value': 'time' }, 'AGG': { 'name': 'Arg', 'value': 'time' }, 'GUU': { 'name': 'Val', 'value': 'time' }, 'GUC': { 'name': 'Val', 'value': 'time' }, 'GUA': { 'name': 'Val', 'value': 'time' }, 'GUG': { 'name': 'Val', 'value': 'time' }, 'GCU': { 'name': 'Ala', 'value': 'cell' }, 'GCC': { 'name': 'Ala', 'value': 'cell' }, 'GCA': { 'name': 'Ala', 'value': 'cell' }, 'GCG': { 'name': 'Ala', 'value': 'cell' }, 'GAU': { 'name': 'Asp', 'value': 'speed' }, 'GAC': { 'name': 'Asp', 'value': 'speed' }, 'GAA': { 'name': 'Glu', 'value': 'time' }, 'GAG': { 'name': 'Glu', 'value': 'time' }, 'GGU': { 'name': 'Gly', 'value': 'cell' }, 'GGC': { 'name': 'Gly', 'value': 'cell' }, 'GGA': { 'name': 'Gly', 'value': 'cell' }, 'GGG': { 'name': 'Gly', 'value': 'cell' }}
        self.codones = []
        self.codonActual = ''

        self.init_background()
        self.renderButtons()
        self.renderCodonActual()
        self.renderPrimeraForma()

    def calculateVirus(self, value):
          return len(filter(lambda elem: self.allCodones[elem]['value'] == value, self.codones))

    def play(self):
        print(self.calculateVirus('time') , self.calculateVirus('cell'), self.calculateVirus('speed') )
        time = self.calculateVirus('time') * 10 + 30
        amountOfCells = self.calculateVirus('cell') * 2 + 20
        virusSpeed = self.calculateVirus('speed') + 3
        gameScene = pilas.escenas.GameScene(time=time, amountOfCells=amountOfCells, virusSpeed=virusSpeed)
        gameScene.ejecutar()

    def renderCodonActual(self):
        self.codonActualTexto = pilas.actores.Texto("%s"%self.codonActual, x= -270, y= 140)

    def renderPrimeraForma(self):
        self.primaraFormaText = pilas.actores.Texto("", x= 365, y=65)
        self.primaraFormaText.definir_ancho(300)

    def ejecutar(self):
        pass

pilas = pilasengine.iniciar(ancho=1280, alto=720)

pilas.escenas.vincular(GameScene)
pilas.escenas.vincular(MenuScene)
pilas.escenas.vincular(EndScene)
gameScene = pilas.escenas.MenuScene()

gameScene.ejecutar()
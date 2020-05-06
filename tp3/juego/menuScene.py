# coding: utf-8
import pilasengine
import virus
import cell
import random

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
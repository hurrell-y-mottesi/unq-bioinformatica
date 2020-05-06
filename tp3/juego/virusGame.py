# coding: utf-8
import pilasengine
import gameScene
import menuScene
import endScene

pilas = pilasengine.iniciar(ancho=1280, alto=720)

pilas.escenas.vincular(GameScene)
pilas.escenas.vincular(MenuScene)
pilas.escenas.vincular(EndScene)
gameScene = pilas.escenas.MenuScene()

gameScene.ejecutar()

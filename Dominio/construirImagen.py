#!/usr/bin/python3
# -*- coding: utf-8 -*-

#pip install pillow

from PIL import Image
from Dominio.Cubo import Cubo
import Dominio.utils

dimension = 2 #Dimension del cubo NxN
padding = 20 #Tamaño de 'baldosa' y de separación

#Abrir imagenes para formar el cubo
img = Image.open('./res/FormarCubo/background.png')
img_yellow = Image.open('./res/FormarCubo/yellow.png')
img_orange = Image.open('./res/FormarCubo/orange.png')
img_green = Image.open('./res/FormarCubo/green.png')
img_white = Image.open('./res/FormarCubo/white.png')
img_blue = Image.open('./res/FormarCubo/blue.png')
img_red = Image.open('./res/FormarCubo/red.png')


def crearFondo(dimension, padding):
    ancho = padding * dimension * 2 +50
    largo = padding * dimension * 2+50
    img=Image.new('RGBA', (ancho,largo), (0,0,0,0))
    img.save('./res/FormarCubo/background.png')


def switch_caracter(caracter, posX, posY):
    if caracter == '0': img.paste(img_red, (posX,posY))
    if caracter == '1': img.paste(img_blue, (posX,posY))
    if caracter == '2': img.paste(img_yellow, (posX,posY))
    if caracter == '3': img.paste(img_green, (posX,posY))
    if caracter == '4': img.paste(img_orange, (posX,posY))
    if caracter == '5': img.paste(img_white, (posX,posY))


def construirCubo(dimension, padding, id):
    cubesize = (dimension*padding)
    cont = 0
    posY = 0
    posX = cubesize + padding
    posInicial= posX
    piezascara= dimension*dimension

    for caracter in id:
        switch_caracter(caracter, posX, posY)
        posX = posX+padding
        cont = cont+1

        if (cont%dimension) == 0:
            posX = posInicial
            posY= posY + padding
                        
        if cont == piezascara:
            posX = posInicial
            posY = cubesize + (int) (cubesize/2)
            posInicial = posX

        elif cont == (piezascara*2):
            posX = posInicial
            posY = posY + (int)(cubesize/2)

        elif cont==(piezascara*3):
            posX = 0
            posY = cubesize + (int) (cubesize/2)
            posInicial = posX

        elif cont == (piezascara*4):
            posX = cubesize*3
            posY = cubesize + (int) (cubesize/2)
            posInicial = posX
        
        elif cont==(piezascara*5):
            posX = cubesize*4 + (int) (cubesize/2)
            posY = cubesize + (int) (cubesize/2)
            posInicial = posX

    img.save('./' + Dominio.utils.PATHS.get('image_folder') + '/' + Dominio.utils.getTimestampedName('cuboFormado') + '.png')
    
    
def createImage(cubo):
    dimension = len(cubo.getCuboMatrix()[1])
    id = cubo.cuboToStr()
    crearFondo(dimension, padding)
    construirCubo(dimension, padding, id)


    
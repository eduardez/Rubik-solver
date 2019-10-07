#!/usr/bin/python3
# -*- coding: utf-8 -*-

#pip install pillow

from PIL import Image
from Cubo import Cubo
import utils

dimension = 3 #Dimension del cubo NxN
padding = 20 #Tamaño de 'baldosa' y de separación

#Abrir imagenes para formar el cubo
img = Image.open('./formarCubo/background.png')
img_yellow = Image.open('./formarCubo/yellow.png')
img_orange = Image.open('./formarCubo/orange.png')
img_green = Image.open('./formarCubo/green.png')
img_white = Image.open('./formarCubo/white.png')
img_blue = Image.open('./formarCubo/blue.png')
img_red = Image.open('./formarCubo/red.png')


def crearFondo(dimension, padding):
    ancho = padding * dimension * 5
    largo = padding * dimension * 4
    img=Image.new('RGBA', (ancho,largo), (0,0,0,0))
    img.save('./formarCubo/background.png')


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
            posY = posY + (cubesize*2)

        elif cont == (piezascara*2):
            posX = 0
            posY = cubesize + (int)(cubesize/2)
            posInicial = posX

        elif (cont%piezascara) == 0:
            posX = posX + cubesize + padding
            posY = posY-cubesize
            posInicial = posX
    img.save('./' + utils.PATHS.get('image_folder') + '/' + utils.getTimestampedName('cuboFormado') + '.png')
    
    
def createImage(cubo):
    dimension = len(cubo.getCuboMatrix()[1])
    id = cubo.cuboToStr()
    crearFondo(dimension, padding)
    construirCubo(dimension, padding, id)


    
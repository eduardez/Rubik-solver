#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install pillow
# pip install python-resize-image

from PIL import Image, ImageOps

import Dominio.utils
from Dominio.Cubo import Cubo


def construirCubo(dimension, padding, id, img, cubo):
    '''
    Posiciona la pieza en la imagen
    y, en función de su valor, la coloca en la imagen general. 
    Finalmente redimensiona la imagen y la guarda con el idHash del cubo.

    Argumentos:
        dimension: tamaño del cubo (n para un NxN)
        padding: tamaño constante. Es el tamaño de la pieza. 
                 Tambien se utiliza como medida de separación de caras.
        id: matriz del cubo puesto en forma de string para obtener los colores.
        img: imagen 'background' a la que se unen el resto de imagenes.
        cubo: objeto cubo actual.
    Returns:
        Nothing
    '''
    cubesize = (dimension*padding)
    cont = 0
    posY = padding
    posX = cubesize + (int)(cubesize/2) + padding
    posInicial = posX
    piezascara = dimension*dimension

    for caracter in id:
        switch_caracter(caracter, posX, posY, img)
        posX = posX+padding
        cont = cont+1

        if (cont % dimension) == 0:
            posX = posInicial
            posY = posY + padding

        if cont == piezascara:
            posX = posInicial
            posY = cubesize + (int)(cubesize/2)
            posInicial = posX

        elif cont == (piezascara*2):
            posX = posInicial
            posY = posY + padding*2

        elif cont == (piezascara*3):
            posX = padding*2
            posY = cubesize + (int)(cubesize/2)
            posInicial = posX

        elif cont == (piezascara*4):
            posX = cubesize*3
            posY = cubesize + (int)(cubesize/2)
            posInicial = posX

        elif cont == (piezascara*5):
            posX = cubesize*4 + padding*2
            #posX = cubesize*4 + (int)(cubesize/2)
            posY = cubesize + (int)(cubesize/2)
            posInicial = posX

    img = img.resize((600, 500))
    img.save('./' + Dominio.utils.PATHS.get('image_folder') +
             '/' + cubo.idHash + '.png')


def crearFondo(dimension, padding):
    '''
    Metodo que crea una imagen 'background' de un tamaño apropiado en función
    de la dimensión del cubo.

    Argumentos:
        dimension: tamaño del cubo (n para un NxN)
        padding: tamaño constante. Es el tamaño de la pieza. 
                 Tambien se utiliza como medida de separación de caras.
    Return:
        Nothing
    '''
    ancho = dimension*padding*6
    largo = dimension*padding*5
    img = Image.new('RGBA', (ancho, largo), (0, 0, 0, 0))
    img.save('./res/FormarCubo/background.png')
    img.close


def createImage(cubo):
    '''
    Método que genera un archivo .png con el cubo. El nombre de dicho archivo es el hash del estado generado.
    Argumentos:
        cubo: objeto cubo con el que vamos a trabajar para generar la imagen
    Return:
        Nothing
    '''
    dimension = len(cubo.getCuboMatrix()[1])
    id = cubo.cuboToStr()
    padding = 20
    crearFondo(dimension, padding)
    crearPiezas()
    img = Image.open('./res/FormarCubo/background.png')
    construirCubo(dimension, padding, id, img, cubo)

def crearPiezas():
    '''Crea las imagenes de las piezas en un tamaño 19x19 y de un color específico'''

    img = Image.new('RGBA', (19, 19), "red")
    img.save('./res/FormarCubo/red1.png')

    img = Image.new('RGBA', (19, 19), "blue") 
    img.save('./res/FormarCubo/blue.png')

    img = Image.new('RGBA', (19, 19), "white") 
    img.save('./res/FormarCubo/white.png')

    img = Image.new('RGBA', (19, 19), "green") 
    img.save('./res/FormarCubo/green.png')

    img = Image.new('RGBA', (19, 19), "orange") 
    img.save('./res/FormarCubo/orange.png')

    img = Image.new('RGBA', (19, 19), "yellow")
     
    img.save('./res/FormarCubo/yellow.png')


def switch_caracter(caracter, posX, posY, img):
    '''
    Metodo que incluye el color y la posicion correcta en la imagen 'background'
    Argumentos:
        caracter: posición del id que indica el color que se debe insertar
        posX: posición del eje X donde se tiene que insertar la pieza.
        posY: posición del eje Y donde se tiene que insertar la pieza.
        img: imagen en la que se inserta la pieza.
    Returns:
        Nothing
    '''
    img_yellow = Image.open('./res/FormarCubo/yellow.png')
    img_orange = Image.open('./res/FormarCubo/orange.png')
    img_green = Image.open('./res/FormarCubo/green.png')
    img_white = Image.open('./res/FormarCubo/white.png')
    img_blue = Image.open('./res/FormarCubo/blue.png')
    img_red = Image.open('./res/FormarCubo/red.png')

    if caracter == '0':
        img.paste(img_red, (posX, posY))
    if caracter == '1':
        img.paste(img_blue, (posX, posY))
    if caracter == '2':
        img.paste(img_yellow, (posX, posY))
    if caracter == '3':
        img.paste(img_green, (posX, posY))
    if caracter == '4':
        img.paste(img_orange, (posX, posY))
    if caracter == '5':
        img.paste(img_white, (posX, posY))

    img_yellow.close
    img_orange.close
    img_green.close
    img_white.close
    img_blue.close
    img_red.close

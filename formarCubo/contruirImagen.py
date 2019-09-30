#!/usr/bin/python3
# -*- coding: utf-8 -*-

#pip install pillow

from PIL import Image

img=Image.new('RGBA', (800,400), "black")
img.save('./formarCubo/background.png')
img_back= Image.open('./formarCubo/background.png')

img = Image.new('RGBA', (20, 20), "red") 
img.save('./formarCubo/red.png')
img_red= Image.open('./formarCubo/red.png')

img = Image.new('RGBA', (20, 20), "blue") 
img.save('./formarCubo/blue.png')
img_blue= Image.open('./formarCubo/blue.png')

img = Image.new('RGBA', (20, 20), "white") 
img.save('./formarCubo/white.png')
img_white= Image.open('./formarCubo/white.png')

img = Image.new('RGBA', (20, 20), "green") 
img.save('./formarCubo/green.png')
img_green= Image.open('./formarCubo/green.png')

img = Image.new('RGBA', (20, 20), "orange") 
img.save('./formarCubo/orange.png')
img_orange= Image.open('./formarCubo/orange.png')

img = Image.new('RGBA', (20, 20), "yellow") 
img.save('./formarCubo/yellow.png')
img_yellow= Image.open('./formarCubo/yellow.png')


img= Image.open('./formarCubo/background.png')
img_red = Image.open('./formarCubo/red.png')
img_blue = Image.open('./formarCubo/blue.png')

# ##(Vertical, Horizontal)
dimension=3
cubesize = (dimension*20)
posY = 0
posX = cubesize +50 
cont = 0
posInicial= posX
piezascara= dimension*dimension
id='113412431243356312154351123465621234531421541223123456'

def switch_caracter(caracter):
    if caracter == '1': img.paste(img_blue, (posX,posY))
    if caracter == '2': img.paste(img_yellow, (posX,posY))
    if caracter == '3': img.paste(img_green, (posX,posY))
    if caracter == '4': img.paste(img_orange, (posX,posY))
    if caracter == '5': img.paste(img_white, (posX,posY))
    if caracter == '6': img.paste(img_red, (posX,posY))

for caracter in id:
    switch_caracter(caracter)
    posX = posX+21
    cont = cont+1
    if (cont%dimension) == 0:
        posX = posInicial
        posY= posY + 21
    if cont == piezascara:
        posX = posInicial
        posY = posY + (cubesize*2)
    if cont == (piezascara*2):
        posX = 0
        posY = cubesize+30
        posInicial = posX

    #!Este elif falla.
    elif (cont%piezascara) == 0:
        posX = posX + cubesize +20
        posY = posY-cubesize
        posInicial = posX

img.save('./formarCubo/CuboFormado.png')
    


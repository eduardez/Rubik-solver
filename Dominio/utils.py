#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json, datetime
from pprint import pprint

PATHS = {
    'json_folder' : './res/json_files/',
    'image_folder' : './res/img_cubes/'
}

# --------------- Utils generar cubos ------------------
def generarCubo(tam):
    pass


# --------------- Utils generales ------------------
def getTimestampedName(name):
    td = datetime.datetime.now().strftime("[%H-%M-%S.%f")[:-2]
    td += ']'
    return td + name 


def createFolder(name):
    """Crea una carpeta (si no existe) para contener
    todos los archivos JSON generados.

    Argumentos:
        Nothing
    Returns:
        Nothing   
    """
    try:
        os.makedirs(name)
    except FileExistsError:
        pass


def emptyFolder(name):
    for arch in os.listdir(name):
        ruta = os.path.join(name, arch)
        try:
            if os.path.isfile(ruta):
                os.unlink(ruta)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

# --------------- Utils de los archivos JSON ------------------
def jsonRead(path):
    """Abre un archivo JSON y devuelve los datos del archivo.

    Argumentos:
        path (str): Ruta relativa hacia el archivo.
    Returns:
        data (Any): Datos contenidos en el JSON.   
    """
    with open(path) as json_file:
        try:
            data = json.load(json_file)
            #pprint(data)
            return data
        except FileNotFoundError:
            print('\nArchivo JSON no encontrado.')

    
def jsonWrite(name, json_data):
    """Escribe un archivo JSON en la carpeta json_files.

    Argumentos:
        name (str): Nombre del archivo,
        json_data (Any): Datos del archivo JSON.
    Returns:
        Nothing.   
    """
    with open(PATHS.get('json_folder') + getTimestampedName(name) + '.json', 'w') as salida:
        salida.write(getJSONConFormato(json_data))


def getJSONConFormato(json):
    """Prettify para JSON. Da un formato bonito para
    luego escribirlo en los ficheros JSON escritos
    por el programa.

    Argumentos:
        json (str): Datos del archivo JSON.
    Returns:
        formatted_json (str): Datos formateados del archivo JSON.   
    """
    formatted_json= '{'
    for caras in json:
        formatted_json += '\n"' + caras +'":['
        for stick in json[caras]:
            formatted_json += str(stick) + ','
        formatted_json = formatted_json[:-1]
        formatted_json += '],'
    formatted_json = formatted_json[:-1]
    formatted_json += '\n}'
    return(formatted_json)




from ctypes.wintypes import HHOOK
from encodings import normalize_encoding
import json
from datetime import datetime
from email.encoders import encode_noop
from gettext import install
import json
from msilib import type_string
from operator import ixor	
import os
from pprint import pp, pprint
from re import X
from sqlite3 import Cursor
from time import sleep
from tkinter import CENTER
from traceback import print_list
import turtle
from unittest import registerResult
from xml.dom.minidom import Element


preguntas = [
   {
    "Pregunta: ": "¿En que año se hundio el Titanic?",
    "Estas en el escalon numero: ": 1,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A:": 1592,
        "Opcion B:": 1912,
        "Opcion C:": 2001,
        "Opcion D:": 2000
    },
    "Opcion_correcta": "B"
},{
    "Pregunta: ": "¿Cual es la capital de Portugal?",
    "Estas en el escalon numero: ": 2,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A:": "Madrid",
        "Opcion B:": "Lisboa",
        "Opcion C:": "Copenhaugue",
        "Opcion D:": "Portugal"
    },
    "Opcion_correcta": "B"
},{
    "Pregunta: ": "¿Cual es el símbolo químico de la Plata?",
    "Estas en el escalon numero: ": 3,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A:": "Cu",
        "Opcion B:": "Ag",
        "Opcion C:": "Mg",
        "Opcion D:": "Pl"
    },
    "Opcion_correcta": "B"
},{
    "Pregunta: ": "¿Cuántas franjas tiene la bandera de Estados Unidos?",
    "Estas en el escalon numero: ": 4,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A": 20,
        "Opcion B": 15,
        "Opcion C": 13,
        "Opcion D": 16
    },
    "Opcion_correcta": "C"
},{
    "Pregunta: ": "¿Cuántos días le toma a la tierra dar una vuelta a la órbita del sol?",
    "Estas en el escalon numero: ": 5,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A:": 365,
        "Opcion B:": 200,
        "Opcion C:": 30,
        "Opcion D:": 1
    },
    "Opcion_correcta": "A"
},{
    "Pregunta: ": "¿Cuál es el país más pequeño del mundo?",
    "Estas en el escalon numero:  ": 6,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A:": "Andorra",
        "Opcion B:": "Vaticano",
        "Opcion C:": "Chipre",
        "Opcion D:": "Belice"
    },
    "Opcion_correcta": "B"
},{
    "Pregunta: ": "¿Cuál es el río más largo del mundo?",
    "Estas en el escalon numero: ": 7,
    "Puntaje: ": 10,
    "Respuestas: ": {
        "Opcion A:": "Tamesis",
        "Opcion B:": "Rio de la Plata",
        "Opcion C:": "Nilo",
        "Opcion D:": "Amazonas"
    },
    "Opcion_correcta": "C"
},{

    "Pregunta: ": "¿Qué conductor de la Formula 1 ha ganado más campeonatos?",
    "Estas en el escalon numero:  ": 8,
    "Puntaje: ": 5,
    "Respuestas: ": {
        "Opcion A:": "Michael Schumacher",
        "Opcion B:": "Ayrton Senna",
        "Opcion C:": "Carlos Reutemann",
        "Opcion D:": "Lewis Hamilton"
    },
    "Opcion_correcta": "D"
},{
    "Pregunta: ": "¿Cuántas respiraciones toma el cuerpo humano diariamente?",
    "Estas en el escalon numero: ": 8,
    "Puntaje: ": 5,
    "Respuestas: ": {
        "Opcion A:": 26000,
        "Opcion B:": 20000,
        "Opcion C:": 21000,
        "Opcion D:": 30000
    },
    "Opcion_correcta": "C"
},{
    "Pregunta: ": "¿Dónde se celebraron los primeros Juegos Olímpicos modernos?",
    "Estas en el escalon numero: ": 8,
    "Puntaje: ": 5,
    "Respuestas: ": {
        "Opcion A:": "Atenas",
        "Opcion B:": "Babilonia",
        "Opcion C:": "Egipto",
        "Opcion D:": "Turquía"
        },
    "Opcion_correcta": "A"
},{
    "Pregunta: ": "¿Qué cantante fue conocido, entre otras cosas, como El rey del pop?",
    "Estas en el escalon numero: ": 8,
    "Puntaje: ": 5,
    "Respuestas: ": {
        "Opcion A:": "Michael Jackson",
        "Opcion B:": "Bob Dylan",
        "Opcion C:": "Bb E King",
        "Opcion D:": "Elton Jhon"
    },
    "Opcion_correcta": "A"
}
]

#registro_partidas=[]
#with open('Preguntas.json', 'w', encoding="utf-8") as f:
   # json.dump(preguntas, f,ensure_ascii=False)

#with open('Registro_partidas.json', 'w',encoding="utf-8") as file:
   # json.dump(registro_partidas, file,ensure_ascii=False)


def leer_archivo(nombre_archivo):
    obj_archivo=open(nombre_archivo,'rt',encoding='utf-8')

    str_contenido = obj_archivo.read()
    res=json.loads(str_contenido)

    obj_archivo.close()

    return res
    
def d_print_sorted(respuestas):
    for c in sorted(respuestas):
        print("\033[0;30;47m",c,respuestas[c],'\033[0;m')

def preguntas_y_respuestas(numero_escalon,i):
    print("\033[0;30;46m","Estas en el escalon numero ", i , " la pregunta es:","\033[0;m")
    escalones=leer_archivo("Preguntas.json")
    pregunta=escalones[numero_escalon]["Pregunta: "]
    print("\033[0;33m",pregunta,'\033[0;m')
    d_print_sorted(escalones[numero_escalon]["Respuestas: "])

def preguntas_y_respuestas_ultimo_escalon(numero_escalon,i):
    escalones=leer_archivo("Preguntas.json")
    pregunta=escalones[numero_escalon]["Pregunta: "]
    print("\033[0;33m",pregunta,'\033[0;m')
    d_print_sorted(escalones[numero_escalon]["Respuestas: "])

def respuesta_correcta(numero_escalon,respuesta): 
    escalones=leer_archivo("Preguntas.json")
    return respuesta in escalones[numero_escalon]["Opcion_correcta"]

def puntaje_jugador(numero_escalon,puntaje):
    escalones=leer_archivo("Preguntas.json")
    puntaje=int(puntaje+escalones[numero_escalon]["Puntaje: "])
    return puntaje

def guardar_archivo(nombre_archivo, lista):
    obj_archivo = open(nombre_archivo, 'w', encoding='utf-8')
    
    str_contenido_a_guardar = json.dumps(lista,ensure_ascii=False)
    obj_archivo.write(str_contenido_a_guardar)
    
    obj_archivo.close()

def carga_de_datos():
    numero_escalon=int(input("Ingrese el numero de escalon que quiera modificar la pregunta: "))
    numero_escalon-=1
    nueva_pregunta_usuario=str((input("Ingrese la nueva pregunta: ")))
    opcionA_usuario=str(input("Ingrese la opcion A: "))
    opcionB_usuario=str(input("Ingrese la opcion B: "))
    opcionC_usuario=str(input("Ingrese la opcion C: "))
    opcionD_usuario=str(input("Ingrese la opcion D: "))    
    opcion_correcta_usuario=str(input("Ingrese la opcion correcta : "))
    preguntas[numero_escalon].update({
        "Pregunta: ": nueva_pregunta_usuario,
        "Respuestas: ": {
            "Opcion A:": opcionA_usuario,
            "Opcion B:": opcionB_usuario,
            "Opcion C:": opcionC_usuario,
            "Opcion D:": opcionD_usuario
        },
        "Opcion_correcta": opcion_correcta_usuario 
    })
    guardar_archivo("Preguntas.json",preguntas)
    escalones=leer_archivo("Preguntas.json")
    d_print_sorted(escalones[numero_escalon])
    with open('Preguntas.json', 'w', encoding="utf-8") as f:
        json.dump(preguntas, f,ensure_ascii=False)
    
def abrir_archivo(nombre_archivo):
    obj_archivo = open(nombre_archivo, 'rt', encoding='utf-8')
    str_contenido = obj_archivo.read()
    res = json.loads(str_contenido)
    obj_archivo.close()
    return res

def nombre_correcto(numero,nombre):
    lista=leer_archivo("Registro_partidas.json")
    return nombre in lista[numero]["Nombre del jugador: "]

def fecha_correcta(numero,fecha):
    lista=leer_archivo("Registro_partidas.json")
    return fecha in lista[numero]["Fecha y hora: "]

Puntaje=int()
os.system("cls")
print("\033[0;30;43m","Bienvenido al juego de Los 8 escalones de la Programación.",'\033[0;m',"\n","\n")
print("\033[1;33m","Elija el modo que desea: ",'\033[0;m',"\n")
print("\033[0;30;47m","1 - Carga de Datos","\n","2 - Jugar","\n","3 - Consultas",'\033[0;m',"\n")
opcion=int(input("\033[4;35m"+"Elija la opcion que desea ingresando el numero correspondiente:"+'\033[0;m'))
os.system("cls")
lista_opciones=[]
lista_opciones_verdaderas=[]
lista_preguntas=[]

if opcion == 1:
    print("\033[0;30;43m","MODO CARGA DE DATOS",'\033[0;m',"\n")
    carga_de_datos()

elif opcion==2:

    #numero_jugador=int(input("Ingrese su numero de jugador: "))
    nombre=str(input("\033[4;35m"+"Ingrese su nombre para registrarlo como jugador: "+'\033[0;m'))
    fecha_hora=str(input("\033[4;35m"+"Ingrese la fecha de hoy en el siguiente formato (dia/mes/año/hora/minutos): "+'\033[0;m'))
    #fecha=datetime.strptime(fecha_hora,"%d/%m/%Y/%H/%M")

    os.system("cls")


    print("\033[0;30;43m","MODO JUGAR",'\033[0;m',"\n")
    print("\033[0;32m","PERFECTO! EMPECEMOS EL JUEGO",'\033[0;m')
    sleep(1)
    print("\033[0;32m","3",'\033[0;m')
    sleep(1)
    print("\033[0;32m","2",'\033[0;m')
    sleep(1)
    print("\033[0;32m","1",'\033[0;m')
    sleep(1)

    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("black")
    texto.penup()
    texto.hideturtle()
    texto.write("Puntaje: 0"    ,   align ="center", font = ["Courier", 24, "normal"])
    Puntaje= 0
    i= 0
    numero_escalon= 0
    Puntaje=int()

    escalones=leer_archivo("Preguntas.json")
    while i < 7:  
                os.system("cls")
                preguntas_y_respuestas(numero_escalon,numero_escalon+1)
                respuesta_usuario=str(input("\033[4;35m"+"Elija su respuesta escribiendo la letra correcta: "+'\033[0;m')).upper()
                ultima_pregunta=escalones[numero_escalon]["Pregunta: "]
                lista_preguntas.append(ultima_pregunta)
                lista_opciones.append(respuesta_usuario)
                if respuesta_correcta(numero_escalon,respuesta_usuario):
                    lista_opciones_verdaderas.append("Verdadero")
                    puntaje_jugador(numero_escalon,Puntaje)
                    print("\n")
                    Puntaje+=10
                    texto.clear()
                    texto.write("Puntaje: {}".format(Puntaje)  ,  align ="center", font = ["Courier", 24, "normal"])
                    print("\033[0;30;42m","Respuesta correcta!","\n","Tenes", Puntaje ,"puntos","\n","Pasas al siguiente escalon!",'\033[0;m',"\n")
                    #sleep(3)
                    numero_escalon+=1
                    i+=1
                else:
                    lista_opciones_verdaderas.append("Falso")
                    os.system("cls")
                    print ("Game Over")
                    break
                i=i
                numero_escalon=numero_escalon
                
    while i>6 and i<11:
            os.system("cls")
            e=1
            print("\033[0;30;46m","ESTAS EN EL ULTIMO ESCALON,AHORA TENES QUE RESPONDER 4 PREGUNTAS CORRECTAS CONSECUTIVAS","\033[0;m")
            print("\033[4;31m"," La pregunta numero ", e ," es :",'\033[0;m')
            preguntas_y_respuestas_ultimo_escalon(numero_escalon,numero_escalon+1)
            respuesta_usuario=str(input("\033[4;35m"+"Elija su respuesta escribiendo la letra correcta: "+'\033[0;m')).upper()
            lista_preguntas.append(ultima_pregunta)
            lista_opciones.append(respuesta_usuario)
            if respuesta_correcta(numero_escalon,respuesta_usuario) and i<10:
                    lista_opciones_verdaderas.append("Verdadero")
                    print("\n","\033[0;30;42m","Respuesta correcta! sumaste 20 puntos!",'\033[0;m',"\n")
                    #sleep(3)
                    numero_escalon+=1
                    e+=1
                    i+=1
                    Puntaje+=20
                    texto.clear()
                    texto.write("Puntaje: {}".format(Puntaje)  ,  align ="center", font = ["Courier", 24, "normal"])
                    os.system("cls")
            elif respuesta_correcta(numero_escalon,respuesta_usuario) and i>9:
                    lista_opciones_verdaderas.append("Verdadero")
                    os.system("cls")
                    print("\n","\033[0;30;42m","FELICITACIONES! GANASTE EL JUEGO DE LOS 8 ESCALONES DE LA PROGRAMACION",'\033[0;m',"\n")
                    numero_escalon+=1
                    e+=1
                    i+=1
                    Puntaje+=20
                    print("Tu Puntaje es:",Puntaje, "podes fijarte en el marcador debajo")
                    texto.write("Puntaje: {}".format(Puntaje)  ,  align ="center", font = ["Courier", 24, "normal"])
            else:
                lista_opciones_verdaderas.append("Falso")
                os.system ("cls")
                print ("Game Over")
                break

    escalones=leer_archivo("Preguntas.json")
    partidas=leer_archivo("Registro_partidas.json")
    
    lista_preguntas_dict=[]

    partidas.append({
            "Nombre del jugador: ": nombre,
            "Fecha y hora: " : fecha_hora,
            "Puntaje obtenido: ": Puntaje,
            "Preguntas que le tocaron: " : lista_preguntas_dict
            })
    x=0
    for x in range(len(lista_preguntas)):
        lista_preguntas_dict.append({ 
            "Preguntas que le tocaron: " : {
                "Pregunta: " : lista_preguntas[x],
                "Opcion seleccionada: ": lista_opciones[x],
                "Es respuesta correcta: ":lista_opciones_verdaderas[x]
        }})
    guardar_archivo("Registro_partidas.json",partidas)

elif opcion==3:
    print("\033[0;30;43m","MODO CONSULTAS",'\033[0;m',"\n")
    lista=leer_archivo('Registro_partidas.json')
    #print(lista)
    print("\033[0;30;47m","1 - Filtrar por nombres","\n","2 - Filtrar por fecha")
    filtros=int(input("Elija la opcion: "))
    lista_nombres=[]
    lista_puntajes=[]
    lista_fechas=[]
    if filtros==1:
        nombre_filtro=input(("Ingrese el nombre del jugador, a continuación le mostraremos sus puntajes: "))
        for x in range(len(lista)):
            if nombre_correcto(x,nombre_filtro):
                numero_puntaje=lista[x]["Puntaje obtenido: "]
                lista_nombres.append(numero_puntaje)
                lista_nombres.sort()
                print(lista_nombres)
    elif filtros==2:
        fecha_filtro=input(("Ingrese la fecha en la que jugo, a continuación le mostraremos sus puntajes: "))
        for x in range(len(lista)):
            if fecha_correcta(x,fecha_filtro):
                print(lista[x]["Puntaje obtenido: "])

""""
if filtros==1:
    
        lista=leer_archivo('Registro_partidas.json')
        nombre_filtro=input(("Ingrese el nombre del jugador, a continuación le mostraremos sus puntajes: "))
        
        if nombre_filtro in lista[]["Nombre del jugador: "]:
            print(registro_partidas["Puntaje obtenido"])
        else:
            print("El nombre ingresado no se encuentra en la base de datos")
"""
import requests
import json
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("HomeWeather")
root.geometry("250x122")

api_key = '30a0a1deb5b8512aa9b6789ef5f99624'
city_coord = '43.262985, -2.935013'
base_url = 'https://api.darksky.net/forecast/'
param_url = 'lang=es&exclude=minutely,hourly,flags&units=si'
url = base_url + api_key + "/" + city_coord + "?" + param_url

response = requests.get(url)
    
#Convertimos los datos a json
x = response.json()

#Revisamos que la conexión no esté dando error y captamos datos

if x["currently"] != "404":
    #guardamos "currently" en la variable y
    y = x["currently"]

    #guardamos todos los valores de currently
    temp_actual = int(y["temperature"])
    pres_actual = y["pressure"]
    descrip_actual = y["summary"]
    icon_actual = y["icon"]
    
    #Definimos el tipo de icono en base a icon recibido por json (creamos funcion para que sea reutilizable
    
    def icono_tiempo(nombre_var):
        if nombre_var == "clear-day":
            print("imagen sol")
        elif nombre_var == "clear-night":
            print("imagen luna")
        elif nombre_var == "rain":
            print("imagen lluvia")
        elif nombre_var == "snow":
            print("imagen nieve")
        elif nombre_var == "sleet":
            print("imagen granizo")
        elif nombre_var == "wind":
            print("imagen viento")
        elif nombre_var == "fog":
            print("imagen niebla")
        elif nombre_var == "cloudy":
            print("imagen nube")
        elif nombre_var == "partly-cloudy-day":
            print("imagen dia nube")
        elif nombre_var == "partly-cloudy-night":
            print("imagen noche nube")
        
    icono_tiempo(icon_actual)

    #guardamos varlores diarios en z
    z = x["daily"]
    prev_dias = z["data"]

    #Intentamos meter funcion para semplificar legibilidad del codigo
    # def previsiones(prev_dias = z["data"]):
    #     temp_max_manana = (["temperatureHigh"])
    #     temp_min_manana = (["temperatureLow"])
    #     pres_manana = ["pressure"]
    #     icon_manana = ["icon"]
    # print(previsiones(prev_dias[5]))

    #Día 1
    time_manana = prev_dias[2]["time"]
    #convertimos UNIX recibido a formato legible
    print(datetime.utcfromtimestamp(time_manana).strftime('%d / %m'))

    temp_max_manana = int(prev_dias[2]["temperatureHigh"])
    temp_min_manana = int(prev_dias[2]["temperatureLow"])
    pres_manana = prev_dias[2]["pressure"]
    icon_manana = prev_dias[2]["icon"]
    
    

    #mostramos un icono para saber si la presión sube o baja respecto al día anterior
    if pres_manana > pres_actual:
        print(r'\u1F815')
    elif pres_manana == pres_actual:
        print('=')
    else:
        print(r'\u1F817')

    #Día 2
    time_pasado_manana = prev_dias[3]["time"]
    #convertimos UNIX recibido a formato legible
    print(datetime.utcfromtimestamp(time_pasado_manana).strftime('%d / %m'))

    temp_max_pasado_manana = int(prev_dias[3]["temperatureHigh"])
    temp_min_pasado_manana = int(prev_dias[3]["temperatureLow"])
    pres_pasado_manana = prev_dias[3]["pressure"]
    icon_pasadp_manana = prev_dias[3]["icon"]

    #mostramos un icono para saber si la presión sube o baja respecto al día anterior
    if pres_pasado_manana > pres_manana:
        print(r'\u1F815')
    elif pres_pasado_manana == pres_manana:
        print('=')
    else:
        print(r'\u1F817')
    
     #Día 3
    time_tres_prev = prev_dias[4]["time"]
    #convertimos UNIX recibido a formato legible
    print(datetime.utcfromtimestamp(time_tres_prev).strftime('%d / %m'))

    temp_max_tres = int(prev_dias[4]["temperatureHigh"])
    temp_min_tres = int(prev_dias[4]["temperatureLow"])
    pres_tres = prev_dias[4]["pressure"]
    icon_tres = prev_dias[4]["icon"]

    #mostramos un icono para saber si la presión sube o baja respecto al día anterior
    if pres_tres > pres_pasado_manana:
        print(r'\u1F815')
    elif pres_tres == pres_pasado_manana:
        print('=')
    else:
        print(r'\u1F817')


     #Día 4
    time_cuatro_prev = prev_dias[5]["time"]
    #convertimos UNIX recibido a formato legible
    print(datetime.utcfromtimestamp(time_cuatro_prev).strftime('%d / %m'))

    temp_max_cuatro = int(prev_dias[5]["temperatureHigh"])
    temp_min_cuatro = int(prev_dias[5]["temperatureLow"])
    pres_cuatro = prev_dias[5]["pressure"]
    icon_cuatro = prev_dias[5]["icon"]

    #mostramos un icono para saber si la presión sube o baja respecto al día anterior
    if pres_cuatro > pres_tres:
        print(r'\u1F815')
    elif pres_cuatro == pres_tres:
        print('=')
    else:
        print(r'\u1F817')
    

     #Día 5
    time_cinco_prev = prev_dias[6]["time"]
    #convertimos UNIX recibido a formato legible
    print(datetime.utcfromtimestamp(time_cinco_prev).strftime('%d / %m'))

    temp_max_cinco = int(prev_dias[6]["temperatureHigh"])
    temp_min_cinco = int(prev_dias[6]["temperatureLow"])
    pres_cinco = prev_dias[6]["pressure"]
    icon_cinco = prev_dias[6]["icon"]

    #mostramos un icono para saber si la presión sube o baja respecto al día anterior
    if pres_cinco > pres_cuatro:
        print(r'\u1F815')
    elif pres_cinco == pres_cuatro:
        print('=')/home/pi/Desktop/homeWeather
    else:
        print(r'\u1F817')
        
    #GUI
    mylabel = Label(root, text=temp_actual)
    mylabel.pack()
    
    
    root.mainloop()
    
    
    

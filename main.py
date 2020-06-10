import requests, json
from datetime import datetime

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
    temp_actual = y["temperature"]
    pres_actual = y["pressure"]
    descrip_actual = y["summary"]
    icon_actual = y["icon"]

    #guardamos varlores diarios en z
    z = x["daily"]
    prev_dias = z["data"]
   
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

    

 
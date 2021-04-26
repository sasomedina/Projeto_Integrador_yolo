x# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:31:07 2020

@author: caio.mukai
"""
# =============================================================================
# Teste Api Google
# =============================================================================
import pandas as pd
import googlemaps
from utils.utils import *
import json

jsonConn = (json.load(open('Caio - AIzaSyB.json')))
conect = (jsonConn['google']['local']['pass'])
estacao = read_csv("data/estacao.csv")
df=estacao

gmaps_key = googlemaps.Client(key = Conect)

# df["LAT"] = None
# df["LON"] = None

for i in range(0, len(df), 1):
    geocode_result = gmaps_key.geocode(df.iat[i, 0])
    geocode_result = gmaps_key.geocode("Term. Jabaquara  São Paulo  Brazil")
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        df.iat[i,df.columns.get_loc("LAT")]= lat
        df.iat[i,df.columns.get_loc("LON")]= lon
    except:
        lat = None
        lon = None
        
save_as_csv(df, 'data/Address_to_GPS.csv')

# =============================================================================
# Teste de adress to geolocation
# =============================================================================
        
from utils.utils import *
from geopy.geocoders import Nominatim 
import pandas as pd

df_aps=read_csv('aps.csv')

x=df_aps['Endereço'].unique()


nom = Nominatim()
for i in x :
    n=nom.geocode("R. Cel. Joaquim Ferreira Lôbo, 305 - Vila Nova Conceição")
    print(i,n.latitude, n.longitude)


# =============================================================================
# Teste Calculo de distancia 
# =============================================================================
from geopy import distance
from utils.utils import *
estacao = read_csv("data/estacao.csv")
#house = read_csv("data/Data_set.csv")

house = ([-23.5701325,-46.6573532],[-23.593657,-46.6846833],[-23.5973664,-46.6863424],[-23.5995101,-46.6766726],[-23.5302546,-46.6789501])
for i in range(0, 10):
    print (i)
    house = house[1]
    lat = (estacao['latitude'][3])
    lat = (-23.6244547)
    lon = (-46.6379525)
    lon = (estacao['longitude'][3])
    metro=(lat,lon)
    print(distance.distance(house, metro).km)

 house = (-23.5701325,-46.6573532)
 metro = (-23.6244547,-46.6379525)
#print(distance.distance(wellington, salamanca).km)
print(distance.distance(house, metro).km)

# =============================================================================
# Teste Calculo de distancia Api GOOGLE
# =============================================================================

import  googlemaps
import json
from utils.utils import *
import pandas as pd

df_house = read_csv("data/Data_set_full.csv")
df_estacao = read_csv("data/estacao.csv")

jsonConn = (json.load(open('Caio - AIzaSyB.json')))
conect = (jsonConn['google']['local']['pass'])
gmaps_key = googlemaps.Client(key = conect)

# house = ['R. Cel. Joaquim Ferreira Lôbo, 305','Alameda Campinas, 708 - Jardim Paulista, São Paulo - SP'
#          , 'R. Gomes de Carvalho, 1146 - Vila Olímpia, São Paulo - SP'
#          , 'R. Quatá, 76 - Vila Olímpia, São Paulo - State of São Paulo'
#          , 'R. Turiassú, 1473 sp']

# metro = ['Marginal Pinheiros, 7522 - Vila Olímpia, São Paulo - SP, 04533-085']
colunas = ['ID_origen','L_ORIGEM','ID_DESTINO','L_DESTINO', 'DISTANCIA','TEMPO']

df_distancia = pd.DataFrame(columns=colunas)

for index,l_house in df_house.iterrows():
    for index,l_estacao in df_estacao.iterrows():
        try:
            distance_result = gmaps_key.distance_matrix(l_house['Endereço']
            ,l_estacao['address'], mode='walking')
            distance_walking = (distance_result['rows'][0]['elements'][0]['distance']['value'])
            tempo_s_walking = (distance_result['rows'][0]['elements'][0]['duration']['value'])
        except: 
            distance_walking = 0
            tempo_s_walking = 0
        list_temp = (l_house['ID'], l_house['Endereço'], l_estacao['estaçao']
                     ,l_estacao['address'],distance_walking,tempo_s_walking)
        #aux = df_house.loc[df_house['Endereço']==l_house, ['ID', 'Endereço']]
        #aux['ID_DESTINO'] = 
        temp = pd.DataFrame([list_temp],columns=colunas)
        df_distancia = df_distancia.append(temp, ignore_index=True)
save_as_csv(df_distancia, "data/Todos_as_estaçoes.csv")
# distance_result = gmaps_key.distance_matrix(house[0],metro, mode='walking')
# distance_walking = (distance_result['rows'][0]['elements'][0]['distance']['value'])
# tempo_s_walking = (distance_result['rows'][0]['elements'][0]['duration']['value'])
# print ("Enderesso de Origem: "+ distance_result['origin_addresses'][0])
# print ("Enderesso de Destino: "+ distance_result['destination_addresses'][0])
# print (distance_walking/100 )
# print (tempo_walking /60)



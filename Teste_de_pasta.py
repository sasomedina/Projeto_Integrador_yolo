# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:40:49 2020

@author: caio.mukai
"""
import pandas as pd
import cv2
import argparse
import numpy as np
import os
from os import listdir
from os.path import isfile, join, isdir
from utils.processa import olha_imagem
from utils.utils import *

# =============================================================================
# Le Imagen 
# =============================================================================
start_path = os.getcwd()
os.chdir(start_path)
dir_image = ("/images/")
#dir_image = ("/pasta-share/FOTOS")
c = start_path +dir_image
folders = os.listdir(start_path+dir_image)

list_all_folder_dir = []
for name in folders:
    folder=os.path.join(start_path+dir_image,name)
    list_all_folder_dir.append(folder)
name = []
    
list_all_file_dir = []
for list_folder in list_all_folder_dir:
    os.chdir(list_folder)
    files = filter(os.path.isfile, os.listdir())
    files = [os.path.join(list_folder, f) for f in files]
    os.chdir(start_path)
    for teste in files:
        list_all_file_dir.append(teste)
        
list_all_itens = []
for _ in list_all_file_dir:
    print (_)
    try:
        itens = olha_imagem(_)
        list_all_itens.append(itens)
    except:
        pass

dfs = []
for i, value in enumerate(list_all_itens):
    df = pd.DataFrame(list_all_itens[i], columns=['ID','Class', 'Conf', 'Item'])
    dfs.append(df)
df = []
dfs = pd.concat(dfs, axis=0)
dfs = dfs.groupby(['ID','Item'], as_index=False)[['Conf']].max()
dfs.head()
# =============================================================================
# Cria Data frame das imagen
# =============================================================================
df_aps=read_csv('data/aps.csv')
df_itens=pd.read_excel('TODAS_IMAGENS.xlsx')

for id_ap in df_aps['ID'].unique():
    # Olhando itens em cada um dos aps
    df_itens_ap = df_itens.loc[df_itens['ID'] == id_ap]
    # Salvando em uma lista todos os itens presentes
    itens_ap = df_itens_ap['Item'].unique()

    for item in itens_ap:
        # Testa se o item está nas colunas do df_aps
        if item in df_aps.columns.tolist():
            # Se sim, escreve como 1, sinalizando que o item existe e grava a confiança
            df_aps.loc[df_aps['ID'] == id_ap, item] = 1
            df_aps.loc[df_aps['ID'] == id_ap, str(item)+'_conf'] = df_itens_ap.loc[df_itens_ap['Item'] == item, 'Conf'].values
            
            
save_as_csv(df_aps,'data/Data_set.csv')
print (x)
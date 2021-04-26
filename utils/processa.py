# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:34:53 2020

@author: caio.mukai
"""
import pandas as pd
import cv2
import argparse
import numpy as np
import os
from os import listdir
from os.path import isfile, join, isdir


def olha_imagem(local_imagem):
    
    #local_imagem = (r".\images\Alam. Campinas One_Bed\IMG_8803.jpg")
    cfg_teste = ("./yolo_lib/yolov3.cfg")
    weight_teste = ("./yolo_lib/yolov3.weights")
    txt_teste = ("./yolo_lib/yolov3.txt")
    path_image = os.path.normpath(local_imagem)
    slipt_image=path_image.split(os.sep)

    def get_output_layers(net):
        
        layer_names = net.getLayerNames()
        
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    
        return output_layers
    
    def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    
        label = str(classes[class_id])
    
        color = COLORS[class_id]
    
        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    
        cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
    image = cv2.imread(local_imagem)
    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392
    classes = None
    
    with open(txt_teste, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
        
    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
    net = cv2.dnn.readNet(weight_teste, cfg_teste)
    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(get_output_layers(net))
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.6
    nms_threshold = 0.4
    view_list = []
    
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                numero_classe = class_id
                percentual = float(confidence)
                label = str(classes[class_id])
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
                itens = ([slipt_image[-2],numero_classe,percentual,label])
                view_list.append(itens)
    return view_list

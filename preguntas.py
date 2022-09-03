"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

arc = csv.reader(open("data.csv", newline=""), delimiter="\t")

def pregunta_01():
    ite = 0
    for fila in arc: 
        ite += int(fila[1])
    return ite


def pregunta_02():
    res = {}

    for fila in arc:
        if fila[0] not in res: 
            res[fila[0]] = 1
        else: 
            res[fila[0]] += 1
    
    res1 = sorted(res.items(), key=lambda x: x[0])
    return res1


def pregunta_03():
    res = {}

    for fila in arc:
        if fila[0] not in res: 
            res[fila[0]] = int(fila[1])
        else: 
            res[fila[0]] += int(fila[1])

    res1 = sorted(res.items(), key=lambda x: x[0])
    return res1


def pregunta_04():
    res = {}

    for fila in arc:
        mes = fila[2].split("-")[1]
        if mes not in res: 
            res[mes] = 1
        else: 
            res[mes] += 1

    res1 = sorted(res.items(), key=lambda x: x[0])
    return res1


def pregunta_05():
    res, res1 = {}, []

    for fila in arc:
        if fila[0] not in res: 
            res[fila[0]] = [int(fila[1])]
        else: 
            res[fila[0]] += [int(fila[1])]

    resOrd = sorted(res.items(), key=lambda x: x[0])
    for ltr in resOrd: 
        res1.append((ltr[0], max(ltr[1]), min(ltr[1])))
    return res1


def pregunta_06():
    res, res1 = {}, []

    for fila in arc:
        for ele in fila[4].split(","):
            val = ele.split(":")
            if val[0] not in res: 
                res[val[0]] = [int(val[1])]
            else: 
                res[val[0]] += [int(val[1])]

    resOrd = sorted(res.items(), key=lambda x: x[0])
    for ltr in resOrd: 
        res1.append((ltr[0], min(ltr[1]), max(ltr[1])))
    return res1


def pregunta_07():
    res = {}

    for fila in arc:
        if fila[1] not in res: 
            res[fila[1]] = [fila[0]]
        else: 
            res[fila[1]] += [fila[0]]

    resOrd = sorted(res.items(), key=lambda x: x[0])
    return resOrd


def pregunta_08():
    res = {}

    for fila in arc:
        if fila[1] not in res:
            res[fila[1]] = [fila[0]]
        else:
            if fila[0] not in res[fila[1]]: 
                res[fila[1]] += [fila[0]]

    resOrd = sorted(res.items(), key=lambda x: x[0])
    for item in resOrd: 
         item[1].sort()
    return resOrd


def pregunta_09():
    res = {}

    for fila in arc:
        for ele in fila[4].split(","):
            val = ele.split(":")
            if val[0] not in res: 
                res[val[0]] = 1
            else: 
                res[val[0]] += 1

    resOrd = sorted(res.items(), key=lambda x: x[0])
    return resOrd


def pregunta_10():
    res = []

    for fila in arc:
        col4 = fila[3].split(",")
        col5 = fila[4].split(",")
        res.append((fila[0], len(col4), len(col5)))

    return res


def pregunta_11():
    res = {}

    for fila in arc:
        col4 = fila[3].split(",")
        for val in col4:
            if val not in res: 
                res[val] = int(fila[1])
            else: 
                res[val] += int(fila[1])

    return dict(sorted(res.items()))


def pregunta_12():
    res = {}
    for fila in arc:
        col5, valor = fila[4].split(","), 0
        for ele in col5:
            valor += int(ele.split(":")[1])
        
        if fila[0] not in res:
            res[fila[0]] = valor
        else:
            res[fila[0]] += valor

    return dict(sorted(res.items()))
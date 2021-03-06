def sim_jac(s1, s2):

    bigrams_s1 = []
    bigrams_s2 = []

    for i in range(len(s1) - 1):
        bigrams_s1.append(s1[i:i+2])
    
    for i in range(len(s2) - 1):
        bigrams_s2.append(s2[i:i+2])

    c_common = 0

    for i in bigrams_s1:
        if bigrams_s2.count(i) > 0:
            c_common += 1

    return c_common / ((len(s1) - 1) + (len(s2) - 1) - c_common)

def encontrar_palabras(transcript,cjto_palabras):
    '''
    Toma un string (en minúsculas) y un conjunto de palabras. Busca el primer match
    de cjto_palabras en transcript y particiona el string en:
        1. El slice de la cadena antes del primer match (antes_palabra)
        2. La cadena del primer match (coincidencia de cjto_palabras)
        3. El slice de la cadena después del match (despues_palabra)
    '''
    inicio,final=list(re.finditer(r'|'.join(cjto_palabras),transcript))[0].span()
    antes_palabra=transcript[:inicio].strip()
    despues_palabra=transcript[final:].strip()
    palabra=transcript[inicio:final]
    return antes_palabra,palabra,despues_palabra


def agregar_adentro(codigo, transcipcion):
    codigo2 = main(transcipcion)
  
    return codigo[:-1] + codigo2


import numpy as np

def main(instruccion):
    global bloque

    plantillas = [
                crear_funcion,
                crear_condicional,
                crear_condicional,
                asignar_variable,
                crear_variable,
                crear_llamada,
                crear_for,
                fin_de_bloque,
                crear_comentario,
                crear_regresa         
                ]

    comandos = [set(['definir', 'funcion', 'parametros']),
                set(['mientras']),
                set(['si']), # si se cumple / mientras se cumpla
                set(['asignar', 'con']),
                set(['definir', 'variable']),
                set(['ejecuta', 'argumentos']),
                set(['para', 'rango']),
                set(['terminar','bloque']),
                set(['comentario']),
                set(['regresa'])

                ]

    J = []
    for comando in comandos:
        J.append(len(set(instruccion.strip().split(' ')).intersection(comando)) / len(set(instruccion.strip().split(' ')).union(comando)))
    # print(J,np.argmax(J))
    pos_func=np.argmax(J)
    # print(pos_func)
    return plantillas[pos_func](instruccion)
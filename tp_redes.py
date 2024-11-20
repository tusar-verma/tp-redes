#!/usr/bin/env python3
import sys
from scapy.all import *
from time import *

def calcular_rtts_time_exceeded():

    responses = {}

    for i in range(30):

        for lista_rtts in range(1,25):
            probe = IP(dst=sys.argv[1], ttl=lista_rtts) / ICMP()
            t_i = time()
            ans = sr1(probe, verbose=False, timeout=0.8)
            t_f = time()
            rtt = (t_f - t_i)*1000

            if ans is not None and ans.haslayer(ICMP):
                # solo me quedo con aquellas respuestas que fueron de Time Exceeded
                if ans[ICMP].type == 11 or ans.src == sys.argv[1]: # tipo time exceeded
                    if lista_rtts not in responses:
                        responses[lista_rtts] = []
                    responses[lista_rtts].append((ans.src, rtt))
                #if ttl in responses:
                #    print(ttl, responses[ttl])


    # Muestro el resultado de los 30 envios por cada ttl
    for e in responses:
        print("------------")
        print(e, responses[e])
    
    return responses
# promediar RTTs

# Para los distintos TTL seleccionar la IP que mas veces aparece
# Tomar las RTT de dicha IP y promediarlo
# Se obtiene así el RTT del router a distancia TTL hops

def calcular_rtt_promedio_por_ttl(responses):

    rtt_promedio = {}

    for ttl in responses:
        lista_rtts = responses[ttl]

        counters_per_ip = {}
        # obtengo la IP con mas respuestas de time exceeded
        for tupla in lista_rtts:
            if tupla[0] not in counters_per_ip:
                counters_per_ip[tupla[0]] = 1
            else:
                counters_per_ip[tupla[0]] += 1
        
        ip_con_mas_rtts = max(counters_per_ip, key=counters_per_ip.get)

        # calculo el rtt promedio para dicha ip
        # recorro toda la lista de rtts para la ttl actual y voy acumulando los rtts de la ip conseguida
        res = 0
        count = 0
        for tupla in lista_rtts:
            if tupla[0] == ip_con_mas_rtts:
                count += 1
                res += tupla[1]

        rtt_promedio[ttl] = (ip_con_mas_rtts, res / count)

    return dict(sorted(rtt_promedio.items()))

# Calcular RTT entre saltos

# Tomar el vector resultante del procedimiento anterior y calcular la diferencia
# de saltos sucesivos
# Si da negativo, ignorarlo y usar el RTT del siguiente salto hasta que de positivo

def calcular_rtt_entre_saltos(rtt_promedio):

    rtt_entre_saltos = []

    ttls_disponibles = sorted(rtt_promedio.keys())

    for i in range(len(ttls_disponibles)):

        # busco el proximo elemento de ttls_disponibles tal que la diferencia de rrt[j] - rtt[i] sea positiva
        j = i+1    
        while (j < len(ttls_disponibles) and rtt_promedio[ttls_disponibles[j]][1] - rtt_promedio[ttls_disponibles[i]][1] < 0):
            j+=1
        
        # si pude encontrar un hop tal que el rtt quede positivo, guardo la diferencia. 
        # Sino guardo 0 
        if (j < len(ttls_disponibles)):
            rtt_entre_saltos.append(rtt_promedio[ttls_disponibles[j]][1] - rtt_promedio[ttls_disponibles[i]][1])
        else:
            rtt_entre_saltos.append(0)

    return rtt_entre_saltos


res = calcular_rtts_time_exceeded()
print(res)
print("------")
res = calcular_rtt_promedio_por_ttl(res)
print(res)
print("------")
res = calcular_rtt_entre_saltos(res)
print(res)

# ejercicio 2

# 192.0.66.20
# 129.132.19.216
# 129.187.255.109
# 41.204.161.206
# 130.226.237.173
import numpy as np

# 40 primeros valores de la tabla tau. 
# En nuestro caso de uso tenemos hasta 25 muestras (TTLs) por lo que nos sobra.
# La tabla empieza con n=3 por eso pongo 3 valores en 0 al principio
tabla_tau = [0, 0, 0, 1.1511, 1.4250, 1.5712, 1.653, 1.7110, 1.7491, 1.7770, 1.7984, 1.8153, 1.8290, 1.8403, 1.8498, 1.8579, 1.8649, 1.8710, 1.8764, 1.8811, 1.8853, 1.8891, 1.8926, 1.8957, 1.8985, 1.9011, 1.9035, 1.9057, 1.9078, 1.9096, 1.9114, 1.9130, 1.9146, 1.9160, 1.9174, 1.9186, 1.9198, 1.9209, 1.9220, 1.9240]


def detect_outliers_cimbala(data):

    # convertir datos a numpy array y ordenarlos
    sample = np.sort(data)    

    outliers = []
    hubo_outliers = True


    while (hubo_outliers):

        mean = np.mean(sample)
        std_dev = np.std(sample)

        abs_deviation = np.array([abs(e - mean) for e in sample])
        sample_size = sample.size
        
        # los posibles outliers son el elemento más grande y el más chico
        posible_out_arg = np.argmax(abs_deviation)
        test_out = tabla_tau[sample_size] * std_dev

        if (abs_deviation[posible_out_arg] > test_out):
            outliers.append(sample[posible_out_arg])
            hubo_outliers = True
            sample = np.delete(sample, posible_out_arg)
        else:
            hubo_outliers = False

    return outliers



def calcular_outliers():
    nai = [10.852303649439957, 11.432670101974953, 2.487454269871563, 124.93927478790283, 0.4895579987677934, 3.6683527455813874, 94.83540654182431, 4.367184638977051, 0.5378643671671739, 6.83275063832599, 138.52503299713135, 9.621246655782102, 7.416661580403627, 0]
    ttls_nai = [1,2,7,8,9,10,11,15,16,17,18,19,20,21]

    cop = [13.255270322163899, 14.327486356099445, 207.42810567220053, 207.99339612325033, 2.9042800267537245, 4.737663269042969, 5.196587244669587, 0.231170654296875, 6.6667954126994005, 0, 8.246286710103334, 0]
    ttls_cop = [1,2,7,8,9,10,11,12,13,14,15,18]


    
    #zur = [19.575084580315487, 21.214021576775448, 134.16869905259875, 139.66718514760336, 104.22531763712567, 110.12521584828696, 0, 2.49936580657959, 0.5045334498087755, 6.252876917521178, 0, 0]
    #ttls_zur = [1,2,7,8,9,10,11,12,13,14,15,16]
    zur = [19.575084580315487, 21.214021576775448, 139.66718514760336, 110.12521584828696, 2.49936580657959, 0.5045334498087755, 6.252876917521178, 0, 0]
    ttls_zur = [1,2,8,10,12,13,14,15,16]


    
    mun = [10.546832992917011, 12.005914960588726, 0.30262697310674724, 122.4228342374166, 0.30933959143501966, 110.25757449013847, 6.228049596150697, 7.784589131673158, 2.9729426592246, 3.6610027839397503, 0, 0]
    ttls_mun = [1,2,7,8,9,10,11,12,13,14,15,16]

    #har = [16.318576676504954, 19.479180517650786, 135.9595287413824, 136.58105532328287, 139.9232228597005, 0, 0, 0]
    #ttls_har = [1,2,7,9,10,12,13,14]

    har = [16.318576676504954, 19.479180517650786, 135.9595287413824, 136.58105532328287, 139.9232228597005, 0, 0, 0]
    ttls_har = [1,2,7,9,10,12,13,14]


    outliers_har = detect_outliers_cimbala(har)
    outliers_mun = detect_outliers_cimbala(mun)
    outliers_zur = detect_outliers_cimbala(zur)
    outliers_nai = detect_outliers_cimbala(nai)
    outliers_cop = detect_outliers_cimbala(cop)

    ttls_out_har = []
    ttls_out_mun = []
    ttls_out_zur = []
    ttls_out_nai = []
    ttls_out_cop = []


    for o in outliers_har:
        ttls_out_har.append(ttls_har[har.index(o)])

    for o in outliers_mun:
        ttls_out_mun.append(ttls_mun[mun.index(o)])

    for o in outliers_zur:
        ttls_out_zur.append(ttls_zur[zur.index(o)])

    for o in outliers_nai:
        ttls_out_nai.append(ttls_nai[nai.index(o)])
        
    for o in outliers_cop:
        ttls_out_cop.append(ttls_cop[cop.index(o)])

    ttls_out_har.sort()
    ttls_out_mun.sort()
    ttls_out_zur.sort()
    ttls_out_nai.sort()
    ttls_out_cop.sort()
        
    print(ttls_out_har)
    print(ttls_out_mun)
    print(ttls_out_zur)
    print(ttls_out_nai)
    print(ttls_out_cop)


calcular_outliers()
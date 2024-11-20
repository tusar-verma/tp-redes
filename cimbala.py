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



def prueba_nairobi():
    nai_b = [10.852303649439957, 11.432670101974953, 2.487454269871563, 124.93927478790283, 0.4895579987677934, 3.6683527455813874, 94.83540654182431, 4.367184638977051, 0.5378643671671739, 6.83275063832599, 138.52503299713135, 9.621246655782102, 7.416661580403627, 0]
    ttls = [1,2,7,8,9,10,11,15,16,17,18,19,20,21]


    outliers = detect_outliers_cimbala(nai_b)
    print(outliers)

    ttls_outliers = []

    for o in outliers:
        ttls_outliers.append(ttls[nai_b.index(o)])

    print(ttls_outliers)

prueba_nairobi()
#contador = 0


#while contador < 10: 
#    print (contador)
#    contador += 1 # Es lo mismo a contador = contador + 1

contador_externo = 0
contador_interno = 0


while contador_externo < 5: 
    while contador_interno < 6:
        print (contador_externo, contador_interno)
        contador_interno += 1
    
    contador_externo += 1 
    contador_interno = 0
        #contador += 1 # Es lo mismo a contador = contador + 1


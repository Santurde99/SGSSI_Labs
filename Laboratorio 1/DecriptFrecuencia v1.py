
def decrypt(mensaje):
    abecedario = [0]*27 #una posicion por letra en el alfabeto
    letras_totales = 0
    for caracter in mensaje:
        pos = ord(caracter)
        if (pos >=97 and pos <=122) or pos == 164:
            if pos == 164:
               abecedario[13] = abecedario[13]+1
            elif pos<=110:
               pos = pos-97
               abecedario[pos] = abecedario[pos] + 1
            elif pos > 110:
               pos = pos-96
               abecedario[pos] = abecedario[pos] + 1
            letras_totales = letras_totales +1

    #Tenemos anotadas el numero de apariciones de cada letra y el total de letras
    i=0
    while i <= 26:
        abecedario[i] = (abecedario[i]/letras_totales)*100
        i = i + 1
    #Tenemos el porcentaje de aparicion de cada letra
    #Volvemos a iterar el mensaje sustituyendo cada letra por la equivalente
    resultado = ""
    diccio = relacionar(abecedario)
    for caracter in mensaje:
       letraenc = ord(caracter) #obtenemos su valor ascii
       if (letraenc >=97 and  letraenc <=122) or letraenc == 164:
          caracter = diccio[caracter]
       resultado = resultado + caracter
    respuesta = ""
    print("=========================================================================================")
    print("Respuesta:")
    print("=========================================================================================")
    print (resultado)
    print("=========================================================================================")
    while (respuesta != 's') or (respuesta != 'n'):
      print ("Si el texto no es demasiado largo, posiblemente la traduccion no sea correcta, sin embargo, la 'a' y la 'e' (las mas comunes) deberian estar en su sitio, deseas cambiar las letras manualmente? s/n")
      respuesta = input()
      if respuesta == 's':
       cambiarLetras(resultado)
       respuesta = "n"
      else:
       print ("Presiona enter para salir")
       input()    

def cambiarLetras (texto):
   letraActual = ""
   letraNueva = ""
   salir = False
   while salir == False:
      print("Introduce la letra que deseas cambiar en minuscula o escibe 'salir' para salir")
      letraActual = input()
      if (len(letraActual) == 1):
         letraNueva = ""
         while (len(letraNueva) !=1):
            print("Introduce la letra que ocupara su lugar EN MAYUSCULA")
            letraNueva = input()
         texto = texto.replace(letraActual,letraNueva)
         print("=========================================================================================")
         print("El texto nuevo es:")
         print("=========================================================================================")
         print(texto)
         print("=========================================================================================")
      elif (letraActual == "salir"):
         salir = True
         print("=========================================================================================")
         print("El texto final es:")
         print("=========================================================================================")
         print(texto)
      else:
         print("")


   
def relacionar (TablaFrec):
   print("Creando diccionario, espere porfavor")
   referencia = ['e','a','o','l','n','s','d',"r",'u','i','t','c','p','m','y','q','b','h','g','f','v','j','ñ','z','x','k','w']
   diccionario = {}
   for letra in referencia:
      indice = 0 #posicion en la tabla de frecuencias
      masAlto = 0
       #Valor mas alto encontrado
      posMasAlto = 0 #Posicion de valor mas alto encontrado
      while indice < len(TablaFrec):
         if TablaFrec[indice] > masAlto:
            masAlto = TablaFrec[indice]
            posMasAlto = indice
         else:
            indice = indice +1
      diccionario[definirLetra(posMasAlto)] = letra
      indice = indice+1  
      TablaFrec[posMasAlto] = -1 
   print("Diccionario creado")      
   return diccionario

def definirLetra(posAlfabetica):
   letraResultado = ''
   if posAlfabetica == 14:
      letraResultado = 'ñ'
   elif posAlfabetica <=13:
      letraResultado = chr(posAlfabetica+97)
   else:
      letraResultado = chr(posAlfabetica+96)
   return letraResultado


if __name__ == '__main__':
 print("Introduce el mensaje encriptado por analisis de frecuencia")
 mensaje = input()
 decrypt(mensaje.lower())
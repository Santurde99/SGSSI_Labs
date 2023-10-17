import hashlib
import os

def main():
    encontrados = []
    print("Introduce el hash md5 que buscas")
    hash_objetivo = input()
    directorio = os.listdir('/home/ander/fotos')
    indice = 0
    for elemento in directorio:
        indice= indice+1
        print(indice)
        path_archivo = os.path.join("/home/ander/fotos", elemento)
        with open(path_archivo, 'rb') as archivo:
                contenido = archivo.read()
                hash_archivo = hashlib.md5(contenido).hexdigest();
                print(str(indice) + " " + hash_archivo)
        if hash_objetivo == hash_archivo:
             print("El archivo nº " + str(indice) + "coincide, buscando mas hash que coincidan...")
             encontrados.append(indice)
    print("Nº de los elementos con el mismo hash:")
    print(encontrados)
                
if __name__ == "__main__":
    main()
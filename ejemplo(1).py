
def imprimir_lista(a):
    for i in a:
        print("id : ",i[0]," Nombre : ",i[1]," Precio : ",i[2])
        print(".-.-.-.")

listita=[[1,'mesa',55000],[2,'silla',90000]]
acumulador=0
for x in listita:
    acumulador=x[2]+acumulador

cantidad=len(listita)
imprimir_lista(listita)
promedio=acumulador/cantidad
print("La suma de ls precios es : ",acumulador)
print("Hay actualmente ",cantidad," productos")
print("El precio promedio es : ",promedio)

'''
def imprimir_diccionario(d):
    for x in d:
        print("id : ",x["id"], "Detalle : ",x["nombre"])

listita=[{"id":1,"nombre":"mesa","precio":55000},
         {"id":2,"nombre":'silla',"precio":90000}]



imprimir_diccionario(listita)

'''

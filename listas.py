l = [3,"tres",True,["uno",10]];

l[2] = 4;

l2 = l[1] #elemento en la posicion 1

l3 = l[3][0] #elemento de una lista que esta en otra lista

listaCopia = l[0:3] #se copian los elementos de l desde la posicion 0 hast la posicion 2
					#si se deja sin rango se copiaran todos los elementos
listaCopia1 = l[1::2]#se Incluye un salto de 2 en dos "uno si y uno no"

l[0:2] = [4,3] #se reemplezan los elementos de una lista que estan en el rango 0:2

print (l2);
print(l3)
print(l[2])
print(listaCopia)
print(listaCopia1)
print(l)
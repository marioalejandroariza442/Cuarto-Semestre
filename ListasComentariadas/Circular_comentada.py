#Definicion de la clase nodo: representa un elemento de la lista circular
class Nodo:
    def __init__(self, dato):
        self.dato=dato             #Guarda el valor o dato del nodo
        self.siguiente=None        #Referencia al siguiente nodo

#Clase Circular: Maneja la estructura de la lsita circular 
class Circular:
    def __init__(self):
        self.primero=None          #Apunta al primer nodo de la lista
        self.cont=0                #Contador de elementos en la lista 

#Metdo para agregar un nuevo nodo al final de la lista circular  
    def agregar(self,dato):
        nuevo=Nodo(dato)           #Se crea un nuevo nodo con el dato recibido 

        #Si la lista esta vacia, el nuevo nodo sera el primero y apuntara a si mismo
        if not self.primero:
            self.primero=nuevo
            nuevo.siguiente=self.primero
        else:

            #Si ya hay elementos, recorremos hasta el ultimo nodo
            actual=self.primero
            while actual.siguiente !=self.primero:
               actual=actual.siguiente
               self.cont+=1        #Incrementa el contador al recorrer 

            #Se inserta el nuevo nodo al final y se cierra el ciclo apuntando al primero    
            actual.siguiente=nuevo
            nuevo.siguiente=self.primero
            self.cont+=1           #Aumenta el contador total de nodos

    #Metodo para mostrar todos los elementos de la lista circular            
    def mostrar(self):
        actual=self.primero
        i=0

        #Recorre la lista imprimiendo los datos de cada nodo hasta llegar de nuevo al primero 
        while actual and i< self.cont:
            print(actual.dato)
            actual=actual.siguiente
            i+=1
            
#Ejemplo de uso:        
k=Circular()        #Se crea una lista circular vacia
k.agregar(12)       #Se agregan varios elementos
k.agregar(9)
k.agregar(88)
k.agregar(8800)
k.agregar(9988)
k.mostrar()         #Se muestran todos los datos de la lista
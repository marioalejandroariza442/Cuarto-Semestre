#Definicion de la clase NodoDoble, que representa un nodo en una lista doblemente enlazada
class NodoDoble:
    def __init__(self,dato):
        self.dato=dato                  #Valor que ingresa el nodo
        self.siguiente=None             #Apuntador al siguiente nodo (None)
        self.anterior=None              #Apuntador al nodo anterior (None)
        
#Definicion de la clase de la ListaDoble, que representa la lista doblemente enlazada
class ListaDoble:
    def __init__(self):
        self.cabeza=None                #Primer nodo de la lista (cabeza)
        self.cola=None                  #Ultimo nodo de la lista (cola)
        
    #Metodo para agregar un nodo al final de la lista     
    def agregar(self,dato):
        nuevo=NodoDoble(dato)           #Crea un nuevo nodo con el dato recibido
        if not self.cabeza:             #Si la lista esta vacia (no hay cabeza)
            self.cabeza=nuevo           #El nuevo nodo sera la cabeza
            self.cola=nuevo             #Y tambien la cola, porque es el unico nodo 
        else:
            
            #La cola actual debe apuntar al nuevo nodo como siguiente 
            self.cola.siguiente=nuevo
            #El nuevo apunta hacia atras a la cola actual
            nuevo.anterior=self.cola
            #Actualizar la cola para que sea el nuevo nodo
            self.cola=nuevo
    
    #Metodo para imprimir la lista desde la cabeza hacia adelante 
    def adelante(self):
        actual=self.cabeza             #Comienza desde la cabeza 
        while actual:                  #Mientras haya un nodo actual
            print(actual.dato)         #Imprime el dato almacenado
            actual=actual.siguiente    #Avanza al siguiente nodo
        print("None")                  #Imprime el fin de la lista
     
    #Metodo para imprimir la lista desde la cola hacia atras    
    def atras(self):
        actual=self.cola               #Comienza desde la cola 
        while actual:                  #Mientras haya un nodo actual
            print(actual.dato)         #Imprime el dato almacenado
            actual=actual.anterior     #Retrocede al nodo anterior 
        print("None")                  #Imprime el fin de la lista 

#Crea una instancia de ListaDoble
l1=ListaDoble()

#Agrega varios nodos con distintos datos
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

#Imprime la lista desde la cabeza hacia adelante 
l1.adelante()

#Imprime la lista desde la cola hacia atras
l1.atras()
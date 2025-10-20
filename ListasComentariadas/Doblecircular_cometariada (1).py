#Definicion de la clase NodoDoble, que representa un nodo de una lista doblemente enlazada
class NodoDoble:
    def __init__(self,dato):
        self.dato=dato              #Valor ingresado en el nodo
        self.siguiente=None         #Apuntador al siguiente nodo
        self.anterior=None          #Apuntador al nodo anterior 

#Definicion de la clase ListaDoble, que representa la lista doblemente enlazada
class ListaDoble:
    def __init__(self):
        self.cabeza=None            #Primer nodo de la lista
        self.cola=None              #Apuntador al siguiente nodo
        self.cont=0                 #Apuntador al nodo anterior
    
    #Metodo para agregar un nuevo nodo con el dato especificado al final de la lista
    def agregar(self,dato):
        nuevo=NodoDoble(dato)       #Crea un nuevo nodo con el dato
        if not self.cabeza:         #Si la lista esta vacia 
            self.cabeza=nuevo       #El nuevo nodo es la cabeza
            self.cola=nuevo         #Y tambien la cola (unico nodo)
        else:
            self.cola.siguiente=nuevo         #El siguiente de la cola apunta al nuevo nodo
            nuevo.anterior=self.cola          #El anterior del nuevo nodo apunta a la cola actual
            self.cola=nuevo                   #Actualizar la cola a este nuevo nodo
            
        #Hace que la lista sea circular    
        self.cola.siguiente=self.cabeza       #El siguiente de la cola apunta a la cabeza 
        self.cabeza.anterior=self.cola        #El anterior de la cabeza apunta a la cola 
        self.cont+=1                          #Incrementa el contador de nodos 
        
    #Metodo para recorrer hacia adelante desde la cabeza y mostrar los datos
    def adelante(self):
        actual=self.cabeza
        i=0
        while actual and i<self.cont:         #Recorrer solo hasta la cantidad de nodos
            print(actual.dato)                #Imprimir el dato del nodo actual
            actual=actual.siguiente           #Mover al siguiente nodo
            i+=1
        
    #Metodo para recorre hacia atras desde la cola y mostrar los datos    
    def atras(self):
        actual=self.cola
        i=0
        while actual and i<self.cont:         #Recorrer solo hasta la cantidad de nodos
            print(actual.dato)                #Imprimir el dato del nodo actual
            actual=actual.anterior            #Mover al nodo anterior
            i+=1
        
#Codigo de prueba: Crea una lista y agrega varios datos
l1=ListaDoble()
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

#Imprime los datos hacia adelante 
l1.adelante()
print("="*50)

#Imprime los datos hacia atras
l1.atras()
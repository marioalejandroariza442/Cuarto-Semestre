#Definicion de la clase nodo, que representa un nodo simple para una lista enlazada simple
class Nodo():
    def __init__(self,dato):
        self.dato=dato                 #Valor ingresado en el nodo
        self.siguiente=None            #Apuntador al siguiente nodo (None)

#Definicion de la clase Lista, que representa una lista enlazada simple
class Lista:
    def __init__(self):
        self.primero=None              #Inicialmente la lista esta vacia, sin primer nodo
    
    #Metodo para agregar un nuevo nodo al final de la lista    
    def agregar(self,dato):
        nuevo=Nodo(dato)               #Crear un nuevo nodo con el dato
        if not self.primero:           #Si la lista esta vacia
            self.primero=nuevo         #El nuevo nodo sera el primero 
        else:
            actual=self.primero   
            
            #Recorrer la lista hasta el ultimo nodo         
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevo    #Agregar el nuevo nodo al final          
        return 1                      #Retorna 1 para indicar exito
    
    #Metodo para eliminar un nodo que tenga un dato especifico
    def eliminar(self,dato):
        actual=self.primero
        anterior=None
        
        #Buscar el nodo que tenga el dato buscado
        while actual and actual.dato!=dato:
            anterior=actual
            actual=actual.siguiente
        if not actual:
            return                   #Si no se encontro el nodo, salir sin hacer nada
        if not anterior:
            
            #Si el nodo a eliminar es el primero, actualizar la cabeza de la lista
            self.primero=actual.siguiente
        else:
            
            #Si el nodo esta en medio o al final, saltar al nodo a eliminar
            anterior.siguiente=actual.siguiente 
            
    #Metodo para imprimir todos los elementos de la lista 
    def imprimir(self):
        actual=self.primero
        while actual:
            print(actual.dato)       #Imprime el dato del nodo actual
            actual=actual.siguiente  #Avanza al siguiente nodo

#Crea una instancia de la lista 
lili=Lista()

#Agregar algunos elementos a la lista 
lili.agregar('k')
lili.agregar(999)
lili.agregar(1000)
    
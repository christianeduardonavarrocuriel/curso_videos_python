class Hello:

    def __init__(self):
        print("¡¡Hello World!!")
        
    def metodo(self):   
        print("Método")
        
"""
Aqui crearemos un método, lo crearemos escribiendo " def metodo(self): " recordemos que self sirve para que nuestro metodo tenga
acceso a las variables miembros de la clase y a los métodos miembros de la clase.
Después, imprimimos la palabra "Método"

"""

objeto = Hello()
##En esta parte, para que se imprima lo que queremos, necesitamos llamar al método, que en este caso se llamará "objeto.metodo"
objeto.metodo()

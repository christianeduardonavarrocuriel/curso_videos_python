##Primero creamos la clase y le ponemos el nombre a la clase, en este caso se llamará "hello"
class hello:

##Ahora, lo que haremos sera definir el método, que aqui el metodo sera "__init__", que tambien se le conoce como "método constructor"
    def __init__(self):
##Aqui, imprimiremos lo que queremos que se imprima, en este caso, queremos que se imprima "¡¡Hello World!!
        print("¡¡Hello World")


"""
Ahora, para que en realidad se imprima lo que queremos en la "Terminal", tenemos que definir el nombre del objeto,
que en este caso, se le llamara "saludo", despues le pondremos el signo "igual" "=" ya que nos ayudará a crear la instancia de
nuestra clase "hello", después el nombre de la clase para que se imprima lo que queremos, recordemos
en este programa se llama "hello", después agrgamos adelante del nombre de la clase los paréntesis
"""

saludo = hello()
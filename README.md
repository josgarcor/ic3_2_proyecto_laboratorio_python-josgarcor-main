
# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>)
Autor/a: \<Jose Manuel García Corrales\>   uvus:\<josgarcor5\>

## Estructura de las carpetas del proyecto


## Carpeta src

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **cars.py**: Este módulo contiene el código de los datos de los coches.
  * **cars_test.py**: Este módulo contiene el código test de los datos de los coches.
  * **parsers.py**: Este módulo contiene el código para parsear a cadena los elementos de tipo bool.

  
* **/data**: Contiene el dataset o datasets del proyecto
    * **all_parsed.csv**: Este fichero ".csv" contiene los datos de los coches.
    
  
    
## Estructura del *dataset*



El dataset está compuesto por 9 columnas, con la siguiente descripción:

* **Datetime**: de tipo DateTime, representa la fecha del registro.

* **Make**: de tipo String, representa la marca del coche.

* **Model**: de tipo String, representa el modelo del coche.

* **Year**: de tipo Integer, representa el año fabricación.
 
* **Engine**: de tipo Float, representa la potencia del motor.

* **Mileage**: de tipo Float, representa el kilometraje del coche.

* **Price**: de tipo Float, representa el precio.

* **Fuel_type**: de tipo String, representa el tipo de la gasolina.

* **New**: de tipo Boolean, representa si el coche es nuevo o no.


....

## Tipos implementados

Namedtuple: 

Cars = namedtuple("Cars","datetime,make,model,year,engine,mileage,price,fuel_type,new")


en la que los tipos de cada uno son los siguientes:


Cars(datetime.time, str, str, int, float, float, float, str, bool)

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas. El módulo principal es el módulo cars.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.

### Módulo cars
Entrega 1
* **Bloque 0**
* **leer_csv(fichero)**: Lee la nametupled "Cars" con sus diferentes valores y devuelve una lista de tuplas con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el módulo parsers:
* **parsebool(cad)**: Función para convertir de cadena a booleano.

* **Bloque 1** 
* **filtrar_marca_modelo(fichero, marca)**: Filtra según la marca del coche los modelos de los mismos y los añade a un conjunto.
* **calcular_media_precio_marca(fichero,marca)**: Calcula la media de los precios de los coches según la marca del mismo. 


* **Bloque 2** 
* **maximo_kilom_por_año(fichero,año=None)**: Recoge el máximo kilometraje de los vehiculos según el año. Función Auxiliar: "filtro_año_kilom(fichero,año)", permite filtrar kilometro/año.
* **n_precio_fuel(fichero, fuel, n)**: Según el tipo de fuel, recoge los n precios de los coches más altos.
* **dicc_marca_nuevo(fichero, año, nuevo)**: Diccionario que permite recoger el número de vehiculos nuevos o de segunda mano por año.


* **Bloque 3**
* **contar_km_segun_fuel_por_año(fichero,año)**: Recoge el número total de kilometros hechos segun el tipo de fuel en un año determinado.
* **max_km_fuel_año(fichero,año)**: Recoge el máximo y el mínimo valor de los kilometros segun el año.
* **dicc_porcentaje_km_por_año(fichero,año)**: Diccionario que como clave tiene el año dado y como valores el porcentaje segun los kilometros hechos.
* **dicc_top_n_coches_por_motor(fichero, n=3)**: Diccionario que como clave tiene el motor y como valores el top 3 coches con ese motor.


* **Bloque 4**
* **grafica(fichero)**: Nos devuelve una grafica en el que en el eje x nos encontramos el año y en el eje y los kilometros hechos.
### Módulo test

* **<test_leer_csv>**: Visualiza en pantalla el número total de registros leídos, los 3 primeros registros leídos y los 3 últimos registros leídos.
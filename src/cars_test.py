from cars import *

if __name__ == "__main__":
    Coches = leer_csv("data/all_parsed.csv")

"EJERCICIO 1"

def test_leer_csv():
    print("Leidos: ", len(Coches), "datos de coches")
    print("Registro 1:",Coches[0])
    print("Registro 2:",Coches[1])
    print("Registro 3:",Coches[2])
    print("Registros ultimos:")
    print(Coches[-1])
    print(Coches[-2])
    print(Coches[-3])



#test_leer_csv()

#----- BLOQUE 2 ---------------------------------------------------------------------------

"EJERCICIO 2"

def test_filtrar_marca_modelo():
    print("Coches por marca y modelo")
    print(filtrar_marca_modelo(Coches,"Porsche"))
    print(filtrar_marca_modelo(Coches,"Audi"))

"EJERCICIO 3"

def test_calcular_media_precio_marca():
    print("Calcular media de los precios por marca de coche")
    print(calcular_media_precio_marca(Coches,"Peugeot"),"€.")
    print(calcular_media_precio_marca(Coches,"Audi"),"€.")


#test_filtrar_marca_modelo()
#test_calcular_media_precio_marca()


#----- BLOQUE 3 ---------------------------------------------------------------------------



"EJERCICIO 4"

def test_maximo_kilom_por_año():
    print("Calculo maximo de kilometraje por año")
    print(maximo_kilom_por_año(Coches,2001))

def test_n_precio_fuel():
    print("Los 3 mayores precios según el tipo de fuel")
    print(n_precio_fuel(Coches,"H",3))


def test_dicc_marca_nuevo():
    print("Diccionario que muestra que devuelve según el año 2004 el numero total de coches nuevos")
    print(dicc_marca_nuevo(Coches,2004, True))
    print("Diccionario que muestra que devuelve según el año 2004 el numero total de coches de segunda mano")

    print(dicc_marca_nuevo(Coches,2004, False))



#test_maximo_kilom_por_año()
#test_n_precio_fuel()
#test_dicc_marca_nuevo()

#----- BLOQUE 4 ---------------------------------------------------------------------------
def test_contar_km_segun_fuel_por_año():
    print("Diccionario de los kilometros segun el fuel y el año 2008:",contar_km_segun_fuel_por_año(Coches,2008))
def test_max_km_fuel_año():
    print("Maximo y minimo kilometraje en el año 2008",max_km_fuel_año(Coches,2008))
def test_dicc_porcentaje_km_por_año():
    print("Diccionario que muestra el porcentaje de los kilometros por año, con clave Marca",dicc_porcentaje_km_por_año(Coches,2007))
def test_dicc_top_n_coches_por_motor():    
    print("Diccionario que muestra el top 3 de coches por motor",dicc_top_n_coches_por_motor(Coches))

#def test_grafica():
    #print("Grafica: ",grafica(Coches,2005))

test_contar_km_segun_fuel_por_año()
test_max_km_fuel_año()
test_dicc_porcentaje_km_por_año()
test_dicc_top_n_coches_por_motor()

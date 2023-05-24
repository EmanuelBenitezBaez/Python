"""
COMO CONVERTIR VARIABLE LOCAL EN GLOBAL
"""
#LLAMADA A LAS FUNCIONES


#DEFINICION DE FUNCION
#EN ESTE EJEMPLO LA FUNCION DEVUELVE UN RESULTADO FUERA DEL SCOPE DE LA FUNCION
#PARA ESO USAMOS LA PALABRA RESERVADA RETURN
#EL RETURN CORTA LA EJECUCIOND E LA FUNCION, CUALQUIER INSTRUCCION DEBAJO DE ELLA, NO SE EJECUTA

def suma(numero1,numero2):
 resultado = numero1 + numero2
 print (resultado)
 return resultado

resultadoDevuelto=suma(10,20)

print(resultadoDevuelto)

#LAS FUNCIONES TAMBIEN OUDEN DEVOLVER VARIOS VALORES

def operaciones(numero1,numero2):
    suma=numero1 + numero2
    resta=numero1 - numero2
    multiplica=numero1 * numero2
    division=numero1 / numero2
    return suma,resta,multiplica,division



sumas,resta,multiplica,division=operaciones(10,10)
print(sumas,resta,multiplica,division)
#FUNCIONES

"""
REGLAS GENERALES DE LAS FUNCIONES:
1- NO SE EJECUTA AL MENOS QUE LAS LLAMES.
2- LA PUEDO LLAMAR LAS VECES QUE QUIERA.
3- PRIMERO SE DEFINE LA FUNCION Y DESPUES SE LLAMA.
4-PRIMERO VAN LOS PARAMETROS REQUERIDOS Y AL FINAL LOS VALORES DEL PARAMETRO POR DEFAULT
"""
#TIPOS DE FUNCIONES
#SIN PARAMETROS
"""
def funcionSinParametro():
//conjunto de instrucciones 
"""
def derechosPersonas():
    
    print("Salud")
    print("Vida")
    print("Estudiar")

def derechosPersonasMayores():
    print("Voto")
    print("Otros derechos")
    print("Trabajo")
    



#LLAMADA DE LAS FUNCIONES

derechosPersonas() 
derechosPersonasMayores()

#FUNCIONES CON PRAMETROS
"""

def funcionConParametro(parametro1,parametro2):

 #instrucciones

"""
#LO QUE NOS PERMITE LOS PARAMETROS ES ENVIARLE VALORES O DATOS A LA FUNCION Y LAS USE DENTRO DE ELLA
#LA FUNCION VA A RECIBIR VALORES DESDE FUERA Y SE LOS ASIGNA A UNA VARIABLE , EN ESTE CASO ,LOS PARAMETROS

def mayoriaEdad(nombre,edad):
    print(f'Segun la edad  de {nombre} que es de {edad} años, sus derechos son:')

    if(edad>=18):
      derechosPersonas() 
      derechosPersonasMayores()
    else:
        derechosPersonas()


mayoriaEdad("Tatiana",10)    


#FUNCIONES CON PARAMETROS OPCIONALES//POR DEFECTO
"""
def parametrosOpcionales(parametro1,parametro2=pordefecto):
#instrucciones
"""

#LE DAMOS EL VALOR POR DEFECTO DENTRO DEL PARAMETRO, EN ESTE CASO 'X'
#EN RESUMEN SI NO SE LE PASA UN NOMBRE POR PARAMETRO, EL VALOR POR DEFECTO VA A SER 'X'
#POR REGLA EL VALOR DEL PARAMTRO POR DEFECTO VA SIEMPRE ULTIMO.
def mayoriaEdadParametroPorDefecto(edad,nombre='DESCONOCIDO'):
    print(f'Segun la edad  de {nombre} que es de {edad} años, sus derechos son:')

    if(edad>=18):
      derechosPersonas() 
      derechosPersonasMayores()
    else:
        derechosPersonas()

mayoriaEdadParametroPorDefecto(25)
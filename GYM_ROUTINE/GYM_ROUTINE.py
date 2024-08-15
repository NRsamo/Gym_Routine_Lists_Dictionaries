#Dictionary to store workout routines

import pprint

routine={   #Nombre de la variable que almacena un diccionario
    'Legs': [
        {'Exercise' : 'Barbell Squat','Sets' : 2,'Reps' : 12, 'Weight' : 140},    #Las llaves denotan un diccionario 
        {'Exercise' : 'Leg Extensions','Sets' : 2,'Reps' : 12, 'Weight' : 100}          #Los corchetes [ ] denotan una LISTA en este caso es una lista de diccionarios
        ],       #Cada elemento dentro de las listas {'Exercise' : 'Barbell squat'}.... es un diccionario con sus respectivos valores (: 2, :12....)
    'Chest' : [
        {'Exercise' : 'Incline Bench Press', 'Sets' : 2, 'Reps' : 12, 'Weight' : 100},  #Los nombres de las claves deben ser consistentes para evitar problemas de acceso
        {'Exercise' : 'DB Flies', 'Sets' : 2, 'Reps' : 12, 'Weight' : 22}
        ]
    }



#Function to show routine
def show_routine(rout):
    print(f"\nRoutine for {rout}:")
    print("\nCon pretty print\n")
    pprint.pprint(routine[rout]) #pprint Sirve para imprimir estructuras de datos de manera mas legible y es util cuando las estructuras son largas y 
    print("\nSin pretty print\n")
    for exerc in routine[rout]:
        print(f"- {exerc['Exercise']}:{exerc['Sets']} sets of {exerc['Reps']} reps with {exerc['Weight']} Kg")
        

# Function to check and add exercise if it doesn't exist using get()
def agregar_ejercicio(rout, exercise, sets, reps, weight):
    found = any(ex['Exercise'] == exercise for ex in routine[rout]) #esta es una funcion generadora que utiliza un ciclo for de forma condensada, seria lo mismo a escribir:
    #found = False
    #for ex in routine[rout]:
    #    if ex['Exercise'] == exercise:
    #        found = True
    #        break
    #La funcion generadora realiza la busqueda en una sola linea de codigo de una manera mas conscisa
    #el ciclo for extraera los valores correspondientes a rout en la biblioteca routine para cada valor extraido ex realizara una comparacion mediante la funcion any
    #especificamente en el nombre del ejercicio y lo comparara con exercise, si los nombres coinciden, found sera verdadero, de lo contrario pasara a la siguiente condicion if not found
    
    if not found: #si any no encuentra ninguna coincidencia entonces found es False, con la presencia de not, found se convierte en True, y se ejecuta la instruccion.
        routine[rout].append({'Exercise': exercise, 'Sets': sets, 'Reps': reps, 'Weight': weight}) #append es un metodo que agrega un nuevo elemento al final de una lista
        #El orden en que se ingresan los atributos esta hecho de forma posicional lo que significa que el argumento de la funcion debe contener los valores en el orden correcto
        #Si se desea ingresar atributos en cualquier orden, hay que indicarlo en los parametros de la funcion de manera explicita 
        #agregar_ejercicio(rout='Legs',sets=3,reps,10,exercise='Lunges',weight=60)
        
        print(f"\nEl ejercicio {exercise} se ha agregado a la rutina {rout}")
    else:
        print(f"\nEl ejercicio {exercise} ya existe en la rutina {rout}")

        
#Function for progress record using setdefault()
def registrar_progreso(rout,Exercise,series_completadas,peso_actualizado=None): #peso_actualizado tiene asignado por defecto un valor determinado en caso
    #en caso de que no se ingrese un nuevo valor
    

    for ex in routine[rout]: #Access to the exercises list in the specified routine for the muscular group
        if ex['Exercise']==Exercise:
            ex['series_completadas']=ex.setdefault('series_completadas',0)+series_completadas #se esta buscando acceder a la clave series_completadas en el diccionario routine
            #pero como la clave no existe entonces setdefault la agregara con un valor predeterminado de 0 mas el valor actual de series completadas si es que existe
            
            if peso_actualizado: #verifica si existe un nuevo valor para esta variable, si es asi entonces este valor se almacena en Weight
                ex['Weight']=peso_actualizado
            print(f"\nProgreso registrado:{Exercise} - {series_completadas} series completadas, peso actualizado a {ex['Weight']} Kg")
            break

#Function to calcula total Weight lifted in a routine using get()
def calcular_peso_total(rout):
    total_peso=0
    for Exercise in routine[rout]:
        total_peso += Exercise['Sets'] * Exercise['Reps'] * Exercise.get('Weight',0)
    print(f"\nPeso total levantado en la rutina de {rout}:{total_peso} Kg")
    

# Function to add or update progress with setdefault()
def actualizar_progreso(rout, exercise, progreso):
    for ex in routine[rout]:
        if ex['Exercise'] == exercise:
            ex['Progreso'] = ex.setdefault('Progreso', []) + [progreso] #se agrega un nuevo elemento que contiene el progreso. Como en este caso es una cadena de caracteres
            #la funcion setdefault agrega por defecto una lista vacia [], despues concatena esta lista con [progreso] utilizando el operador +
            print(f"\nProgreso actualizado para {exercise}: {ex['Progreso']}")
           #NOTA: cuando se trabaja con un valor numerico la operacion + suma directamente los valores
           #cuando se trabaja con listas, la operacion + concatena elementos a la LISTA existente no a la cadena, lo cual la lista va agregando valores en un nuevo slot 



# Check if an exercise exists in the routine
def verificar_ejercicio(rout, exercise):
    if any(ex['Exercise'] == exercise for ex in routine[rout]):
        print(f"\nEl ejercicio {exercise} existe en la rutina {rout}")
    else:
        print(f"\nEl ejercicio {exercise} no existe en la rutina {rout}")

# List all exercises in a routine
def listar_ejercicios(rout):
    ejercicios = [ex['Exercise'] for ex in routine[rout]]
    print(f"\nEjercicios en la rutina {rout}: {ejercicios}")

# Check all keys in a specific exercise dictionary
def listar_claves_ejercicio(rout, exercise):
    print("\nListar claves")
    for ex in routine[rout]:
        if ex['Exercise'] == exercise:
            lista=list(ex.keys())
            break
    #claves encontradas
    for clave in lista:
        print(clave)

            

#Compare between Lists and Dictionaries
def comparar_listas_diccionarios():
    #Ejemplo con listas
    lista_ejercicios=['Barbell Squat','Bench Press','Flys']
    print(f"\nLista de ejercicios: {lista_ejercicios}")
    print(f"\nPrimer ejercicio en la lista: {lista_ejercicios[0]}")
    
    #Ejemplo con diccionarios
    dict_ejercicios={
        'Legs' : 'Barbell Squat','Chest' : 'Bench Press', 'Back' : 'Pull Ups' 
        }
    print(f"\nDiccionario de ejercicios: {dict_ejercicios}")
    print(f"\nLeg workout : {dict_ejercicios['Legs']}")
    
    print(f"\nAgregar un ejercicio a la lista:")
    lista_ejercicios.append('Deadlift') #Recordar que para agregar un elemento a una LISTA se utiliza append
    print(f"\nLista de ejercicios actualizada: {lista_ejercicios}")
    
    print(f"\nAgregar un nuevo grupo muscular al diccionario:")
    dict_ejercicios['Shoulders'] = 'Military Press' #Recordar que para agregar un elemento a un DICCIONARIO se agrega o actualiza el par clave-valor den el diccionario
    print(f"\nDiccionario de ejercicios actualizado: {dict_ejercicios}")
    
    

#Using the functions
show_routine('Legs')
registrar_progreso('Legs','Barbell Squat', 2, peso_actualizado=160)
calcular_peso_total('Legs')
comparar_listas_diccionarios()
agregar_ejercicio('Legs', 'Lunges', 3, 10, 80)
actualizar_progreso('Legs', 'Barbell Squat', '2 series completadas')
verificar_ejercicio('Legs', 'Lunges')
listar_ejercicios('Legs')
listar_claves_ejercicio('Legs', 'Barbell Squat')
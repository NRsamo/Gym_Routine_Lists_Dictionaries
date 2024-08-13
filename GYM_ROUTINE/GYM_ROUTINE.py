#Dictionary to store workout routines
routine={
    'Legs': [
        {'Exercise' : 'Barbell Squat','Sets' : 2,'Reps' : 12, 'Weight' : 140},
        {'Exercise' : 'Leg Extensions','Sets' : 2,'Reps' : 12, 'Weight' : 100}
        ],
    'Chest' : [
        {'Exercise' : 'Incline Bench Press', 'Sets' : 2, 'Reps' : 12, 'Weight' : 100},  #Los nombres de las claves deben ser consistentes para evitar problemas de acceso
        {'Exercise' : 'DB Flies', 'Sets' : 2, 'Reps' : 12, 'Weight' : 22}
        ]
    }



#Function to show routine
def show_routine(rout):
    print(f"\nRoutine for {rout}:")
    for exerc in routine[rout]:
        print(f"- {exerc['Exercise']}:{exerc['Sets']} sets of {exerc['Reps']} reps with {exerc['Weight']} Kg")
        
#Function for progress record using setdefault()
def registrar_progreso(rout,Exercise,series_completadas,peso_actualizado=None):
    for ex in routine[rout]:
        if ex['Exercise']==Exercise:
            ex['series_completadas']=ex.setdefault('series_completadas',0)+series_completadas
            if peso_actualizado:
                ex['Weight']=peso_actualizado
            print(f"\nProgreso registrado:{Exercise} - {series_completadas} series completadas, peso actualizado a {ex['Weight']} Kg")
            break

#Function to calcula total Weight lifted in a routine using get()
def calcular_peso_total(rout):
    total_peso=0
    for Exercise in routine[rout]:
        total_peso += Exercise['Sets'] * Exercise['Reps'] * Exercise.get('Weight',0)
    print(f"\nPeso total levantado en la rutina de {rout}:{total_peso} Kg")
    

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
    lista_ejercicios.append('Deadlift')
    print(f"\nLista de ejercicios actualizada: {lista_ejercicios}")
    
    print(f"\nAgregar un nuevo grupo muscular al diccionario:")
    dict_ejercicios['Shoulders'] = 'Military Press'
    print(f"\nDiccionario de ejercicios actualizado: {dict_ejercicios}")
    
    

#Using the functions
show_routine('Legs')
registrar_progreso('Legs','Barbell Squat', 2, peso_actualizado=160)
calcular_peso_total('Legs')
comparar_listas_diccionarios()
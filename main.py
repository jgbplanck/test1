def vector_maximizado(vector):
    vector_skip = []
    for i in range(0, len(vector)):
        vector_skip.append(0)
    completado = False
    while (completado == False):
        completado = True
        for i in range(0, len(vector)):
            if vector_skip[i] == 0:
                completado = False
        vector_skip = eliminar_min(vector,vector_skip)
    
    vector_final = []
    for i in range(0, len(vector)):
        if vector_skip[i] != -1:
            vector_final.append(vector[i])
    print("Vector con los Skip:",vector_skip)

    return vector_final

def eliminar_min(vector,vector_skip):
    posicion_min = -1
    min=media(vector,vector_skip)
    for i in range(0, len(vector)):
        if vector_skip[i] == 0:
            if vector[i] < min:
                min = vector[i]
                posicion_min=i
    print("El mínimo es: ",min)
    print("Y está en la posición: ",posicion_min) 
    if posicion_min == -1:    
        for i in range(0, len(vector)):
            if vector_skip[i] == 0:
                vector_skip[i]=1
        return vector_skip  
    vector_skip[posicion_min]=-1
    if posicion_min - 1 >=0:
        if vector_skip[posicion_min - 1] == -1:
            vector_skip[posicion_min]=1
        else:
            vector_skip[posicion_min - 1]=1
    print("Vector de Skip Modificado: ",vector_skip)
    return vector_skip

def media (vector,vector_skip):
    media = 0
    for i in range(0, len(vector)):
        if vector_skip[i] != -1:
            media += vector [i]
    media = media / len(vector)
    print("La media ahora es: ",media)
    return media

# Programa principal
vector = [5,8,9,-2,-3,10,3,-200,3]
nuevo_vector = vector_maximizado(vector)

print("el vector de los más altos:", nuevo_vector)
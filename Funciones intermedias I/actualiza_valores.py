# Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
estudiantes[0]['last_name'] = 'Bryant'
directorio_deportes['fútbol'][0] = 'Andrés'
z[0]['y'] = 30
print("x:", x)
print("estudiantes:", estudiantes)
print("directorio_deportes:", directorio_deportes)
print("z:", z)

# Iterar a tarves de una lista de diccionarios 
def iterateDictionary(some_list):
    for diccionario in some_list:
        output = ""
        for key, value in diccionario.items():
            output += f"{key} - {value}, "
        output = output.rstrip(", ")
        print(output)
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(estudiantes)

# Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            print(diccionario[key_name])
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
print("Valores de 'first_name':")
iterateDictionary2('first_name', estudiantes)
print("\nValores de 'last_name':")
iterateDictionary2('last_name', estudiantes)

# Iterar a través de un diccionarios con valores de lista
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print()
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

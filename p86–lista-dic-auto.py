# Listas de diccionarios de autos
import os; os.system("Cls")

autos = [
    {'Marca':'Ford','modelo':'Mustang','año':1964},
    {'Marca':'Vw','modelo':'Jetta','año':2015},
]

autos.append({'marca':'Chevrolet','modelo':'Captiva','año':2024})

print('Todo:', autos, len(autos))

for auto in autos:
    print(auto)

print('\nDatos en forma de tabla')
for k in autos[0].keys():
    print(f'{k:<15} \t ', end='')

for auto in autos:
    for v in auto.values():
        print(f'{v:<15}\t', end='')
    print()

for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12}')
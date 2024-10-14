# Operaciones sobre conjuntos
import os; os.system('cls')

muns = {'Zacatecas', 'Guadalupe','Jerez','Fresnillo', 'Fresnillo'}

print('El conjunto : ', muns, len(muns))

print('\nLista de municipios: ')
for mun in muns:
    print(mun,end=' ')

print('\n¿Esta Zacatecas en los municipios? -', 'Zacatecas' in muns)
print('\nAgregra elementos a un conjunto:\n')

muns.add("Teul")
print('El conjunto : ', muns, len(muns))

mas = {'Luis Moya', 'Ojocaliente', 'Tepetongo', 'Rio Grande'}

muns.update(mas)
print('El conjunto : ', muns, len(muns))

muns.remove('Luis Moya')
print('El conjunto : ', muns, len(muns))

muns.discard('Luis Moya')
print('El conjunto : ', muns, len(muns))

mun = muns.pop()
print(mun)
print('El conjunto : ', muns, len(muns))

muns.clear()
print('El conjunto : ', muns, len(muns))










   
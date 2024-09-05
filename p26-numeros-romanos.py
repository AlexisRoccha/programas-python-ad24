'''Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano 
( I, II, III, IV, V, VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje 
de error. Ej. 11, número inválido, Ej: 4 , IV'''

import os; os.system("cls")

num = int(input("Ingresa el numero para decirte a que numero romano corresponde:  "))

if num == 1:
    print(f"El numero romano que le correponde al numero {num} es el I")
elif num == 2:
    print(f"El numero romano que le correponde al numero {num} es el II")
elif num == 3:
    print(f"El numero romano que le correponde al numero {num} es el III")
elif num == 4:
    print(f"El numero romano que le correponde al numero {num} es el VI")
elif num == 5:
    print(f"El numero romano que le correponde al numero {num} es el V")
elif num == 6:
    print(f"El numero romano que le correponde al numero {num} es el VI")
elif num == 7:
    print(f"El numero romano que le correponde al numero {num} es el VII")
elif num == 8:
    print(f"El numero romano que le correponde al numero {num} es el VIII")
elif num == 9:
    print(f"El numero romano que le correponde al numero {num} es el IX")
elif num == 10:
    print(f"El numero romano que le correponde al numero {num} es el X")
else:
    print("Error. Rango invalido")


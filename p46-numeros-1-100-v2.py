import os; os.system("cls")

"""print( list ( range(1, 10) ) )
print( list( range(1, 10, 2) ) )
print( list( range(1, 10, 3) ) )
print( list( range(1, 10, 3) ) )"""

n = int(input("Hasta donde?: "))
i = int(input("Incrementos de: "))

for x in range(1, n+1, i):
    print(x, end=" ")
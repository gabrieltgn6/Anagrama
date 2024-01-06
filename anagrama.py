"""

# Codigo para descubrir si una palabra es un anagrama o no


palabra1 = input(str ("Dime la palabra 1:"))
palabra2 = input(str ("Dime la palabra 2:"))

palabra1 = palabra1.lower()
palabra2 = palabra2.lower()

def is_anagrama (palabra1, palabra2):

    if palabra1 == palabra2[::-1]:
        return True
    else:
        return False





def is_palindromo (palabra1, palabra2):

    if sorted(palabra1) == sorted(palabra2):
        return True
    else:
        return False
    

print ("el palindromo es:")
print (is_palindromo(palabra1, palabra2 ))
print ("el anagrama es:")
print (is_anagrama(palabra1, palabra2))


"""
#Devuelve lista pares
import random



pares = []
rand_generados = []

cantidad_rand_nums = input("Cuantos valores quieres?:")
cantidad_rand_nums = int(cantidad_rand_nums)
print(cantidad_rand_nums)


def filtrado_pares (numeros):
    return[num for num in numeros if num%2 == 0 ]

for i in range (1, cantidad_rand_nums + 1):
    rand_numbs=random.randint(1, cantidad_rand_nums)
    rand_generados.append(rand_numbs)

pares = filtrado_pares(rand_generados)
print (f'los numeros generados son:{rand_generados}')
print (f'los numeros pares son: {pares}')
print (len(pares))
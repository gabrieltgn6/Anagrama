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


print (is_anagrama(palabra1, palabra2))


'''
Uso de callstacks para visualizar la recursión (o viceversa, supongo).
'''

def countdown(n: int):

    print(n)

    if n == 0:
        return None
    
    countdown(n - 1)


countdown(3) #Básicamente usar 3 Mr. Meeseeks para resolver un problema. (o 4 dependiendo de cómo lo ves).
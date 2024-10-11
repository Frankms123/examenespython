# -----------------------------------
# declaring local arrayList
# -----------------------------------
vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]
# -----------------------------------
# Declaring a joins functions
# -----------------------------------
def Join():
 salida = []
 for act in vec1:
     control = act in vec2
 if control:
    salida.append(act)
 return salida


def FullJoin():
 salida2 = vec1
 for act in vec2:
    control = act in salida2
 if not control:
    salida2.append(act)
 return salida2

def RightJoin():
    salida = []
    for act in vec2:
        if act in vec1:
            salida.append((act, act))
        else:
            salida.append((act, None)) 
    return salida

def FullOuterJoin():
    salida = []
    for act in vec1:
        if act in vec2:
            salida.append((act, act)) 
        else:
            salida.append((act, None))  
    for act in vec2:
        if act not in vec1:
            salida.append((None, act)) 
    return salida
# -----------------------------------
# Executing joins functions
# -----------------------------------
print(Join())
print('')
print(FullJoin())
print()
print(RightJoin())
print('')
print(FullOuterJoin())
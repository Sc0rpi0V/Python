# Un module en Python est simplement un fichier contenant du code Python. 
# Ce code peut contenir des fonctions, des classes, des variables, etc. 
# Les modules permettent d'organiser votre code de manière logique, et de le réutiliser facilement.


import packages.operations as operations
#from operations import division -> retrait de operations
#from operations import division, multiplication

if __name__ == "__main__":
    resultSum = operations.sum(10,20)
    print(resultSum)
    resultMult = operations.multiplication(4,3)
    print(resultMult)

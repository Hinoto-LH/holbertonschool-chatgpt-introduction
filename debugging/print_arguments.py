#!/usr/bin/python3
import sys

# On commence à l'index 1 jusqu'à la fin
for arg in sys.argv[1:]:
    print(f"{arg}") # Une f-string permet d’insérer directement des variables ou 
                    # des expressions dans une chaîne de caractères, de manière simple et lisible.
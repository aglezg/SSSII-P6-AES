# ----------------------------------------------------------------
# Práctica 5: Multiplicación en SNOW3G y AES
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 31/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from functions import *
import sys

# Main
cleanTerminal()

# Lectura de opciones
print("\n PRÁCTICA 7: AES\n")

key = input("  Clave: ")
text = input('  Bloque de texto original: ')
print()
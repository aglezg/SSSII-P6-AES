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

# Comprueba si la cadena únicamente posee dígitos hexadecimales
def isHexadecimalString(string):
  hexadecimal_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
  'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
  for char in string:
    if (char in hexadecimal_digits) == False:
      return False
  return True

# Transforma una cadena de 16 bytes en una matriz
def stringToMatrix(string):
  matrix = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
  vector = list(string)
  i = 0
  j = 0
  it = 0
  while (i < len(matrix)):
    while (j < len(matrix[i])):
      matrix[j][i] = vector[it] + vector[it + 1]
      j += 1
      it += 2
    j = 0
    i += 1
  return matrix


# Main
cleanTerminal()

# Lectura de opciones
print("\n PRÁCTICA 7: AES\n")

key = input("  Clave: ")
if (len(key) != 32 or isHexadecimalString(key) == False):
  sys.exit('La clave introducida no es correcta...')
text = input('  Bloque de texto original: ')
if (len(text) != 32 or isHexadecimalString(text) == False):
  sys.exit('El texto introducido no es correcta...')
print()

# Transformamos las cadenas leídas en matrices
key_matrix = stringToMatrix(key)
text_matrix = stringToMatrix(text)

# Etapa inicial
print(' # Etapa inicial:\n')
print('Key:\n')
show(key_matrix)
print('\nBloque de texto tras "AddRoudKey":\n')
text_matrix = addRoundKey(text_matrix, key_matrix)
show(text_matrix)
print()

# 9 iteraciones
print(' # 9 iteraciones (SubBytes-ShiftRows-MixColumns-AddRoundKey):\n')
for i in range(9):
  print('SubKey ' + str(i + 1) + ':\n')
  key_matrix = keyExpansion(key_matrix, i)
  show(key_matrix)
  print('\nBloque de texto tras la iteración ' + str(i + 1) + ':\n')
  text_matrix = subBytes(text_matrix)                # SubBytes
  text_matrix = shiftRow(text_matrix)                # ShiftRows
  text_matrix = mixColumns(text_matrix)              # MixColumns
  text_matrix = addRoundKey(text_matrix, key_matrix) # AddRoundKey
  show(text_matrix)
  print()

# Etapa final
print(' # Etapa final:\n')
print('SubKey 10:\n')
key_matrix = keyExpansion(key_matrix, 9)
show(key_matrix)
print('\nBloque de texto cifrado:\n')
text_matrix = subBytes(text_matrix)                # SubBytes
text_matrix = shiftRow(text_matrix)                # ShiftRows
text_matrix = addRoundKey(text_matrix, key_matrix) # AddRoundKey
show(text_matrix)
print()

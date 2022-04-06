# ----------------------------------------------------------------
# Práctica 5: Multiplicación en SNOW3G y AES
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 31/03/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo de las funciones
# implementadas enla práctica.
# ----------------------------------------------------------------

import string
import os

HEXADECIMAL_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
  'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

# S-Caja utilizada para la operación 'SubBytes'
SBOX = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
         ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
         ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
         ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
         ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
         ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
         ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
         ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
         ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
         ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
         ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
         ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
         ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
         ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
         ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
         ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

# Matriz empleada para la multiplicación en MixColumn
MIXCOLUM_MATRIX = [['02', '03', '01', '01'],
                   ['01', '02', '03', '01'],
                   ['01', '01', '02', '03'],
                   ['03', '01', '01', '02']]

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Rota elementos de un array
# d: Indica los 'd' primeros elementos a rotar
def rotateArray(array, d):
  result = array.copy()
  dCopy = d
  temp = []
  i = 0
  while (i < d):
    temp.append(array[i])
    i += 1
  i = 0
  while (dCopy < len(array)):
    result[i] = array[dCopy]
    i += 1
    dCopy += 1
  result = result[: i] + temp
  return result

# SubBytes
def subBytes(matrix):
  result = []
  i = 0
  j = 0
  while (i < len(matrix)):
    resultRow = []
    while (j < len(matrix[i])):
      resultRow.append(SBOX[int(matrix[i][j][0], 16)][int(matrix[i][j][1], 16)])
      j += 1
    j = 0
    i += 1
    result.append(resultRow.copy())
  
  return result

# ShiftRow
def shiftRow(matrix):
  result = matrix.copy()
  i = 0
  while (i < len(matrix)):
    result[i] = rotateArray(result[i], i)
    i += 1
  return result

# MixColumn
def MixColumn(matrix, constant_matrix = MIXCOLUM_MATRIX):
  

# Imprime por pantalla la matriz
def show(matrix):
  i = 0
  j = 0
  while (i < len(matrix)):
    while (j < len(matrix[i])):
      print(matrix[i][j] + ' ', end='')
      j += 1
    j = 0
    i += 1
    print()


matriz_ejemplo = [['33', '0a', '74', '0a'],
                  ['81', '52', '59', '49'],
                  ['0d', '05', '5d', '47'],
                  ['12', '45', '4c', '43']]

show(subBytes(matriz_ejemplo))
print()
show(shiftRow(subBytes(matriz_ejemplo)))







# Constantes
#SNOW3G_byte = '10101001'
#AES_byte = '00011011'
#
HEXADECIMAL_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
  'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
#
## Comprueba si un cadena es un número hexadecimal
#def isHexadecimalDigit(hexa: string):
#  for digit in hexa:
#    if (digit in HEXADECIMAL_DIGITS == False):
#      return False
#  return True
#
## Convertir de hexadecimal a binario
#def hexaToBin(hexa: string):
#  result = ''
#  for digit in hexa:
#    if (isHexadecimalDigit(digit) == False):
#      return None
#    result += str(bin(int(digit, 16))[2:].zfill(4))
#  return result
#
## Comprueba que una cadena sea un byte, esto es que sea una cadena
## de 1's y 0's con longitud 8
#def isByte(byte: string):
#  if (len(byte) != 8):
#    return False
#  else:
#    for bit in byte:
#      if (bit != '1' and bit != '0'):
#        return False
#    return True
#
## Devuelve una lista con los índices de aquellas posiciones que tengan
## valor 1 de un byte introducido por parámetro
#def getByteIndexsWithValue1(byte: string):
#  if (isByte(byte) == False):
#    return None
#  result = []
#  it = len(byte)
#  while it > 0:
#    if (byte[it - 1] == '1'):
#      result.append(len(byte) - it)
#    it -= 1
#  return result
#
## Realiza la operación XOR sobre 2 bytes
## Estos deben ser cadenas de 1's y 0's de longitud 8
#def XORBytes(byte1, byte2):
#  if (isByte(byte1) == False or isByte(byte2) == False):
#    return None
#  else:
#    result = ''
#    it = 0
#    while (it < len(byte1)):
#      if (byte1[it] == byte2[it]):
#        result += '0'
#      else:
#        result += '1'
#      it += 1
#    return result
#
## Realiza el desplazamiento del algoritmo.
## El byte y la constante introducidas deben expresarse como cadena de 8 bits
#def shiftByte(byte, const, printable = False):
#  if (isByte(byte) == False or isByte(const) == False):
#    return None
#  if (byte[0] == '0'):
#    if (printable):
#      print('     ' + byte[1:] + '0')
#    return byte[1:] + '0'
#  else:
#    if (printable):
#      print('     ' + byte[1:] + '0' + ' + ' + const + ' = ' + XORBytes(byte[1:] + '0', const))
#    return XORBytes(byte[1:] + '0', const)
#
## Multiplicación binaria de 2 bytes
## Los bits deben ser enteros de 8 bits
#def binaryByteMultiplication(byte1, byte2, const, printable = False):
#  result = '00000000'
#  iterableByte = str(byte1)
#  it = 0
#  while (it <= max(getByteIndexsWithValue1(byte2))):
#    if (printable):
#      print('\n   > Step ' + str(it) + ':')
#    if (it in getByteIndexsWithValue1(byte2)):
#      result = XORBytes(result, iterableByte)
#    iterableByte = shiftByte(iterableByte, const, printable)
#    it += 1
#  return result
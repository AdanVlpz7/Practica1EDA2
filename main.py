import random
import math
from timeit import timeit

print("***** Practica 1 *****")
print("Este es un programa que tiene las funciones de BubbleSort, BubbleSort Optimizado y MergeSort")

def measure_time(func, *args, **kwargs):
    globals_ = {'func': func, 'args': args, 'kwargs': kwargs}
    time = timeit('func(*args, **kwargs)',
                  number=1,
                  globals=globals_)
    return f"{time} seconds"

def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                #aux = arr[j]
                #arr[j] = arr[j + 1]
                #arr[j + 1] = aux
                #Sintatic Sugar
                arr[j], arr[j+1] = arr[j+1], arr[j]


def BubbleSortOpt(arr):
    n = len(arr)
    i = 1
    j = 0
    ordenado = False
    while(i < n) or (ordenado == False):
      i += 1
      ordenado = True
      for j in range(n-i-1):
        if(arr[j] > arr[j+1]):
          ordenado = False
          aux = arr[j]
          arr[j] = arr[j+1]
          arr[j+1] = aux

def MergeSort(arr, p , r):
  if p < r:
    q = math.floor((p + r) / 2)
    MergeSort(arr,p,q)
    MergeSort(arr,q+1,r)
    Merge(arr,p,q,r)


def Merge(arr, p , q, r):
  #Sintatic Sugar
  izq = arr[p:q+1]
  der = arr[q + 1: r+1]
  i = 0
  j = 0
  for k in range(p,r+1):
    if(j >= r - q) or (i < q - p + 1) and (izq[i] < der[j]):
      arr[k] = izq[i]
      i+=1
    else:
      arr[k] = der[j]
      j+=1

def Aleatoria(arr, n):
  i = 0
  for i in range(n):
    arr.append(random.randint(0,10))
  return arr

def Ascendente(arr,n):
  i = 0
  for i in range(n):
    arr.append(i)
  return arr

def Descendente(arr, n):
  j = n
  while j > 0:
    arr.append(j)
    j -= 1
  return arr

# creacion de arreglo
n = 20000
a = []
#a = Ascendente(a,n) #mejor caso:D
a = Descendente(a,n) #peor caso:(
#a = Aleatoria(a,n) #caso promedio

print("\nCon n={0}.(peor caso)".format(n))
# copias de arreglo 
a1 = a[:]
a2 = a[:]
a3 = a[:]
#print("\nArreglo original desordenado: \n", a)

#BubbleSort ejecucion
print("\nEl tiempo de ejecucion de BubbleSort es: \n") 
BubbleSort(a1)
print(measure_time(BubbleSort,a1))
#print("\nArreglo original ordenado: \n", a1)

#BubbleSort optimizado ejecucion
print("\nEl tiempo de ejecucion de BubbleSort Optimizado es: \n") 
#BubbleSortOpt(a2)
print(measure_time(BubbleSortOpt,a2))
#print("\nArreglo original ordenado: \n", a2)

#MergeSort ejecucion
print("\nEl tiempo de ejecucion de MergeSort es: \n")
MergeSort(a3,0,len(a)- 1)
print(measure_time(MergeSort,a3,0,len(a3)- 1))
#print("\nArreglo original ordenado: \n", a3)
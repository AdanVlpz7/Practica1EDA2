import math
import random

print("Este es un programa que tiene la función MergeSort")

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
      


n = 10
a = []
for i in range(n):
  a.append(random.randint(0,10))
print("Arreglo desordenado: ", a)
MergeSort(a,0,len(a)- 1)
print("Arrelgo ordenado: ", a)

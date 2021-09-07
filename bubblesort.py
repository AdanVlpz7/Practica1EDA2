import random

print("Este es un programa que tiene la función BubbleSort")

def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                #aux = arr[j]
                #arr[j] = arr[j + 1]
                #arr[j + 1] = aux
                #Sintatic Sugar
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = 10
a = []
for i in range(n):
  a.append(random.randint(0,10))
print("Arreglo desordenado: ", a)
BubbleSort(a)
print("Arrelgo ordenado: ", a)

import math     # untuk fungsi sqrt
import random   # untuk fungsi random

# fungsi untuk mengurutkan array berdasarkan nilai x
def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j][0] > array[j+1][0]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# fungsi untuk menginputkan banyak dimensi dan titik secara random
def inputan():
    array = []
    global dimensi
    global banyakTitik
    banyakTitik = int(input("   Banyaknya titik : "))
    while banyakTitik < 2:
        banyakTitik = int(input("   Input tidak valid! Banyaknya titik: "))
    dimensi = int(input("   Banyak dimensi  : "))
    while dimensi < 2:
        dimensi = int(input("   Input tidak valid! Banyak dimensi: "))
    for i in range(banyakTitik):
        temp =[]
        for j in range(dimensi):
            titik = round(random.uniform(-100, 100), 2)
            temp.append(titik)
        array.append(temp)
    return (sort(array))

# fungsi untuk menghitung jarak euclidean
def EuclideanDistance(array, countEdDnC):
    #mencari jarak euclidean dimensi > 2
    dimensi = len(array[0])
    if dimensi > 2:
        jarak = 0
        for i in range(dimensi):
            jarak += (array[0][i]-array[1][i])**2
        jarak = math.sqrt(jarak)
        closest = [array[0], array[1]]
    #mencari jarak euclidean dimensi 2
    else:
        jarak = math.sqrt((array[0][0]-array[1][0])**2 + (array[0][1]-array[1][1])**2)
        closest = [array[0], array[1]]
    countEdDnC += 1
    return closest, jarak, countEdDnC

# fungsi untuk membagi suatu array menjadi 2 array
def divide(array):
    A1 = []
    A2 = []
    for i in range(len(array)):
        if i < (len(array)//2):
            A1.append(array[i])
        else:
            A2.append(array[i])
    return A1, A2

# fungsi untuk mencari pasangan titik terdekat dengan divide and conquer
def FindClosestPair(array, countEdDnC):
    if len(array) == 2:
        closest, distance, countEdDnC = EuclideanDistance(array, countEdDnC)
    elif len(array) == 3:
        twoPoint1, distance1, countEdDnC = EuclideanDistance([array[0], array[1]], countEdDnC)
        twoPoint2, distance2, countEdDnC = EuclideanDistance([array[0], array[2]], countEdDnC)
        twoPoint3, distance3, countEdDnC = EuclideanDistance([array[1], array[2]], countEdDnC)
        distance = min(distance1, distance2, distance3)
        if distance == distance1:
            closest = twoPoint1
        elif distance == distance2:
            closest = twoPoint2
        else:
            closest = twoPoint3
    else:
        S1, S2 = divide(array)
        twoPoint4, distance1, countEdDnC = FindClosestPair(S1, countEdDnC)
        twoPoint5, distance2, countEdDnC = FindClosestPair(S2, countEdDnC)
        distance = min(distance1, distance2)
        twoPoint, distance, countEdDnC = Sstrip(array, distance, countEdDnC)
        if distance == distance1:
            closest = twoPoint4
        elif distance == distance2:
            closest = twoPoint5
        else:
            closest = twoPoint
    return closest, distance, countEdDnC

# fungsi untuk mencari titik terdekat pada suatu strip
def Sstrip(array, distance, countEdDnC):
    closest = []
    if (len(array) % 2 == 1):
        middle = array[len(array)//2][0]
    else :
        middle = (array[len(array)//2][0] + array[(len(array)//2)+1][0])/2
    temp = []
    for i in range(len(array)):
        if (array[i][0] <= middle + distance and array[i][0] >= middle - distance):
            temp.append(array[i])
    for i in range (len(temp)):
        for j in range (i+1, len(temp)):
            array, dist, countEdDnC = EuclideanDistance([temp[i], temp[j]], countEdDnC)
            if dist < distance:
                distance = dist
                closest = [temp[i], temp[j]]
            else :
                continue
    return closest, distance, countEdDnC

# fungsi untuk mencari pasangan titik terdekat dengan brute force
def bruteForce(array):
    #mencari jarak euclidean terdekat dari banyak pasang titik
    distance = 999999
    countEdBF = 0
    for i in range(len(array)):
        for j in range(1+i, len(array)):
            if i != j:
                twoPoint, distance1, countEdBF = EuclideanDistance([array[i], array[j]], countEdBF)
                if distance1 < distance:
                    distance = distance1
                    closest = [array[i], array[j]]
                else :
                    continue
    return closest, distance, countEdBF

# fungsi untuk menampilkan hasil
def hasil(array, distance, time, countEd):
    print(" ")
    print("   Titik 1          = ", end=" ")
    for i in range (len(array[0])):
        print(array[0][i], end="  ")
    print(" ")
    print("   Titik 2          = ", end=" ")
    for i in range (len(array[0])):
        print(array[1][i], end="  ")
    print(" ")
    print("   Jarak            = ", distance)
    print("   Waktu Eksekusi   = ", time)
    print("   Banyak Operasi Euclidean Distance = ", countEd)
    print(" ")
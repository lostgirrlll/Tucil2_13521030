import os                   # untuk fungsi clear screen
import time                 # untuk fungsi time
import visualize as v       # untuk memanggil fungsi yang ada di file visualisasi
import splashScreen as s    # untuk memanggil fungsi yang ada di file splashScreen
import function as f        # untuk memanggil fungsi yang ada di file function

def main():
    os.system('cls')

    s.output(1)

    array = f.inputan()
    countEdDnC = 0

    # Find Closest Pair with Divide and Conquer
    s.output(2)    
    start = time.time()
    twoPointDnC, distanceDnC, countEdDnC = f.FindClosestPair(array, countEdDnC)
    end = time.time()
    DnCTime = end-start
    f.hasil(twoPointDnC, distanceDnC, DnCTime, countEdDnC)

    # Find Closest Pair with Brute Force
    s.output(3)
    start1 = time.time()
    twoPointBF, distanceBF, countEdBF = f.bruteForce(array)
    end1 = time.time()
    BFTime = end1-start1
    f.hasil(twoPointBF, distanceBF, BFTime, countEdBF)

    # Visualisasi
    v.Visualization(array, twoPointDnC)

    print(" ")
    clear = str(input("   Apakah anda ingin menginput kembali? (y/n) : "))
    if clear == "y" or clear == "Y":
        main()
    else:
        os.system('cls')
        s.output(1)
        s.output(4)

if __name__ == "__main__":
    main()

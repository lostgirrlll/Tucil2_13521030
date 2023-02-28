import numpy as np  # library untuk operasi vektor dan matriks
import matplotlib.pyplot as plt # library untuk visualisasi data
import function as f # library untuk fungsi-fungsi yang dibutuhkan

# fungsi untuk menampilkan hasil dalam bentuk grafik 2D/3D
def Visualization(array, arrayDnC):
    if f.dimensi == 3:
        visualisasi = str(input("   Tampilkan penggambaran semua titik dalam bidang 3D? (y/n) : "))
        if visualisasi == "y" or visualisasi == "Y":
            titik1 = array

            titik1.remove(arrayDnC[0])
            titik1.remove(arrayDnC[1])
            
            dots = np.array(titik1)
            DnC = np.array(arrayDnC)

            fig = plt.figure(figsize = (10,5.5))
            ax = plt.axes(projection='3d')
            ax.grid()
            if (len(dots)!= 0):
                ax.scatter(dots[:,0], dots[:,1], dots[:,2], s = 7.5, alpha = 0.5, edgecolors = 'grey', color = 'yellow')
            ax.scatter(DnC[:,0], DnC[:,1], DnC[:,2], s = 15, color = 'red', marker = 'o', edgecolors = 'black')   
            ax.set_title('3D Scatter Plot')

            ax.set_xlabel('x', labelpad=20)
            ax.set_ylabel('y', labelpad=20)
            ax.set_zlabel('z', labelpad=20)

            plt.show()

    elif f.dimensi == 2:
        visualisasi = str(input("   Tampilkan penggambaran semua titik dalam bidang 2D? (y/n) : "))
        if visualisasi == "y" or visualisasi == "Y":
            titik1 = array
            titik1.remove(arrayDnC[0])
            titik1 = array
            dots = np.array(titik1)
            DnC = np.array(arrayDnC)
        
            plt.rcParams["figure.figsize"] = [7.50, 3.50]
            plt.rcParams["figure.autolayout"] = True
            if (len(dots)!= 0):
                plt.scatter(dots[:, 0], dots[:, 1], color = 'green', s = 15)
            plt.scatter(DnC[:, 0], DnC[:, 1], color = 'red', s = 30)

            plt.show()
    else:
        print("   Maaf, Program hanya bisa menampilkan visualisasi pada bidang 2D dan 3D.")
    
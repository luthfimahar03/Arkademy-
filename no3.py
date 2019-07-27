print("------Panjang------")
def gambar(angka):
        bagi = int(angka/2)
        for i in range(1, bagi+1):
            print("*", end = "   ")
            for j in range(1, angka-2+1):
                print("=", end="   ")
            print("*")
            print()

        for k in range(1, 2):
            print("*", end = "   ")
            for j in range(1, angka-2+1):
                print("*", end="   ")
            print("*")
            print()

        for i in range(1, bagi+1):
            print("*", end = "   ")
            for j in range(1, angka-2+1):
                print("=", end="   ")
            print("*")
            print()

gambar(7)

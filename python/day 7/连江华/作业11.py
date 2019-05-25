for i in range(1,4):
    for j in range(1,6):
        if i==1 :
            if j==1 or j ==2:
                print("○",end="")

            elif j == 4 or j == 5:
                print(" ", end="")

            else:
                print("▲", end="")
        elif i == 2:
            if j == 1 :
                print("○", end="")
            elif j == 5:
                print(" ", end="")
            else:
                print("▲", end="")

        else:
            print("▲", end="")


    print()
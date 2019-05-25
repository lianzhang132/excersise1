for i in range(1,5):
    for j in range(1,7):
        if i ==1 or i ==4:
            print("□",end="")
        if i == 2 or i ==3:
            if j ==2 or j ==3 or j ==4 or j ==5 :
                print("●", end="")
            else:
                print("□", end="")

    print()





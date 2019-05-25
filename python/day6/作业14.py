n =100
for a in range(1,21):
    for b in range(1,34):
        for c in range(1,101):
            if a+b+c==100:
                if 5*a+3*b+c/3==100:
                    print("买公鸡", a, "个")
                    print("买母鸡", b, "个")
                    print("买小鸡",c , "个")
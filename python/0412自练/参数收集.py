def box(x ,y ,z,**args):
    print(args)

    return args

a = box(1,2,3,can=4,ah = 5,huo =6,jdsa =7,sdfa=8)
print(type(a))
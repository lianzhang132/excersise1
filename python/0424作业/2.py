import pickle
str1 = "adfandsker"
file = open("wenjian1","rb")
# pickle.dump(str1,file)
print(pickle.load(file))
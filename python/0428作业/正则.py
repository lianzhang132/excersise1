import re
card = '412823199704294016 fakdjasf flkjdska fe544f fads4555f 545147747 abc abc'
rel1 = "[0-9]+|[a-z]{3}"
rel2 = "[^0-9]+"
rel3 = "[0-9]?"
rel4 = "\s"
# print(re.findall(rel4,card))

# res = re.sub("fa","FA",card)
res = re.split("fa",card)
print(res)
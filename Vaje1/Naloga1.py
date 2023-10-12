import random

vnos = input("Vnesi število: ")
n = int(vnos)
polje = []
while len(polje) < n:
    polje.append(random.randint(1, 100))
print("Polje naključnih naravnih števil od 1 do 100 dolžine vnosa: "+ str(polje))
urejen = []
while polje != []:
    m = max(polje)
    polje.remove(m)
    urejen.append(m)

print("Isto polje, urejeno padajoče: "+ str(urejen))



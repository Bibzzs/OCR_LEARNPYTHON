# Test pour savoir si une année est bissextile

annee = input("Saissisez une année: ")

annee = int(annee)

#print(type(annee))
bissextile = False

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	bissextile=True

if bissextile:
	print(annee, " est bissextile. \n")
else:
	print(annee, " n'est pas bissextile. \n")



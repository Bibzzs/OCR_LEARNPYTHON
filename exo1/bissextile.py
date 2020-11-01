# Test pour savoir si une année est bissextile

annee = input("Saissisez une année: ")

annee = int(annee)

#print(type(annee))
bissextile = False
if annee % 4 == 0:
	if annee % 100 == 0:
		if annee % 400 == 0:
			bissextile = False
	else :
		bissextile = True

if bissextile:
	print(annee, " est pas bissextile. \n")
else:
	print(annee, " n'est pas bissextile. \n")

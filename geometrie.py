a = str(input("Votre forme : "))

if a == "carre" :
	b = str(input("Surface ou Périmètre ? "))
	if b == "surface" :
		c = int(input("Longueur du coté ? "))
		print("surface = " , c*c)
	if b == "perimetre" :
		c = int(input("Longueur du coté ? "))
		print("Périmetre = " , c*4)

if a == "rectangle" :
	b = str(input("Surface ou Périmètre ? "))
	if b == "surface" :
		c = int(input("Longueur ? "))
		d = int(input("Largeur ? "))
		print("surface = " , c*d)
	if b == "perimetre" :
		c = int(input("Longueur ? "))
		d = int(input("Largeur ? "))
		print("Périmetre = " , (c*d)*2)


if a == "cercle" :
	b = str(input("Surface ou Périmètre ? "))
	if b == "surface" :
		c = int(input("Rayon ? "))
		print("surface = " , 3.14*(c*c))
	if b == "perimetre" :
		c = int(input("Rayon ? "))
		print("Périmetre = " , 2*3.14*c)





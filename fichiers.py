import os

os.mkdir('developpement')
f = open("./developpement/developpement.txt",'w')
f.write("ce repertoire contiendra vos développements")
f.close()

os.mkdir('tests')
f = open("./tests/tests.txt",'w')
f.write("ce repertoire contiendra vos tests")
f.close()

os.mkdir('livraisons')
f = open("./livraisons/livraisons.txt",'w')
f.write("ce repertoire contiendra vos livraisons")
f.close()

os.mkdir('bugs')
f = open("./bugs/bugs.txt",'w')
f.write("ce repertoire contiendra les bugs rencontrés")
f.close()

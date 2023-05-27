import os
import subprocess as sp
import time
from os import remove
def abrir (programName,fileName):
	return sp.Popen([programName, fileName])
programName = "SII_Decrypt.exe"
fileName = "game.sii"
abrir(programName,fileName)
time.sleep(4)
os.rename('game.sii','game.txt')
trailer= " assigned_trailer: _nameless"
nameless= ''
cont=0
cont2=0
archivo= open('game.txt','r')
archivo2 = open('dat.txt','w')
for linea in archivo.readlines():
	if(trailer == linea[0:28]):
		archivo2.write(linea)
		nameless = 'trailer : ' + linea[19:-1] + ' {'
		cont = cont + 1
	else:
		cont = cont + 1
		if(linea[0:35] == nameless):
			cont2 = cont + 2
		if (cont2 == cont):
			archivo2.write(linea[0:13] + '-5000' + '\n')
		else:	
			archivo2.write(linea)
archivo.close()
archivo2.close()
remove('game.txt')
os.rename('dat.txt','game.sii')

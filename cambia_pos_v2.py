import os
import subprocess as sp
import time
from os import remove
def abrir (programName,fileName):
	return sp.Popen([programName, fileName])
programName = 'SII_Decrypt.exe'
fileName = 'game.sii'
abrir(programName,fileName)
time.sleep(4)
os.rename('game.sii','game.txt')
trailer_1 = ' trailers[0]: '
nameless_1 = ''
trailer_2 = ''
nameless_2 = ''
p = True
cont = 0
cont2 = 0
cont3 = 0
c_t=0
archivo = open('game.txt','r')
archivo2 = open('dat.txt','w')
for linea in archivo.readlines():
	cont += 1
	trailer_2 = ' trailers[' + str(c_t) + ']: '
	if(trailer_1 == linea[0:14] and p):
		nameless_1 = linea[-23:-1] + linea[-1]
		cont2 = cont
		p = False
	if(trailer_2 == linea[0:14] or trailer_2 == linea[0:15]):
		nameless_2 = linea[-23:-1] + linea[-1]
		cont3 = cont
	if(" trailers[" + str(c_t) + "]:" == linea[0:13] or " trailers[" + str(c_t) + "]:" == linea[0:14]):
		c_t +=1
cont = 0
archivo.close()
archivo = open('game.txt','r')
for lineas in archivo.readlines():
	cont += 1
	if(cont2 == cont):
		archivo2.write(' trailers[0]: _' + nameless_2)
	elif(cont3 == cont):
		archivo2.write(' trailers[' + str(c_t-1) + ']: _' + nameless_1)
	else:
		archivo2.write(lineas)
archivo.close()
archivo2.close()
remove('game.txt')
os.rename('dat.txt','game.sii')

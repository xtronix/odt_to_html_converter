#!/usr/bin/python3

import os
import base64

inpFile = 'prova_imm.html'
directory='images'

def sost_img(nameFileIn, nameFileOut):
	nImm = 0
	fileIn = open(nameFileIn, "r")
	fileOut = open(nameFileOut, 'w')

	while 1:
		riga = fileIn.readline()
		if riga == "":
			break
		indImm = riga.find('data:image/*;base64,')
		if indImm!=-1:
			nImm = nImm + 1
			#name of image
			if riga.find('id="'):
				nameImage = riga[riga.find('id="') + 4 : riga.find('"><img')]
				print(nameImage)
			else:
				nameImage = 'Immagine_'+ nImm
			# if not exist i create a folder "images"
			if not os.path.exists(directory):
				os.makedirs(directory)
			# create a file image base 64
#			fileImm = open(directory + '/' + nameImage + '.png', 'w')
#			fileImm.write(riga[indImm + 20 : riga.find('"/>', indImm)])
#			fileImm.close()
			# create a file image decoded
			fileImm = open(directory + '/' + nameImage + '.png', 'wb')
			imgData = str.encode(riga[indImm + 20 : riga.find('"/>', indImm)])
			fileImm.write(base64.b64decode(imgData))
			fileImm.close()
			riga = riga.replace(riga[indImm : riga.find('"/>', indImm)], directory + '/' + nameImage+ '.png')
			#print (riga)
		fileOut.write(riga)
	fileIn.close()
	fileOut.close()
	
	return

sost_img(inpFile, 'prova1.html')

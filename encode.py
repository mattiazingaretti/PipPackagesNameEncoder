import re


"""
Semplice script per la formattazione delle stringe dei nomi dei pacchetti  mostrati 
da pip (con il comando $ pip list ) in modo da 
generare un file chiamato 'requirements.txt' compatibile con il comando 

$ pip install -r requirements.txt

Assumption: I pacchetti da formattare (Con le eventuali versioni) sono contenuti 
            nel file 'comparison.txt'.  
Usage: python encode.py
Author: Mattia Zingaretti.
"""

f = open("./comparison.txt","r+")

result = re.findall(" \(.*\)",f.read())

f.close()

f = open("./comparison.txt","r+")
res = open("./requirements.txt","w")
cropped = list()
for item in result:
    cropped.append(item[2:-1])
#print(result, cropped)

i = 0
for riga in f:
    riga = riga.replace(result[i], "=="+cropped[i])
    res.write(riga)
    i += 1
    print(riga)

f.close()
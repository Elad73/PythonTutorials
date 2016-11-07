__author__ = 'eladron'

import os
import glob2
import datetime

def writer(celsiusTemps, mode) :
    with open("example.txt", mode) as file:
        for tempInC in celsiusTemps:
            if tempInC > -273.3:
                tempInF = tempInC*1.8+32
                file.write(str(tempInF) + '\n')


#writer([10,-20,-289,100], 'w')

filesUrl = './Sample-Files'
fileNames = glob2.glob("./Sample-Files/*.txt")
print(fileNames)
def filesMerger(url):
    content = ''
    for filename in os.listdir(url):
        fileToRead = url + '/' + filename
        #print(fileToRead)
        with open(fileToRead, 'r') as file:
            content += file.read() + '\n'


    #print(content)

    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f" + ".txt"), 'w') as file:
        file.write(content)

filesMerger(filesUrl)




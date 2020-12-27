import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

haldClutFolder = 'C:\\Users\\SUNNY\\Documents\\BOX\\doc\\HaldCLUT'
haldClutFileInclusion = '.png'
haldClutFileExclustion = '(Expired)'
convertTool = 'convert'
sampleImageFile = 'sample.jpg'
outputFolder = 'output'


# scan through
for subfolder, folders, files in os.walk(haldClutFolder):
    for f in files:
        haldClutFile = subfolder + os.sep + f
        haldClutName = f[:-4]

        if haldClutFileInclusion in haldClutFile and not haldClutFileExclustion in haldClutFile:
            outputFile = outputFolder + os.sep + haldClutName + '.jpg'
            print(haldClutFile)
            print(haldClutName)
            print(outputFile)

            process = subprocess.run(
                [convertTool, sampleImageFile, haldClutFile, '-hald-clut', outputFile], stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, shell=True)
            print(process)

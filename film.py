import os
import subprocess
import multiprocessing
from PIL import Image, ImageDraw, ImageFont

haldClutFolder = 'C:\\Users\\SUNNY\\Documents\\HaldCLUT'
haldClutFileInclusion = '.png'
haldClutFileExclustion = '(Expired)'
convertTool = 'convert'
sampleImageFile = 'sample.jpg'
outputFolder = 'output'


def convert(convertTool, sampleImageFile, haldClutFile, outputFile):
    print(haldClutFile)
    print(outputFile)

    process = subprocess.run(
        [convertTool, sampleImageFile, haldClutFile, '-hald-clut', outputFile], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
    print(process)
    return


# scan through
if __name__ == '__main__':
    pool = multiprocessing.Pool()

    for subfolder, folders, files in os.walk(haldClutFolder):
        for f in files:
            haldClutFile = subfolder + os.sep + f
            haldClutName = f[:-4]

            if haldClutFileInclusion in haldClutFile and not haldClutFileExclustion in haldClutFile:
                outputFile = outputFolder + os.sep + haldClutName + '.jpg'

                pool.apply_async(
                    convert, args=(convertTool, sampleImageFile, haldClutFile, outputFile, ))
    pool.close()
    pool.join()

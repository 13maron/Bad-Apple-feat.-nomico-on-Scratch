# encoding: utf-8 (maybe)
# フレームデータをテキストに変換!

frames = 6571
width, height = 80, 60
mag = 6

from PIL import Image
import os

def textize(baseDir="./"):
        os.makedirs("./text/", exist_ok=True)
        for i in range(frames):
                img = Image.open(baseDir + "images/BadApple" + str(i).zfill(4) + ".jpg")
                data = ""
                for j in range(height):
                        for k in range(width):
                                data += str(hex(img.getpixel((k*mag+int(mag/2), j*mag+int(mag/2)))[0]))[2:].zfill(2)
				
                        if j != height-1:
                                data += "\n"
                text = open(baseDir + "text/Data" + str(i).zfill(4) + ".txt", "w")
                text.write(data)
                text.close()

def join(baseDir="./"):
        joined = open(baseDir + "joined.txt", "w")
        for i in range(frames):
                with open(baseDir + "text/Data" + str(i).zfill(4) + ".txt", "r") as f:
                        for j in range(height):
                                joined.writelines(f.readlines())
                        if i != frames-1:
                                joined.write("\n")

        joined.close()

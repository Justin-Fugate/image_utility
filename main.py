from tkinter import *
from tkinter.filedialog import askdirectory
import os
from PIL import Image
import glob


root = Tk()
root.geometry("200x200")


def show():
    label.config(text=clicked.get())


ext = [
    "jpg"
    "png"
    ]

clicked = StringVar()

clicked.set("jpg")

source_ext = OptionMenu(root, clicked, *ext)
source_ext.pack()

target_ext = OptionMenu(root, clicked, *ext)
target_ext.pack()

button = Button(root, text="click me", command=show).pack()

label = Label(root, text="")
label.pack()

# start a basic dialog window
Tk().withdraw()

# open dialog asking for the source folder directory and store the path in a variable
source_folder = askdirectory()

# open dialog asking for the target folder directory and store the path in a variable
target_folder = askdirectory()

# find all jpegs in the source folder, and store them in a list
imList = glob.glob(source_folder + "/*.jpg", recursive=True)

# loop through all the jpegs found in the source folder
for img in imList:
    # for each jpeg, open it
    im = Image.open(img)

    # extract the filename and extension from the path
    fileNameFull= os.path.split(img)
    # print(f"fileNameFull is {fileNameFull}")
    fileName, ext = os.path.splitext(fileNameFull[1])
    # print(f"fileName is {fileName}")
    im.save(target_folder + "/" + fileName + ".png", "png")

root.mainloop()
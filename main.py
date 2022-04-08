from tkinter import Tk
import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
import os
import time

music_extensions = ["*.mp3","*.mp4","*.flac","*.wav"]
ftypes = [("sound files",music_extensions)]
output_extensions = ["mp3","mp4","flac","wav"]

window = Tk()
window.title("converter")

def detectExtension():
    global file_extension
    global tempName
    global outputName
    tempName, file_extension = os.path.splitext(inputPath)
    for i in output_extensions:
        if i in file_extension:
            return i

def input():
    successText.set("")
    global inputPath
    inputPath = askopenfilename(initialdir="/",filetypes=ftypes)
    fileBox.delete(1, tkinter.END)
    fileBox.insert(0,inputPath)
    extension = detectExtension()
    infoText.set((f"Detected {extension} extension."))

def startConversion():
    outputName = tempName + "." + selectionMenu.get()
    for i in output_extensions:
        if i in file_extension:
            song = AudioSegment.from_file(inputPath,format=i)
            song.export(outputName,format=selectionMenu.get())
            successText.set("SUCCESS")
    
window_width = 500
window_height = 230
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

#input
fileBox = tkinter.Entry(window,cursor="arrow")
fileBox.insert(0,"...")
fileBox.place(x=20,y=50,height=20,width=400)

fileLabel = tkinter.Label(window,text="Select file to convert:")
fileLabel.place(x=20,y=23)

fileButton = tkinter.Button(window,text="Browse", fg="blue",bd=0,command=input,cursor="hand2",activebackground="grey")
fileButton.place(x=430,y=50,height=20)

#selection
selectionLabel = tkinter.Label(window,text="Convert to: ")
selectionLabel.place(x=20,y=80)

selection = tkinter.StringVar(window)
selectionMenu = ttk.Combobox(window, width=30)
selectionMenu.place(x=100,y=80)
selectionMenu["values"] = ["mp3","mp4","flac","wav"]
selectionMenu["state"] = "readonly"
selectionMenu.current(3)

#info text
infoText = tkinter.StringVar()
infoLabel = tkinter.Label(window,textvariable=infoText)
infoLabel.place(x=330,y=80)

#convert
convertButton = tkinter.Button(window,text="Convert",cursor="hand2",bg="#dbdbdb",bd=0,command=startConversion)
convertButton.place(x=125,y=140,height=60,width=250)

#success
global successText
successText = tkinter.StringVar()
successLabel = tkinter.Label(window,textvariable=successText, font=20,fg="green")
successLabel.place(x=200,y=110)

window.mainloop()


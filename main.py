import urllib.request
from tkinter import *

#urllib.request.urlretrieve("https://alfacod.github.io/favicon.ico", "")


win = Tk("downloader")
win.geometry("400x200")
win.title("py downloader")
win.resizable(False,False)


lbl1 = Label(win,text="paste link here").pack(pady=2)
link = Entry(win,width=60)
link.pack(pady=2)





win.mainloop()
import urllib.request
from tkinter import *


def _dl():
    try:
        def _ok():
            w2.destroy()
        url = link.get()
        name = entre.get()
        urllib.request.urlretrieve(url,name)
        link.delete(0,END)
        entre.delete(0,END)
        w2 = Tk()
        w2.title("Alert!")
        w2.geometry("250x60")
        win.resizable(False,False)
        lbl = Label(w2,text="Download finished").pack(pady=2)
        btn = Button(w2,text="ok",command=_ok).pack(pady=1)
    except:
        def _oh():
            w3.destroy()
        w3 = Tk()
        w3.title("Alert!")
        w3.geometry("250x60")
        win.resizable(False,False)
        lbl = Label(w3,text="Anything Wrong!").pack(pady=2)
        btn = Button(w3,text="ok",command=_oh).pack(pady=1)




win = Tk("downloader")
win.geometry("400x150")
win.title("py downloader")
win.resizable(False,False)


lbl1 = Label(win,text="paste link here").pack(pady=2)

link = Entry(win,width=60)
link.pack(pady=2)

lbl2 = Label(win ,text="Path").pack(pady=2)

entre =Entry(win)
entre.pack(pady=2)

dl = Button(win,text="download",command=_dl).pack(pady=5)



win.mainloop()
from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title("Tunniplaan")
root.geometry("805x525")

#frameCnt = 48
#frames = [PhotoImage(file = "gif1.gif",format = "gif -index %i" %(i)) for i in range(frameCnt)]
#aken = Toplevel()
#def update(ind):
#    frame = frames[ind]
#    ind += 1
#    if ind == frameCnt:
#        ind = 0
#    label.configure(image = frame)
#    aken.after(0, update, ind)
#label = Label(aken)
#label.pack()
#aken.after(0, update, 0)
#aken.mainloop()

def failist_sõnastikusse():
    tund_kirjeldus = {}
    file = open("Tunnid.txt","r")
    for line in file:
        tund,kirjeldus = line.strip().split(":")
        tund_kirjeldus[tund.strip()] = kirjeldus.strip()
    file.close()
    return tund_kirjeldus

tund_kirjeldus = failist_sõnastikusse()

def kirjeldus_aknasse(t:str):
    if(askyesno("Küsimus","Kas tahad kirjeldust näha?")):
        alam_root = Toplevel()
        alam_root.title()
        lbl_kirjeldus = Label(alam_root, text = tund_kirjeldus[t]).pack()
        c = Canvas(alam_root,height = 1000, width = 1000)
        file = PhotoImage(file = "gif1.gif")
        c.create_image(10,10,image = file,anchor = NW)
        c.pack()
        alam_root.mainloop()
    else:
        showinfo("Vastus","Kui ei taha, siis ei taha!")

lbl = Label(root, text = "", borderwidth = 2, relief = "groove").grid(row = 0, column = 0, sticky = N+S+W+E)

p = ["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j = 0
for i in range(1,10,2):
    Days = Label(root, height = 5, width = 15, text = p[j], relief = "groove").grid(row = i, column = 0, rowspan = 2, sticky = N+S+W+E)
    j+=1

kell = ["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
    tunnid = Label(root, height = 4, width = 9, text = str(i)+"\n"+kell[i], relief = "groove").grid(row = 0, column = i+1, sticky = N+S+W+E)


b1 = Button(root, text = "Multimeedia", bg = "cornflowerblue", relief = "raised", command = lambda:kirjeldus_aknasse("Multimeedia"))
b1.grid(row = 1, column = 2, columnspan = 2, sticky = N+S+W+E)
b2 = Button(root, text = "Programmeerimise alused", bg = "skyblue", relief = "raised", command = lambda:kirjeldus_aknasse("Programmeerimise alused"))
b2.grid(row = 2, column = 2, columnspan = 3, sticky = N+S+W+E)
b3 = Button(root, text = "Programmeerimise alused", bg = "skyblue", relief = "raised", command = lambda:kirjeldus_aknasse("Programmeerimise alused"))
b3.grid(row = 1, column = 5, columnspan = 3, sticky = N+S+W+E)
b4 = Button(root, text = "Multimeedia", bg = "cornflowerblue", relief = "raised", command = lambda:kirjeldus_aknasse("Multimeedia"))
b4.grid(row = 2, column = 5, columnspan = 2, sticky = N+S+W+E)
b5 = Button(root, text = "Rühma \n juhataja \n tund", bg = "skyblue", relief = "raised", command = lambda:kirjeldus_aknasse("Rühma juhataja tund"))
b5.grid(row = 1, column = 8, rowspan = 2, sticky = N+S+W+E)
b6 = Button(root, text = "Inglise keel", bg = "oldlace", relief = "raised", command = lambda:kirjeldus_aknasse("Inglise keel1"))
b6.grid(row = 3, column = 2, columnspan = 2, sticky = N+S+W+E)
b7 = Button(root, text = "Inglise keel", bg = "plum", relief = "raised", command = lambda:kirjeldus_aknasse("Inglise keel2"))
b7.grid(row = 4, column = 2, columnspan = 2, sticky = N+S+W+E)
b8 = Button(root, text = "Operatsiooni \n süsteemide \n alused", bg = "mediumorchid", relief = "raised", command = lambda:kirjeldus_aknasse("Operatsiooni süsteemide alused"))
b8.grid(row = 3, column = 4, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b9 = Button(root, text = "Kehaline kasvatus", bg = "palevioletred", relief = "raised", command = lambda:kirjeldus_aknasse("Kehaline kasvatus"))
b9.grid(row = 3, column = 7, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b10 = Button(root, text = "Eesti keel", bg = "orchid", relief = "raised", command = lambda:kirjeldus_aknasse("Eesti keel1"))
b10.grid(row = 3, column = 9, sticky = N+S+W+E)
b11 = Button(root, text = "Eesti keel", bg = "thistle", relief = "raised", command = lambda:kirjeldus_aknasse("Eesti keel2"))
b11.grid(row = 4, column = 9, sticky = N+S+W+E)
b12 = Button(root, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "wheat", relief = "raised", command = lambda:kirjeldus_aknasse("Ajalugu, inimgeograafia ja inimeseõpetus eesti keeles"))
b12.grid(row = 3, column = 10, rowspan = 2, sticky = N+S+W+E)
b13 = Button(root, text = "Programmeerimise alused", bg = "skyblue", relief = "raised", command = lambda:kirjeldus_aknasse("Programmeerimise alused"))
b13.grid(row = 5, column = 2, columnspan = 3, sticky = N+S+W+E)
b14 = Button(root, text = "Multimeedia", bg = "cornflowerblue", relief = "raised", command = lambda:kirjeldus_aknasse("Multimeedia"))
b14.grid(row = 6, column = 2, columnspan = 3, sticky = N+S+W+E)
b15 = Button(root, text = "Multimeedia", bg = "cornflowerblue", relief = "raised", command = lambda:kirjeldus_aknasse("Multimeedia"))
b15.grid(row = 5, column = 6, columnspan = 3, sticky = N+S+W+E)
b16 = Button(root, text = "Programmeerimise alused", bg = "skyblue", relief = "raised", command = lambda:kirjeldus_aknasse("Programmeerimise alused"))
b16.grid(row = 6, column = 6, columnspan = 3, sticky = N+S+W+E)
b17 = Button(root, text = "Kunstiained", bg = "hotpink", relief = "raised", command = lambda:kirjeldus_aknasse("Kunstiained"))
b17.grid(row = 5, column = 9, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b18 = Button(root, text = "Andmebaasisüsteemide alused \n (eesti keeles)", bg = "lightcoral", relief = "raised", command = lambda:kirjeldus_aknasse("Andmebaasisüsteemide alused (eesti keeles)"))
b18.grid(row = 7, column = 2, columnspan = 5, rowspan = 2, sticky = N+S+W+E)
b19 = Button(root, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "wheat", relief = "raised", command = lambda:kirjeldus_aknasse("Ajalugu,\n inimgeograafia ja inimeseõpetus eesti keeles"))
b19.grid(row = 7, column = 7, rowspan = 2, sticky = N+S+W+E)
b20 = Button(root, text = "Eesti keel", bg = "orchid", relief = "raised", command = lambda:kirjeldus_aknasse("Eesti keel1"))
b20.grid(row = 7, column = 8, sticky = N+S+W+E)
b21 = Button(root, text = "Eesti keel", bg = "thistle", relief = "raised", command = lambda:kirjeldus_aknasse("Eesti keel2"))
b21.grid(row = 8, column = 8, sticky = N+S+W+E)
b22 = Button(root, text = "Keel ja kirjandus", bg = "greenyellow", relief = "raised", command = lambda:kirjeldus_aknasse("Keel ja kirjandus"))
b22.grid(row = 9, column = 3, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b23 = Button(root, text = "Matemaatika", bg = "pink", relief = "raised", command = lambda:kirjeldus_aknasse("Matemaatika"))
b23.grid(row = 9, column = 6, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b24 = Button(root, text = "Suhtlemine ja \n klienditeenindus", bg = "blueviolet", relief = "raised", command = lambda:kirjeldus_aknasse("Suhtlemine ja klienditeenindus"))
b24.grid(row = 9, column = 8, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b25 = Button(root, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "wheat", relief = "raised", command = lambda:kirjeldus_aknasse("Ajalugu, inimgeograafia ja inimeseõpetus eesti keeles"))
b25.grid(row = 9, column = 10, rowspan = 2, sticky = N+S+W+E)

root.mainloop()

import tkinter
import random
random.seed()

#def titel():
	 #titellist = [
	# "der Drecksack",
#	 "der dummschwätzer",
#	 "der feine",
	# "der Herr",
#	 "der trunkenbold"]
	(random.choice(titellist))

def ende():
	main.destroy()


def anzeigen():
	lb["text"] = " "
	for x in li.curselection():
         lb["text"] = lb["text"] + b2.get() + " der " +  li.get(x)+" "

	
main = tkinter.Tk()


b1 =tkinter.Label(main, text= "Es war einmal ein Held....")
b1 ["font"] = "courier 10 italic"
b1 ["height"] = 2
b1["width"] = 40
b1 ["borderwidth"] = 5
#b1 ["relief"] = 0
b1 ["bg"] = "#F0F8FF"
b1 ["fg"] = "#000000"
b1 ["anchor"] = "n"
b1.pack()

ba = tkinter.Label(main, text ="Name:")
ba.pack()


b2 =tkinter.Entry(main)
b2.pack()

yb=tkinter.Label(main, text ="deinTitel:")
yb.pack()


li = tkinter.Listbox(main, height=0)
li.insert("end", "Geile")
li.insert("end", "Drecksack ")
li.insert("end", "Kackstelze")
li.pack()

bshow = tkinter.Button(main,text ="Anzeigen", command = anzeigen)
bshow.pack()

tb=tkinter.Label(main, text="und jeder Mensch kannte ihn unter denn namen:")
tb.pack()

lb = tkinter.Label(main, text ="")
lb ["font"] = "courier 10 italic"
lb ["height"] = 2
lb ["width"] = 40
lb ["borderwidth"] = 5
lb ["relief"] = "groove"
lb ["bg"] = "#F0F8FF"
lb ["fg"] = "#000000"
lb["anchor"] = "w"
lb.pack()



b = tkinter.Button (main, text = "Ende", command = ende)
b.pack()


main.mainloop()
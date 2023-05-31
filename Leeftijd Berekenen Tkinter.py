from tkinter import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.title('Jelle"s  leeftijd berekenen')
root.geometry("250x250")


def leeftijd():
    while True:
        try:
            num = int(my_entry.get())
        except ValueError:
            print("Please enter a valid integer")
    	    #error wanneer geen getal word ingevoerd
            break

        if num >= 1500 and num <= 2023:
            #grenzen stellen
            huidigjaar = datetime.now().year
            age = huidigjaar - int(my_entry.get())
            messagebox.showinfo('Leeftijd', f'U bent of wordt: {age}')
            break
        # else:

        #    print('The integer must be in the range 1-10')


my_label = Label(root, text='voer uw geboorte jaar in')
my_label.pack(pady=20)
my_entry = Entry(root)
my_entry.pack(pady=20)
my_button = Button(text="bereken!", command=leeftijd)
my_button.pack(pady=20)


root.mainloop()

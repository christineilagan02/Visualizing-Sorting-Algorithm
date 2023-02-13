
# Final Project
# Sorting Algorithm Visualiser (title)

from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='#082A46')

def Generate():
    print('Selected Algorithm: ' )



selected_algorithm = StringVar()
# label, buttons, speed scale

mainlabel = Label(root, text = "Algorithm : ", font = ("new roman", 16, "italic bold"), bg = "#05897A", 
                  width = 10, fg = "black", relief = GROOVE, bd = 5)
mainlabel.place(x = 0, y = 0)

algo_menu = ttk.Combobox(root, width = 15, font = ("new roman", 19, "italic bold"), textvariable = selected_algorithm, 
                         values = ['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algo_menu.place(x = 145, y = 0)
algo_menu.current(0)      # by default bubble sort

random_generate = Button(root, text = "Generate", bg = '#2DAE9A', font = ("arial", 12, "italic bold"), 
                         relief = SUNKEN, activebackground = '#05945B', activeforeground = "white", bd = 5, 
                         width = 10, command = Generate)
random_generate.place(x = 750, y = 60)



root.mainloop()
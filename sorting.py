
# Final Project
# Sorting Algorithm Visualiser (title)

from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='lightblue')
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i / max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400        # we have multiplied 400 because we will normalised our values with one
                                                # one formula so that our data won't exceed our canvas
        x1 = (i+1) * x_width
        y1 = canvas_height
        
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]), font = ("new roman", 10, "italic bold"),
                           fill = "black")

    root.update_idletasks()
def StartAlgorithm():
    global data
    if not data:
        return
    
    if(algo_menu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedscale.get())
        
    elif algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, speedscale.get())
    
    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, drawData, speedscale.get())
    drawData(data, ['green' for x in range(len(data))])



def Generate():
    global data
    print('Selected Algorithm: ' + selected_algorithm.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())
    
    
    data = []
    for _ in range(sizeevalue):
        # we will add that speed scaled by appending it 
        data.append(random.randrange(minivalue, maxivalue+1))
    drawData(data, ['#A90042' for x in range(len(data))])



selected_algorithm = StringVar()
# label, buttons, speed scale

mainlabel = Label(root, text = "Algorithm : ", font = ("new roman", 16, "italic bold"), bg = "violet", 
                  width = 10, fg = "black", relief = GROOVE, bd = 5)
mainlabel.place(x = 20, y = 10)

algo_menu = ttk.Combobox(root, width = 15, font = ("new roman", 19, "italic bold"), textvariable = selected_algorithm, 
                         values = ['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algo_menu.place(x = 170, y = 10)
algo_menu.current(0)      # by default bubble sort

random_generate = Button(root, text = "Generate", bg = 'skyblue', font = ("arial", 12, "italic bold"), 
                         relief = SUNKEN, activebackground = 'blue', activeforeground = "white", bd = 5, 
                         width = 10, command = Generate)
random_generate.place(x = 750, y = 70)

sizevaluelabel = Label(root, text = "Size : ", font = ("new roman", 12, "italic bold"), bg = "pink", 
                  width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
sizevaluelabel.place(x = 20, y = 70)

sizevalue = Scale(root, from_ = 5, to = 30, resolution = 1, orient = HORIZONTAL, font = ("arial", 14, "italic bold"), 
                  relief = GROOVE, bd = 2, width = 10)
sizevalue.place(x = 140, y = 70)

minvaluelabel = Label(root, text = "Min Value : ", font = ("new roman", 12, "italic bold"), bg = "pink", 
                  width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
minvaluelabel.place(x = 260, y = 70)

minvalue = Scale(root, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, font = ("arial", 14, "italic bold"), 
                  relief = GROOVE, bd = 2, width = 10)
minvalue.place(x = 380, y = 70)


maxvaluelabel = Label(root, text = "Max Value : ", font = ("new roman", 12, "italic bold"), bg = "pink", 
                  width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
maxvaluelabel.place(x = 510, y = 70)

maxvalue = Scale(root, from_ = 5, to = 100, resolution = 1, orient = HORIZONTAL, font = ("arial", 14, "italic bold"), 
                  relief = GROOVE, bd = 2, width = 10)
maxvalue.place(x = 630, y = 70)

start = Button(root, text = "Start", bg = 'lightgreen', font = ("arial", 12, "italic bold"), 
        relief = SUNKEN, activebackground = 'green', activeforeground = "white", bd = 5, width = 10, command = StartAlgorithm)
start.place(x = 750, y = 10)

speedlabel = Label(root, text = "Speed : ", font = ("new roman", 12, "italic bold"), bg = "violet", 
                  width = 10, fg = "black", height = 2, relief = GROOVE, bd = 3)
speedlabel.place(x = 415, y = 10)

speedscale = Scale(root, from_ = 0.1, to = 5.0, resolution = 0.2, length = 200, digits = 2, orient = HORIZONTAL, font = ("arial", 14, "italic bold"), 
                  relief = GROOVE, bd = 1, width = 10)
speedscale.place(x = 535, y = 10)

canvas = Canvas(root, width = 870, height = 450, bg = "silver")
canvas.place(x = 10, y = 130)

root.mainloop()
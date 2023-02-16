
# Final Project
# original code: https://youtu.be/RD1JqhtNgvw
# Sorting Algorithm Visualiser (title)

from tkinter import *
from tkinter import ttk

import random
import pygame
from tkinter import messagebox

# algorithm file
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='lightblue')
data = []

# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
image = PhotoImage(file = 'image/sorted logo.png')
  
# Setting icon of master window
root.iconphoto(False, image)

# Creating a photoimage object to use image
photo = PhotoImage(file = 'image/mark.png')

# Resizing image to fit on button
photoimage = photo.subsample(6, 6)

def message():
    messagebox.showinfo("Information", 'Press ENTER to START, Press SHIFT+TAB to GENERATE and Press ESC to CLOSE WINDOW')

# here, image option is used to
# set image on button
mark = Button(root, image = photoimage, command = message)
mark.place(x = 425, y = 10)

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

    root.update()

pygame.mixer.init()
sound = pygame.mixer.Sound('audio/beat.mp3')
sound1 = pygame.mixer.Sound('audio/sorted.mp3')

def StartAlgorithm():
    global data
    timeTick = set_speed()
    if not data:
        return
    
    if(algo_menu.get() == 'Quick Sort'):
        sound.play()
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
        
    elif (algo_menu.get() == 'Merge Sort'):
        sound.play()
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    
    elif algo_menu.get() == "Bubble Sort":
        sound.play()
        bubble_sort(data, drawData, timeTick)
        
    elif algo_menu.get() == "Insertion Sort":
        sound.play()
        insertion_sort(data, drawData, timeTick)
        
    elif algo_menu.get() == "Selection Sort":
        sound.play()
        selection_sort(data, drawData, timeTick)
        
    drawData(data, ['green' for x in range(len(data))])
    sound1.play()
    sound.stop()
    
# Bind the Enter Key to the window
root.bind('<Return>', lambda event: StartAlgorithm())

# This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 1
    elif speed_menu.get() == 'Medium':
        return 0.5
    else:
        return 0.1
    

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
    
# Bind the Shift+Tab key with the event
root.bind('<Shift-Tab>', lambda event: Generate())

# Define an event to close the window
def close_win(e):
   root.destroy()
   
# Bind the ESC key with the callback function
root.bind('<Escape>', lambda e: close_win(e))


selected_algorithm = StringVar()
speed_name = StringVar()
# label, buttons, speed scale

mainlabel = Label(root, text = "Algorithm : ", font = ("new roman", 16, "italic bold"), bg = "violet", 
                  width = 10, fg = "black", relief = GROOVE, bd = 5)
mainlabel.place(x = 20, y = 10)

algo_menu = ttk.Combobox(root, width = 15, font = ("new roman", 19, "italic bold"), textvariable = selected_algorithm, 
                         values = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort'])
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
minvaluelabel.place(x = 265, y = 70)

minvalue = Scale(root, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, font = ("arial", 14, "italic bold"), 
                  relief = GROOVE, bd = 2, width = 10)
minvalue.place(x = 385, y = 70)


maxvaluelabel = Label(root, text = "Max Value : ", font = ("new roman", 12, "italic bold"), bg = "pink", 
                  width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
maxvaluelabel.place(x = 510, y = 70)

maxvalue = Scale(root, from_ = 5, to = 100, resolution = 1, orient = HORIZONTAL, font = ("arial", 14, "italic bold"), 
                  relief = GROOVE, bd = 2, width = 10)
maxvalue.place(x = 630, y = 70)

start = Button(root, text = "Start", bg = 'lightgreen', font = ("arial", 12, "italic bold"), 
        relief = SUNKEN, activebackground = 'green', activeforeground = "white", bd = 5, width = 10, command = StartAlgorithm)
start.place(x = 750, y = 10)

# dropdown to select sorting speed 
speedlabel = Label(root, text = "Speed: ", font = ("new roman", 16, "italic bold"), bg = "violet", 
                  width = 9, fg = "black", relief = GROOVE, bd = 5)
speedlabel.place(x = 490, y = 10)

speed_menu = ttk.Combobox(root, width = 7, font = ("new roman", 15, "italic bold"), textvariable = speed_name, 
                         values = ['Fast', 'Medium', 'Slow'])
speed_menu.place(x = 630, y = 10)
speed_menu.current(1)     # by default medium

canvas = Canvas(root, width = 870, height = 450, bg = "silver")
canvas.place(x = 10, y = 130)

root.mainloop()
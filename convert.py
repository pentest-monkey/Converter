#A simple GUI to convert miles to kilometers.
#original author: https://github.com/clear-code-projects


import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.609
    output_string.set(km_output)


#window
window = ttk.Window(themename='darkly')
window.title('Conversion')
window.geometry('300x200')

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'bold', padding='15' )
title_label.pack()

#entry label
entry_label = ttk.Label(master = window, text = 'Enter your miles:', font = 'Arial 10')
entry_label.pack()


# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = tk.LEFT, padx=5, pady=5)
button.pack(side = tk.RIGHT)
input_frame.pack()

#result label
result_label = ttk.Label(master = window, text = 'Kilometers: ', font = 'bold')
result_label.pack()

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
text = 'Kilometers: ', background = 'blue',
font = 'Arial 13 bold italic', 
textvariable = output_string)
output_label.pack()

#run
window.mainloop()
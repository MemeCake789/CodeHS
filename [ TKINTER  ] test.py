import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Draw a rectangle
rectangle = canvas.create_rectangle(50, 50, 200, 150, fill="red")

# Draw an oval
oval = canvas.create_oval(250, 50, 350, 150, fill="blue")

# Draw a line
line = canvas.create_line(50, 250, 350, 250)



window.mainloop()
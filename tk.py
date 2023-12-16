import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)

for i in range(8):
    canvas.create_line((75 * i, 0), (75 * i, 600))
for i in range(8):
    canvas.create_line((0, 75 * i), (600, 75 * i))

canvas.pack()
master.mainloop()
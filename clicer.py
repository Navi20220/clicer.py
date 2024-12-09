import tkinter as tk
import random


def move_cube():
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    canvas.coords(cube, x - 25, y - 25, x + 25, y + 25)


root = tk.Tk()
root.title("Кликер")
root.geometry("400x400")


canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()


cube = canvas.create_rectangle(175, 175, 225, 225, fill="blue")


canvas.tag_bind(cube, "<Button-1>", lambda event: move_cube())


root.mainloop()

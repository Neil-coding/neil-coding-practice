import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Neil's Mission Rocket")
root.geometry("1000x1000")

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Open and close image files properly
with Image.open("bg.jpeg") as img:
    background_image = ImageTk.PhotoImage(img)

canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Open and close image files properly
with Image.open("rocketnbg.png") as img:
    rocket_image = ImageTk.PhotoImage(img)

rocket = canvas.create_image(500, 500, anchor=tk.NW, image=rocket_image)

bullet_speed = 10

def move_right(event):
    canvas.move(rocket, 10, 0)

def move_left(event):
    canvas.move(rocket, -10, 0)

def move_up(event):
    canvas.move(rocket, 0, -10)

def move_down(event):
    canvas.move(rocket, 0, 10)

def fire(event):
    bullet = canvas.create_image(canvas.coords(rocket)[0] + 50, canvas.coords(rocket)[1], anchor=tk.NW, image=bullet_image)
    move_bullet(bullet)

def move_bullet(bullet):
    canvas.move(bullet, 0, -bullet_speed)
    if canvas.coords(bullet)[1] > 0:
        root.after(50, move_bullet, bullet)
    else:
        canvas.delete(bullet)

# Open and close image files properly
with Image.open("happy.png") as img:
    bullet_image = ImageTk.PhotoImage(img)

root.bind('<KeyPress-Right>', move_right)
root.bind('<KeyPress-Left>', move_left)
root.bind('<KeyPress-Up>', move_up)
root.bind('<KeyPress-Down>', move_down)
root.bind('<space>', fire)

tk.mainloop()

import turtle
from turtle import Screen, Turtle
import tkinter as tk
from PIL import ImageGrab
import tkinter.messagebox as tkMessageBox


WIDTH, HEIGHT = 300, 200
IMG_FILENAME = 'my_drawing.png'

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                    borderwidth=0, highlightthickness=0)
screen = turtle.TurtleScreen(canvas)

t = turtle.RawTurtle(screen.getcanvas())

def init_turtle():
    t.speed(-1)
    t.penup()
    t.goto(0,80)
    t.pendown()
    t.pensize(10)

def clear_board():
    t.reset()
    init_turtle()
    
def clear_click(event):
    clear_board()

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def getter(widget):
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    return ImageGrab.grab().crop((x, y, x1, y1))

def save_file(root, canvas, filename):
    """ Convert the Canvas widget into a bitmapped image. """
    # Get image of Canvas and convert it to bitmapped image.
    img = getter(canvas).convert('L').convert('1')
    img.save(IMG_FILENAME)

    tkMessageBox.showinfo("Info", "Image saved as %r" % filename, parent=root)

def main(): 
    init_turtle() 
    canvas.pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack()
    
    clear_button = tk.Button(btn_frame,text="Clear",bg="blue",fg="yellow")
    check_button = tk.Button(btn_frame,text="Check",bg="blue",fg="yellow",command=lambda: save_file(root, canvas, IMG_FILENAME))

    t.ondrag(dragging)  

    clear_button.bind("<Button-1>", clear_click)
    check_button.pack(side=tk.LEFT)
    clear_button.pack(side=tk.LEFT)
    root.mainloop()

main()
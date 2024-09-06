from tkinter import Tk, Canvas, Label
import math

root = Tk()

root.title("Hello World!")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate position x and y coordinates
x = (screen_width/2) - (1200/2)
y = (screen_height/2-50) - (700/2)
root.geometry('%dx%d+%d+%d' % (1200, 700, x, y))

w = Label(root, text="I'm so good", fg="blue")
w.pack()

C = Canvas(root, width=1200, height=screen_height)
C.pack()

dir = 1
def draw(m):
    global dir
    C.delete("all")
    loc = []
    loc2 = []
    x=0
    while x<24:
        for j in range(4):
            loc.append([])
            loc2.append([])
            loc[j].append([x, math.asin(math.sin(x)*math.sin(m))+160+(math.pi*j)])
            loc2[j].append([x, math.asin(math.sin((((2*j+1)*math.pi)/2)-x)*math.sin(((3*math.pi)/2)-m))+160+(math.pi/2)+(math.pi*(j-1))])
        x+=0.1
    for i in range(4):
        C.create_line(loc[i], fill='blue', smooth=True)
        C.create_line(loc2[i], fill='black', smooth=True)

    if m > 6.29 or m < 0.01: dir *= -1
    C.scale("all", 0, 160, 50, 40)
    root.after(2, draw, m+dir*0.01)

draw(0.01)
root.mainloop()
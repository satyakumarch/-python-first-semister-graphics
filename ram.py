from turtle import*
import colorsys
speed(99)
hideturtle()
pensize(4)
bgcolor('black')
hue = 0.0
for i in range(300):
    color = colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    hue+=0.005
    for j in range(2):
        fd(i)
        lt(30*2+1)
        rt(120)
    rt(60*2)
done()    
from tkinter import *
from tkinter import Canvas
import random
import time


root=Tk()
root.geometry("400x400")
root.title("Bubble sort visualiser")
our_canvas=Canvas(root,width=800,height=800,bg="white")
our_canvas.pack()
y0=50
yn=650
inc=10
n=(yn-y0)/10


arr=random.sample(range(y0,yn,inc),n)
for i in range(n-1): 
	for j in range(0, n-i-1):
		if arr[j] > arr[j+1]:
			temp=arr[j]
			arr[j]=arr[j+1]
			arr[j+1]=temp
			i=100
			root.update()
			our_canvas.delete("all")
			for y in arr:
				our_canvas.create_line(i,0,i,y,fill="black",width="0.1c")
				i=i+inc
			time.sleep(0.05)

root.mainloop()



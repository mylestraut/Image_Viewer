from tkinter import *
from PIL import ImageTk, Image
from LinkedList.LinkedList import LinkedList
from Photo.Photo import Photo
#from folder.file import Klasa

root = Tk()
root.title("Viewer V2")

img_1 = ImageTk.PhotoImage(Image.open("images/bali.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("images/bali_beach.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("images/bali_swing.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("images/arrival.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("images/Bali_forest.jpg"))


def forward(position):
	global label_1
	global button_forward
	global button_back

	label_1.grid_forget()

	label_1 = Label(root, image=image_list.get_position(position).value)
	label_1.grid(row=0, column=0, columnspan=3)

	button_forward = Button(root, text='>>', command=lambda: forward(position + 1))
	button_back = Button(root, text='<<', command=lambda: back(position - 1))

	if image_list.get_position(position).next == None:
		button_forward = Button(root, text='>>', state=DISABLED)

	button_forward.grid(row=1, column=2)
	button_back.grid(row=1, column=0)

	status = Label(root, text='Image ' + str(position) + ' of ' + str(image_list.len_link()), relief=SUNKEN)
	status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

def back(position):

	global label_1
	global button_forward
	global button_back

	label_1.grid_forget()

	label_1 = Label(root, image=image_list.get_position(position).value)
	label_1.grid(row=0, column=0, columnspan=3)

	button_forward = Button(root, text='>>', command=lambda: forward(position + 1))
	button_back = Button(root, text='<<', command=lambda: back(position - 1))

	if position == 1:
		button_back = Button(root, text='<<', state=DISABLED)

	button_forward.grid(row=1, column=2)
	button_back.grid(row=1, column=0)

	status = Label(root, text='Image ' + str(position) + ' of ' + str(image_list.len_link()), relief=SUNKEN)
	status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)


photo_1 = Photo(img_1, "Bali")
photo_2 = Photo(img_2, "Bali Beach")
photo_3 = Photo(img_3, "Bali Swing")
photo_4 = Photo(img_4, "Arrival")
photo_5 = Photo(img_5, "Bali Forest")

image_list = LinkedList(photo_1)
image_list.append(photo_2)
image_list.append(photo_3)
image_list.append(photo_4)
image_list.append(photo_5)

#print(image_list.len_link())

label_1 = Label(root, image=image_list.get_position(1).value)
label_1.grid(row=0, column=0, columnspan=3)

button_forward = Button(root, text='>>', command=lambda: forward(2))
button_back = Button(root, text='<<', command=lambda: back(2), state=DISABLED)
button_quit = Button(root, text='Quit', command=root.quit)

status = Label(root, text='Image 1 of ' + str(image_list.len_link()), relief=SUNKEN)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_quit.grid(row=1, column=1)

status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

root.mainloop()
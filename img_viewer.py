from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

img_1 = ImageTk.PhotoImage(Image.open("images/bali.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("images/Bali_forrest.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("images/bali_beach.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("images/bali_swing.jpg"))

img_list = [img_1, img_2, img_3, img_4]

my_label = Label(root, image=img_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_index):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()

	my_label = Label(root, image=img_list[image_index])
	my_label.grid(row=0, column=0, columnspan=3)

	button_forward = Button(root, text=">>", padx=30, pady=10, command=lambda: forward(image_index + 1))
	button_back = Button(root, text="<<", padx=30, pady=10, command=lambda: back(image_index - 1))
	
	if image_index == len(img_list)-1:
		button_forward = Button(root, text=">>", padx=30, pady=10, state=DISABLED)
		
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_index):
	global my_label
	global button_forward
	global button_back
	
	my_label.grid_forget()

	my_label = Label(root, image=img_list[image_index])
	my_label.grid(row=0, column=0, columnspan=3)

	button_back = Button(root, text="<<", padx=30, pady=10, command=lambda: back(image_index - 1))
	button_forward = Button(root, text=">>", padx=30, pady=10, command=lambda: forward(image_index + 1))

	if image_index == 0:
		button_back = Button(root, text="<<", padx=30, pady=10, state=DISABLED)

	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", padx=30, pady=10, command=back, state=DISABLED)
button_quit = Button(root, text="Quit", padx=30, pady=10, command=root.quit)
button_forward = Button(root, text=">>", padx=30, pady=10, command=lambda: forward(1))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()

















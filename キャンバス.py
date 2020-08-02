import tkinter
root=tkinter.Tk()
root.title("初めてのキャンバス")
root.geometry("800x800")
canvas=tkinter.Canvas(root,width=800,height=800,bg="skyblue")
canvas.pack()
gazou=tkinter.PhotoImage(file="お金.png")
canvas.create_image(400,400,image=gazou)
root.mainloop()
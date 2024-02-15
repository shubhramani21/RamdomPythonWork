import pyshorteners
import tkinter as tk
import webbrowser

# making the root
root=tk.Tk()


# creating canvas   
canvas=tk.Canvas(root, width=400, height=300)
def get_short_url():

    def open_link(event):
        webbrowser.open(short_url)
    
    s = pyshorteners.Shortener()
    
    
    input_url1=entry.get()
    short_url=s.tinyurl.short(input_url1)
    print(short_url)
    
    label = tk.Label(root, text=str(short_url), fg="blue", cursor="hand2")
    label.pack(pady=10)

    # Bind the label to the function that opens the link
    label.bind("<Button-1>", open_link)

    canvas.create_window(200,230,window=label)






entry=tk.Entry(root)
canvas.create_window(200, 140, window=entry)

button = tk.Button(text='Get Short URL', command=get_short_url)
canvas.create_window(200, 180, window=button)


canvas.pack()






s = pyshorteners.Shortener()

root.mainloop()
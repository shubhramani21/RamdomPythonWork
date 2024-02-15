import tkinter as tk
import webbrowser

def open_link(event):
    webbrowser.open("https://www.example.com")

root = tk.Tk()
root.title("Clickable Hyperlink Example")



label = tk.Label(root, text="Click here to visit example.com", fg="blue", cursor="hand2")
label.pack(pady=10)

# Bind the label to the function that opens the link
label.bind("<Button-1>", open_link)

root.mainloop()
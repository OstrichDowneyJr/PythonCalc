import customtkinter as ctk

# Setting appearance mode and default theme
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 

# Creating root window
root = ctk.CTk()
root.geometry("600x600")
root.title("Calculator")

entry = ctk.CTkEntry(root,width=300, font=("Arial",24))
entry.grid(row = 0, column =0,padx=20, pady=10 )

def button_click(value):
    current = entry.get()
    entry.delete(0, ctk.end)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, ctk.END)
    

root.mainloop()
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Flash n Bash")
root.geometry("400x300")

page2 = tk.Frame(root, bg="lightblue")

def show_page2():
    page1.pack_forget()
    page2.pack(fill="both", expand=True)

page1 = tk.Frame(root, bg="lightblue")
page1.pack(fill="both", expand=True)



# This is a label of my text that when i run the code it there will be widget pop up called Main menu
l_main_menu = tk.Label(page1, text="Main menu")
l_main_menu.grid(row=0, column=0, columnspan= 2)

# This is a button so when i run my code there will be a button called start and when i press on it there will be a function
btn_start = tk.Button(page1, text="Start", command=show_page2)
btn_start.grid(row=3, column=0, columnspan=2)

# This is a Label so when i run my code there will be a widget label called Name 
l_username = tk.Label(page1, text="Name:")
l_username.grid(row=1, column=0)

# This i
ent_name = tk.Entry(page1)
ent_name.grid(row=1, column=1, padx=1, pady=3, sticky="w")

create_flash_card = tk.Label(page2, text="Create your flash cards")
create_flash_card.grid(row=3, column=1, pady=25)

blank_box = tk.Entry(page2, width=30)
blank_box.grid(row=4, column=1, pady=15)
roblox = tk.Button(page2, text="Create & Save", width=15)
roblox.grid(row=5, column=2, pady=10)

root.mainloop()
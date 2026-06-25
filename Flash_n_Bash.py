import tkinter as tk

root = tk.Tk()
root.title("Flash n Bash")
root.geometry("400x300")

def page2():
    
    page1.pack_forget()

    page2.pack(fill="both", expand = True)

page1 = tk.Frame(root, bg="lightblue")
page1.pack(fill="both", expand = True)

#tk.Label(root, text="Well done")

#root.grid_columnconfigure(1, weight=1)


l_main_menu = tk.Label(page1, text="Main menu")
l_main_menu.grid(row=0, column=0, columnspan= 2)
btn_start = tk.Button(page1, text="Start", command=page2)
btn_start.grid(row=3, column=0, columnspan=2)
l_username = tk.Label(page1, text="Name:")
l_username.grid(row=1, column=0)

ent_name = tk.Entry(page1)
ent_name.grid(row=1, column=1, padx=1, pady=3, sticky="w")

page2 = tk.Frame (root, bg="lightblue")

create_flash_card = tk.Label(page2, text="Create your flash cards")
create_flash_card.grid(row = 3, column = 1, pady = 25)

root.mainloop()
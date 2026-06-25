import tkinter as tk

root = tk.Tk()
root.title("Flash n Bash")
root.geometry("400x300")

# 1. THE FIX: Rename the function so it doesn't clash with the frame variable
def switch_to_page2():
    page1.pack_forget()                   # Hide Frame 1
    page2.pack(fill="both", expand=True)  # Show Frame 2

# --- FRAME 1 SETUP ---
page1 = tk.Frame(root, bg="lightblue")
page1.pack(fill="both", expand=True)

l_main_menu = tk.Label(page1, text="Main menu", bg="lightblue")
l_main_menu.grid(row=0, column=0, columnspan=2)

l_username = tk.Label(page1, text="Name:", bg="lightblue")
l_username.grid(row=1, column=0)

ent_name = tk.Entry(page1)
ent_name.grid(row=1, column=1, padx=1, pady=3, sticky="w")

# The command now safely calls the renamed function
btn_start = tk.Button(page1, text="Start", command=switch_to_page2)
btn_start.grid(row=3, column=0, columnspan=2)


# --- FRAME 2 SETUP ---
# 2. THE FIX: Create the second frame, but DO NOT pack it yet. 
# It sits invisibly in memory until the button is pressed.
page2 = tk.Frame(root, bg="lightgreen")

# Any widget you want on screen 2 MUST be parented to page2
l_game_title = tk.Label(page2, text="Welcome to Screen 2!", bg="lightgreen", font=("Arial", 14))
l_game_title.pack(pady=20)

btn_back = tk.Button(page2, text="Back", command=lambda: [page2.pack_forget(), page1.pack(fill="both", expand=True)])
btn_back.pack()


root.mainloop()

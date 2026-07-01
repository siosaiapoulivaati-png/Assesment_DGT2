import tkinter as tk

# --- 1. CORE WINDOW CONFIGURATION ---
root = tk.Tk()
root.title("Flash n Bash")
root.geometry("400x300")
root.configure(bg="lightblue")

# Force columns and rows to expand evenly so layout handles resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


# --- 2. THE PERMANENT CORNER CONTAINER ---
# Stays at the top of the root window, visible at all times
top_bar = tk.Frame(root, bg="lightblue")
top_bar.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

l_username = tk.Label(top_bar, text="Name:", bg="lightblue")
l_username.grid(row=0, column=0, padx=2)

ent_name = tk.Entry(top_bar, width=15)
ent_name.grid(row=0, column=1, padx=5)


# --- 3. PAGE SHIFT LOGIC ---
def show_page2():
    page1.grid_remove()  # Safely hides page 1
    page2.grid(row=1, column=0, sticky="nsew")  # Displays page 2

# --- 4. PAGE 1 LAYOUT (MAIN MENU) ---
page1 = tk.Frame(root, bg="lightblue")
page1.grid(row=1, column=0, sticky="nsew")
page1.columnconfigure(0, weight=1)

l_main_menu = tk.Label(page1, text="Main menu", bg="lightblue", font=("Arial", 16, "bold"))
l_main_menu.grid(row=0, column=0, pady=20)

btn_start = tk.Button(page1, text="Start", command=show_page2, width=12)
btn_start.grid(row=1, column=0, pady=10)


# --- 5. PAGE 2 LAYOUT (FLASH CARDS) ---
page2 = tk.Frame(root, bg="lightblue")
page2.columnconfigure(0, weight=1)

create_flash_card = tk.Label(page2, text="Create your flash cards", bg="lightblue", font=("Arial", 12))
create_flash_card.grid(row=0, column=0, pady=15)

blank_box = tk.Entry(page2, width=30)
blank_box.grid(row=1, column=0, pady=10)

roblox = tk.Button(page2, text="Create & Save", width=15)
roblox.grid(row=2, column=0, pady=10)


# --- 6. START THE WINDOW ---
root.mainloop()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Flash n Bash")
root.geometry("400x300")

# --- NEW: This is the list where your cards will be appended ---
flashcards_list = []

# --- NEW: The function that handles the append logic ---
def save_flashcard():
    card_text = blank_box.get()  # 1. Get the text from the entry box
    
    if card_text.strip() == "":  # 2. Check if the user typed nothing or just spaces
        messagebox.showwarning("Empty Box", "Please type something before saving!")
    else:
        flashcards_list.append(card_text)  # 3. APPEND the text to our list
        blank_box.delete(0, tk.END)        # 4. Clear the box so it's ready for the next card
        
        # 5. Show a success popup (optional, but helpful!)
        messagebox.showinfo("Saved!", f"'{card_text}' added to your flashcards!\nTotal cards: {len(flashcards_list)}")
        print("Current list of cards:", flashcards_list)  # Prints in your terminal to track it


page2 = tk.Frame(root, bg="lightblue")

def show_page2():
    page1.pack_forget()
    page2.pack(fill="both", expand=True)

page1 = tk.Frame(root, bg="lightblue")
page1.pack(fill="both", expand=True)

# Centering logic for Page 1
page1.columnconfigure(0, weight=1)
page1.columnconfigure(1, weight=1)
page1.rowconfigure(0, weight=1)
page1.rowconfigure(1, weight=1)
page1.rowconfigure(2, weight=1)
page1.rowconfigure(3, weight=1)

l_main_menu = tk.Label(page1, text="Main menu", bg="lightblue", font=("Arial", 16, "bold"))
l_main_menu.grid(row=0, column=0, columnspan=2, pady=10)

l_username = tk.Label(page1, text="Name:", bg="lightblue")
l_username.grid(row=1, column=0, sticky="e", padx=5)

ent_name = tk.Entry(page1)
ent_name.grid(row=1, column=1, padx=5, pady=3, sticky="w")

btn_start = tk.Button(page1, text="Start", command=show_page2, width=10)
btn_start.grid(row=3, column=0, columnspan=2, pady=15)


# Centering logic for Page 2
page2.columnconfigure((0, 1, 2), weight=1)
page2.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

create_flash_card = tk.Label(page2, text="Create your flash cards", bg="lightblue")
create_flash_card.grid(row=3, column=1, pady=10)

blank_box = tk.Entry(page2, width=30)
blank_box.grid(row=4, column=1, pady=10)

# --- CHANGED: Added command=save_flashcard to link the button to our function ---
roblox = tk.Button(page2, text="Create & Save", width=15, command=save_flashcard)
roblox.grid(row=5, column=1, pady=10)

root.mainloop()

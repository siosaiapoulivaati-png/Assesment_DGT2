import tkinter as tk
from tkinter import messagebox

# 1. INITIALIZE DATA STORAGE
# This list will store all the flashcards you create as dictionaries
flashcards_database = []
current_card_index = 0

root = tk.Tk()
root.title("Flash n Bash - Quizlet Clone")
root.geometry("450x450")
root.configure(bg="#FFEED4")

# ==========================================
# PAGE 1: CREATION PAGE
# ==========================================
create_page = tk.Frame(root, bg="#FFEED4")
create_page.pack(fill="both", expand=True, padx=20, pady=20)

# Title Label for the creator screen
instruction_label = tk.Label(create_page, text="Create a Flashcard", font=("Arial", 16, "bold"), bg="#FFEED4", fg="#D4A357")
instruction_label.pack(pady=10)

# The Small Box Container (Styled to look like your image)
card_box = tk.Frame(create_page, width=250, height=180, bg="#FFF1DA", bd=2, relief="solid", highlightbackground="#D4A357", highlightthickness=1)
card_box.pack_propagate(False) # Stop box from collapsing
card_box.pack(pady=15)

# Editable Title Input Inside the Box
title_label = tk.Label(card_box, text="Title:", font=("Arial", 10, "bold"), bg="#FFF1DA")
title_label.pack(pady=(10,0))
title_entry = tk.Entry(card_box, font=("Arial", 12), justify="center", bd=1)
title_entry.pack(pady=5, padx=20, fill="x")

# Editable Text Input Inside the Box
text_label = tk.Label(card_box, text="Description/Text:", font=("Arial", 10, "bold"), bg="#FFF1DA")
text_label.pack(pady=(5,0))
text_entry = tk.Text(card_box, font=("Arial", 11), height=4, bd=1, wrap="word")
text_entry.pack(pady=5, padx=20, fill="both", expand=True)

# Function to Save Data
def save_flashcard():
    title = title_entry.get().strip()
    # Get all text from the Text widget
    text = text_entry.get("1.0", "end-1c").strip()
    
    if not title or not text:
        messagebox.showwarning("Missing Info", "Please fill out both Title and Text fields!")
        return
        
    # Save to our temporary database
    flashcards_database.append({"title": title, "text": text})
    
    # Clear fields for the next card
    title_entry.delete(0, tk.END)
    text_entry.delete("1.0", tk.END)
    
    messagebox.showinfo("Success", f"Flashcard '{title}' saved successfully!")

# Action Buttons for Page 1
btn_frame = tk.Frame(create_page, bg="#FFEED4")
btn_frame.pack(pady=10)

save_btn = tk.Button(btn_frame, text="Create & Save", font=("Arial", 11, "bold"), bg="#D4A357", fg="white", command=save_flashcard)
save_btn.pack(side="left", padx=10)

# Function to transition pages
def go_to_quiz_page():
    if not flashcards_database:
        messagebox.showwarning("Empty", "Create at least one flashcard before studying!")
        return
    create_page.pack_forget() # Hide page 1
    show_card()               # Load first card data
    quiz_page.pack(fill="both", expand=True, padx=20, pady=20) # Show page 2

done_btn = tk.Button(btn_frame, text="Done (Go to Study)", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=go_to_quiz_page)
done_btn.pack(side="left", padx=10)


# ==========================================
# PAGE 2: STUDY / QUIZ PAGE
# ==========================================
quiz_page = tk.Frame(root, bg="#FFEED4")

quiz_title = tk.Label(quiz_page, text="Study Mode", font=("Arial", 16, "bold"), bg="#FFEED4", fg="#333")
quiz_title.pack(pady=10)

# Display Box for reviewing cards
display_box = tk.Frame(quiz_page, width=250, height=180, bg="#FFFBF5", bd=2, relief="solid")
display_box.pack_propagate(False)
display_box.pack(pady=15)

display_title = tk.Label(display_box, text="", font=("Arial", 14, "bold"), bg="#FFFBF5")
display_title.pack(pady=20)

display_text = tk.Label(display_box, text="", font=("Arial", 11), bg="#FFFBF5", wraplength=200)
display_text.pack(pady=10)

def show_card():
    global current_card_index
    card = flashcards_database[current_card_index]
    display_title.config(text=card["title"])
    display_text.config(text=card["text"])

def next_card():
    global current_card_index
    if current_card_index < len(flashcards_database) - 1:
        current_card_index += 1
        show_card()
    else:
        messagebox.showinfo("End", "You finished reviewing all your cards!")

def go_back_to_creator():
    quiz_page.pack_forget()
    create_page.pack(fill="both", expand=True, padx=20, pady=20)

# Navigation Buttons for Studying
quiz_btn_frame = tk.Frame(quiz_page, bg="#FFEED4")
quiz_btn_frame.pack(pady=10)

next_btn = tk.Button(quiz_btn_frame, text="Next Card →", font=("Arial", 11), command=next_card)
next_btn.pack(side="right", padx=10)

back_btn = tk.Button(quiz_btn_frame, text="← Create More", font=("Arial", 11), command=go_back_to_creator)
back_btn.pack(side="left", padx=10)

root.mainloop()


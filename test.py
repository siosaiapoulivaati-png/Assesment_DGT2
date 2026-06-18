import tkinter as tk

def go_to_page_2():
    # Hide the first page
    page1.pack_forget()
    # Show the second page
    page2.pack(fill="both", expand=True)

def go_to_page_1():
    # Hide the second page
    page2.pack_forget()
    # Show the first page
    page1.pack(fill="both", expand=True)

# 1. Setup Main Window
root = tk.Tk()
root.title("Multi-Page App")
root.geometry("400x300")

# 2. Setup Page 1
page1 = tk.Frame(root, bg="lightblue")
page1.pack(fill="both", expand=True)

label1 = tk.Label(page1, text="Welcome to Page 1", font=("Arial", 16), bg="lightblue")
label1.pack(pady=20)

# Pass the function name directly to 'command' (do NOT use parentheses like go_to_page_2())
btn1 = tk.Button(page1, text="Go to Page 2", command=go_to_page_2)
btn1.pack(pady=10)

# 3. Setup Page 2 (Initially hidden)
page2 = tk.Frame(root, bg="lightgreen")

label2 = tk.Label(page2, text="Welcome to Page 2", font=("Arial", 16), bg="lightgreen")
label2.pack(pady=20)

btn2 = tk.Button(page2, text="Go Back to Page 1", command=go_to_page_1)
btn2.pack(pady=10)

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Input Window")
root.geometry("300x100")

# Add the input text box
text_box = tk.Entry(root, width=30)
text_box.pack(pady=10)

root.mainloop()


root.mainloop()

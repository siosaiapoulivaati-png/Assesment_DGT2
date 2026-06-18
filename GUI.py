import tkinter as tk

root = tk.Tk()
root.title("Flash n Bash")
root.geometry("400x300")

# Configure columns so they look neat
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Main title at the top
tk.Label(root, text="Main menu").grid(row=0, column=1, pady=10)

# Username label and entry box on the SAME row (row 1)
tk.Label(root, text="Username:").grid(row=1, column=1, sticky="e")
ent_name = tk.Entry(root)
ent_name.grid(row=1, column=2, padx=5, pady=3, sticky="w")

# Start button at the bottom
tk.Button(root, text="Start").grid(row=2, column=1, pady=10)
D
root.mainloop()

import tkinter as tk
import subprocess

# Function to run script1
def run_script1():
    subprocess.run(["python", "main.py"])

# Function to run script2
def run_script2():
    subprocess.run(["python", "ponggame.py"])

# Create the main window
root = tk.Tk()
root.title("Script Runner")

# Create and place the buttons
button1 = tk.Button(root, text="Run App 1", command=run_script1)
button1.pack(pady=10)

button2 = tk.Button(root, text="Run App 2", command=run_script2)
button2.pack(pady=10)

# Start the main loop
root.mainloop()

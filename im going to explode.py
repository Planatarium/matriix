import tkinter as tk
from tkinter import messagebox

# global variables to store the entry widgets and the matrix size
entries_A = []
entries_B = []
size = 0

def generate_matrices():
    """create the grid of entry boxes for matrix a and matrix b based on thr size given above"""
    global entries_A, entries_B, size

    try:
        size = int(size_entry.get())
        if size <= 0:
            messagebox.showerror("Error size must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error, enter a valid number")
        return

    entries_A = []
    entries_B = []

    # Basic labels for the grids
    tk.Label(matrix_frame, text="Matrix A").grid(row=0, column=0, columnspan=size)
    tk.Label(matrix_frame, text="Matrix B").grid(row=0, column=size+1, columnspan=size)

    for i in range(size):
        row_A = []
        row_B = []

        for j in range(size):
            # Generate boxes for Matrix A
            eA = tk.Entry(matrix_frame, width=5)
            eA.grid(row=i+1, column=j)
            row_A.append(eA)

            # Generate boxes for Matrix B
            eB = tk.Entry(matrix_frame, width=5)
            eB.grid(row=i+1, column=j+size+1)
            row_B.append(eB)

        entries_A.append(row_A)
        entries_B.append(row_B)


def get_matrix(entries):
    """read the numbers from the entry boxes and converts them into a list of floats"""
    # Temporary placeholder
    print("matrix data read")
    return []


def display_result(matrix):
    """Formats the list result and updates the UI label to show it"""
    # Temporary placeholder
    result_label.config(text="todo brb")

def add():
    """Addition what do yotu think this isa brwajw abfajjw """

    pass

def subtract():
    """Subtracts no shit"""

    pass

def multiply():
    """mulitply a and b awdfaqwerq """

    pass

# --- GUI SETUP ---
root = tk.Tk()
root.title("Matrix Calculator")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Matrix Size (N):").pack(side="left")
size_entry = tk.Entry(top_frame, width=5)
size_entry.pack(side="left")
tk.Button(top_frame, text="Generate", command=generate_matrices).pack(side="left")

matrix_frame = tk.Frame(root)
matrix_frame.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="A + B", command=add).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="A - B", command=subtract).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="A × B", command=multiply).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=10)

# start the application 
root.mainloop()

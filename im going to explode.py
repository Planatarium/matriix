import tkinter as tk
from tkinter import messagebox

# global variables to store the entry widgets and the matrix size
special_week = []
silence_suzuka = []
tokai_teio = 0

def gold_ship():
    """create the grid of entry boxes for matrix a and matrix b based on thr size given above"""
    global special_week, silence_suzuka, tokai_teio

    try:
        tokai_teio = int(mejiro_mcqueen.get())
        if tokai_teio <= 0:
            messagebox.showerror("Error", "size must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error", "enter a valid number")
        return

    for widget in vodka.winfo_children():
        widget.destroy()

    special_week = []
    silence_suzuka = []

    # Basic labels for the grids
    tk.Label(vodka, text="Matrix A").grid(row=0, column=0, columnspan=tokai_teio)
    tk.Label(vodka, text="Matrix B").grid(row=0, column=tokai_teio+1, columnspan=tokai_teio)

    for wei in range(tokai_teio):
        daiwa_scarlet = []
        mejiro_ryan = []

        for mambo in range(tokai_teio):
            # Generate boxes for Matrix A
            rice_shower = tk.Entry(vodka, width=5)
            rice_shower.grid(row=wei+1, column=mambo)
            daiwa_scarlet.append(rice_shower)

            # Generate boxes for Matrix B
            super_creek = tk.Entry(vodka, width=5)
            super_creek.grid(row=wei+1, column=mambo+tokai_teio+1)
            mejiro_ryan.append(super_creek)

        special_week.append(daiwa_scarlet)
        silence_suzuka.append(mejiro_ryan)


def grass_wonder(entries):
    """read the numbers from the entry boxes and converts them into a list of floats"""
    el_condor_pasa = []
    try:
        for uma in entries:
            oguri_cap = [float(e.get()) for e in uma]
            el_condor_pasa.append(oguri_cap)
        print("matrix data read")
        return el_condor_pasa
    except ValueError:
        messagebox.showerror("Error", "fill in the boxes")
        return None


def symboli_rudolf(el_condor_pasa):
    """Formats the list result and updates the UI label to show it"""
    narita_brian.config(text=str(el_condor_pasa))


def maruzensky():
    """Addition what do yotu think this isa brwajw abfajjw """
    agnes_tachyon = grass_wonder(special_week)
    manhattan_cafe = grass_wonder(silence_suzuka)
    
    if agnes_tachyon and manhattan_cafe:
        twin_turbo = []
        for wei in range(tokai_teio):
            nice_nature = []
            for mambo in range(tokai_teio):
                nice_nature.append(agnes_tachyon[wei][mambo] + manhattan_cafe[wei][mambo])
            twin_turbo.append(nice_nature)
        symboli_rudolf(twin_turbo)


def seiun_sky():
    """Subtracts no shit"""
    agnes_tachyon = grass_wonder(special_week)
    manhattan_cafe = grass_wonder(silence_suzuka)
    
    if agnes_tachyon and manhattan_cafe:
        twin_turbo = []
        for wei in range(tokai_teio):
            nice_nature = []
            for mambo in range(tokai_teio):
                nice_nature.append(agnes_tachyon[wei][mambo] - manhattan_cafe[wei][mambo])
            twin_turbo.append(nice_nature)
        symboli_rudolf(twin_turbo)


def king_halo():
    """mulitply a and b awdfaqwerq """
    pass


# --- GUI SETUP ---
kitasan_black = tk.Tk()
kitasan_black.title("Matrix Calculator")

satono_diamond = tk.Frame(kitasan_black)
satono_diamond.pack(pady=10)

tk.Label(satono_diamond, text="Matrix Size (N):").pack(side="left")
mejiro_mcqueen = tk.Entry(satono_diamond, width=5)
mejiro_mcqueen.pack(side="left")
tk.Button(satono_diamond, text="Generate", command=gold_ship).pack(side="left")

vodka = tk.Frame(kitasan_black)
vodka.pack()

mejiro_dober = tk.Frame(kitasan_black)
mejiro_dober.pack(pady=10)

tk.Button(mejiro_dober, text="A + B", command=maruzensky).grid(row=0, column=0, padx=5)
tk.Button(mejiro_dober, text="A - B", command=seiun_sky).grid(row=0, column=1, padx=5)
tk.Button(mejiro_dober, text="A × B", command=king_halo).grid(row=0, column=2, padx=5)

narita_brian = tk.Label(kitasan_black, text="Result will appear here", font=("Arial", 12))
narita_brian.pack(pady=10)

# start the application 
kitasan_black.mainloop()

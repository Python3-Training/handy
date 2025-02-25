#!/usr/bin/env python3
# Mission: Create, share, and enjoy a resistance divider / calculator.
# Will use tkinter if possible, else the console.

def gui():
    import tkinter as tk
    from tkinter import messagebox

    def calculate_resistors():
        try:
            v_in = float(entry_v_in.get())
            v_out = float(entry_v_out.get())
            r1 = float(entry_r1.get())
            
            if v_in <= v_out:
                messagebox.showerror("Input Error", "Input voltage must be greater than output voltage.")
                return

            r2 = (v_out * r1) / (v_in - v_out)
            label_result.config(text=f"R2: {r2:.2f} Ω")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

    # Create the main window
    root = tk.Tk()
    root.title("VΩV")

    # Create and place the input fields and labels
    tk.Label(root, text="Input Voltage (v_in):").grid(row=0, column=0, padx=10, pady=10)
    entry_v_in = tk.Entry(root)
    entry_v_in.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Output Voltage (v_out):").grid(row=1, column=0, padx=10, pady=10)
    entry_v_out = tk.Entry(root)
    entry_v_out.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Resistor R1 (Ω):").grid(row=2, column=0, padx=10, pady=10)
    entry_r1 = tk.Entry(root)
    entry_r1.grid(row=2, column=1, padx=10, pady=10)

    # Create and place the calculate button
    calculate_button = tk.Button(root, text="Calculate R2", command=calculate_resistors)
    calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Create and place the result label
    label_result = tk.Label(root, text="R2: -- Ω")
    label_result.grid(row=4, column=0, columnspan=2, pady=10)

    # Run the application
    root.mainloop()
try:
    import tkinter
    gui()
except:
    v_in = float(input("Voltage In: "))
    v_out = float(input("Voltage Out: "))
    r1 = float(input("Resistor #1: "))

    if v_in <= v_out:
        print("Input voltage must be greater than output voltage.")
        exit()

    r2 = (v_out * r1) / (v_in - v_out)
    print(f"Resistor #2: {r2:.2f} Ω")

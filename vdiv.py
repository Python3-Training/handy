#! /usr/bin/env
# Mission: Create, share, and enjoy a voltage divider / calculator.
# Will use tkinter if possible, else the console.

def gui():
    import tkinter as tk

    def calculate_vout():
        try:
            v_in = float(entry_vin.get())
            r1 = float(entry_r1.get())
            r2 = float(entry_r2.get())

            if r1 <= 0 or r2 <= 0:
                label_vout.config(text="Resistors must be positive values.")
                return

            v_out = v_in * (r2 / (r1 + r2))
            label_vout.config(text=f"Vout: {v_out:.2f} V")
        except ValueError:
            label_vout.config(text="Invalid input. Please enter numbers.")

    window = tk.Tk()
    window.title("ΩVΩ")
    window.geometry("200x160")

    # Labels and entry widgets
    label_vin = tk.Label(window, text="Vin (V):")
    label_vin.grid(row=0, column=0, padx=5, pady=5)
    entry_vin = tk.Entry(window)
    entry_vin.grid(row=0, column=1, padx=5, pady=5)

    label_r1 = tk.Label(window, text="R1 (Ω):")
    label_r1.grid(row=1, column=0, padx=5, pady=5)
    entry_r1 = tk.Entry(window)
    entry_r1.grid(row=1, column=1, padx=5, pady=5)

    label_r2 = tk.Label(window, text="R2 (Ω):")
    label_r2.grid(row=2, column=0, padx=5, pady=5)
    entry_r2 = tk.Entry(window)
    entry_r2.grid(row=2, column=1, padx=5, pady=5)

    # Calculate button
    button_calculate = tk.Button(window, text="Calculate Vout", command=calculate_vout)
    button_calculate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Output label
    label_vout = tk.Label(window, text="Vout: ")
    label_vout.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    window.mainloop()

try:
    import tkinter
    gui()
except:
    v_in = float(input("Voltage In: "))
    r1 = float(input("Resistor #1: "))
    r2 = float(input("Resistor #2: "))

    if r1 <= 0 or r2 <= 0:
        print("Resistors must be positive values.")
        exit()

    v_out = v_in * (r2 / (r1 + r2))
    print(f"Voltage Out: {v_out:.2f} V")

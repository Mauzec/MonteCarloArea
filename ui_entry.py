import random
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def calculate_integral(N):
    if N == '#':
        N_values = [10, 100, 1000, 10000, 100000, 1000000]
    else:
        N_values = [N]
    
    relative_errors = []
    analytical_value = 8.0 / 3.0
    
    xs = []; ys = []
    for N in N_values:
        k = 0
        for i in range(N):
            x = random.uniform(0.0, 4.0)
            y = random.uniform(0.0, 4.0)
            
            if x < 2 and x * x > y:
                k += 1
            
                if len(N_values) == 1:
                    xs.append(x)
                    ys.append(y)
            
        I = 16.0 * k / N
        relative_error = abs(I - analytical_value) / analytical_value
        relative_errors.append(relative_error)
        print(f"{k}, N = {N}, Integral = {I}, Relative error = {relative_error}")
    for i in range(len(N_values)):
        print(f"{k}, N = {N_values[i]}, Integral = {I}, Relative error = {relative_errors[i]}")
        # messagebox.showinfo("Integral", f"N = {N_values[i]}, Integral = {I}, Relative error = {relative_errors[i]}")
    message = '\n'.join([f"N = {N_values[i]}, Integral = {I}, Relative error = {relative_errors[i]}" for i in range(len(N_values))])
    messagebox.showinfo("Integral", message)
    
    x = np.linspace(0, 2, 100)
    y = np.linspace(0, 4, 100)
    X, Y = np.meshgrid(x, y)
    Z1 = X**2
    Z2 = Y

    if N == '#':
        return
    
    plt.figure()
    plt.contourf(X, Y, (Z1 > Z2), cmap='gray')
    plt.contour(X, Y, (Z1 > Z2), colors='black', linewidths=2)
    plt.scatter(xs, ys, color='red', marker='.')
    plt.xlim(0, 2)
    plt.ylim(0, 4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Figure')
    plt.grid(True)
    plt.show()

def calculate_area(N):
    k = 0
    S0 = 16.0  # Area of the square
    St = 6.37517 # True area
    xs = []; ys = []
    for i in range(N):
        x = random.uniform(-2.0, 2.0)
        y = random.uniform(-2.0, 2.0)

        if x * x - y * y * y < 2 and x + y < 1:
            k += 1
            xs.append(x)
            ys.append(y)

    S = S0 * k / N
    sigma = abs(S - St) / St

    print("Area:", S)
    print("Relative error:", sigma)
    
    messagebox.showinfo("Area", f"Area: {S}\nRelative error: {sigma}", icon="error" if sigma > 0.1 else "info")
    
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z1 = X**2 - Y**3
    Z2 = X + Y

    plt.figure()
    plt.contourf(X, Y, (Z1 < 2) & (Z2 < 1), cmap='gray')
    plt.contour(X, Y, (Z1 < 2) & (Z2 < 1), colors='black', linewidths=2)
    plt.scatter(xs, ys, color='red', marker='.')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Figure')
    plt.grid(True)
    plt.show()

def calculate_figure():
    figure = None
    try:
        calculate_area(int(iterations_entry.get()))
    except Exception as e:
        calculate_area(10)
    

def calculate_integral_monte_carlo():
    n = None
    try:
        calculate_integral(int(iterations_entry.get()))
    except Exception as e:
        if iterations_entry.get() == '#':
            calculate_integral('#')
        else:
            calculate_integral(10)


# Create the main window
window = tk.Tk()
window.title("Monte Carlo Area Calculator")

# Create labels and entry fields for user input
iterations_label = tk.Label(window, text="Number of Iterations (N):")
iterations_label.pack()
iterations_entry = tk.Entry(window)
default_text = "entry # to check all possible N"
iterations_entry.insert(0, default_text)
iterations_entry.config(fg="gray")
iterations_entry.bind("<FocusIn>", lambda event: iterations_entry.delete(0, "end"))
iterations_entry.bind("<FocusOut>", lambda event: iterations_entry.insert(0, default_text) if iterations_entry.get() == "" else None)
iterations_entry.pack()



# Create buttons for calculating figure and integral
figure_button = tk.Button(window, text="Calculate Area", command=calculate_figure)
figure_button.pack()

integral_button = tk.Button(window, text="Calculate Integral", command=calculate_integral_monte_carlo)
integral_button.pack()



def plot_figure():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z1 = X**2 - Y**3
    Z2 = X + Y

    plt.figure()
    plt.contourf(X, Y, (Z1 < 2) & (Z2 < 1), cmap='gray')
    plt.contour(X, Y, (Z1 < 2) & (Z2 < 1), colors='black', linewidths=2)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Figure')
    plt.grid(True)
    plt.show()


# Create buttons for calculating figure and integral
figure_button = tk.Button(window, text="Check Figure", command=plot_figure)
figure_button.pack()
window.mainloop()
import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
    except:
        result_label.config(text="Invalid input")

window = tk.Tk()
window.title("Calculator")

entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Add", command=calculate)
button.pack()

result_label = tk.Label(window, text="Result:")
result_label.pack()

window.mainloop()
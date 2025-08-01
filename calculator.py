from tkinter import *

# ---------- Core logic ----------
def button_press(char):
    global equation_text
    equation_text += str(char)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        # Convert [] and {} to () so Python can evaluate
        expr = (equation_text
                .replace('[', '(').replace(']', ')')
                .replace('{', '(').replace('}', ')'))
        result = str(eval(expr))
        equation_label.set(result)
        equation_text = result
    except (SyntaxError, ZeroDivisionError):
        equation_label.set("error")
        equation_text = ""

def clear_all():
    global equation_text
    equation_text = ""
    equation_label.set("")

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

# ---------- GUI ----------
window = Tk()
window.title("Calculator — BODMAS + All Brackets")
window.geometry("520x720")

equation_text = ""
equation_label = StringVar()

display = Label(window, textvariable=equation_label,
                font=("consolas", 20), bg="white",
                width=24, height=2)
display.pack(pady=10)

frame = Frame(window)
frame.pack()

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('/', 3, 3),
    ('(', 4, 0), (')', 4, 1), ('{', 4, 2), ('}', 4, 3),
    ('[', 5, 0), (']', 5, 1), ('←', 5, 2)  # backspace
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = equals
    elif text == '←':
        cmd = backspace
    else:
        cmd = lambda t=text: button_press(t)
    Button(frame, text=text, height=4, width=9, font=35,
           command=cmd).grid(row=row, column=col)

Button(window, text="Clear", height=3, width=20, font=35,
       bg="#ff6666", command=clear_all).pack(pady=20)

window.mainloop()

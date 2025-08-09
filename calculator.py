import tkinter as tk


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error!")

def clean():
    entry.delete(0, tk.END)

def on_button_click(char):
    if char == '=':
        calculate()
    elif char == 'C':
        clean()
    else:
        current = entry.get()
        if current == "Error":
            clean()
        entry.insert(tk.END, char)

def disable_keyboard_input(event):
    return "break"

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg = "#2e2e2e")

button_bg = '#3e3e3e'
button_fg = '#ffffff'
button_active_bg = '#4e4e4e'
entry_bg = '#252525'
entry_fg = '#ffffff'
font = ('Arial', 14)

entry = tk.Entry(
    root,
    width=20,
    font=font,
    justify='right',
    bg=entry_bg,
    fg=entry_fg,
    insertbackground='white',
    borderwidth=0,
    relief=tk.FLAT
)

entry.grid(row=0, column=0, columnspan=4, pady=(20, 10), padx=10, ipady=10)
entry.bind('<Key>', disable_keyboard_input)


button_style = {
    'font': font,
    'width': 5,
    'height': 2,
    'borderwidth': 0,
    'relief': tk.FLAT,
    'bg': button_bg,
    'fg': button_fg,
    'activebackground': button_active_bg,
    'activeforeground': button_fg
}

operator_style = button_style.copy()
operator_style.update({'bg': '#ff9500', 'activebackground': '#ffaa33'})

equals_style = button_style.copy()
equals_style.update({'bg': '#ff7700', 'activebackground': '#ff8c1a'})

clear_style = button_style.copy()
clear_style.update({'bg': '#a5a5a5', 'fg': '#000000', 'activebackground': '#b5b5b5'})

buttons = [
    ('7', button_style), ('8', button_style), ('9', button_style), ('/', operator_style),
    ('4', button_style), ('5', button_style), ('6', button_style), ('*', operator_style),
    ('1', button_style), ('2', button_style), ('3', button_style), ('-', operator_style),
    ('C', clear_style), ('0', button_style), ('=', equals_style), ('+', operator_style)
]

row, col = 1, 0
for (button, style) in buttons:
    tk.Button(
        root,
        text=button,
        **style,
        command=lambda b=button: on_button_click(b)
    ).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1


canvas = tk.Canvas(root, width=300, height=50, bg='#2e2e2e', highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=(20, 10), padx=10)
canvas.create_rectangle(10, 0, 290, 50, fill=entry_bg, outline=entry_bg)


entry.lift()
root.mainloop()
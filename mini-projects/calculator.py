import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.expression = ""
        self.result_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        # Create display
        display = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        display.grid(row=0, column=0, columnspan=4)
        
        # Create buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]
        
        for (text, row, col, *span) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            if span:
                button.grid(row=row, column=col, columnspan=span[0])
            else:
                button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.result_var.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.result_var.set("Error: Div by 0")
            self.expression = ""
        except Exception as e:
            self.result_var.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

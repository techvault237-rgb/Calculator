import tkinter as tk
import random

class DiamondButton(tk.Canvas):
    def __init__(self, parent, text, command=None, size=80, base_color="cyan", glow_color="lightblue"):
        super().__init__(parent, width=size, height=size, highlightthickness=0, bg="black")
        self.size = size
        self.command = command
        self.text = text
        self.base_color = base_color
        self.glow_color = glow_color

        half = size // 2
        # Diamond shape (rotated square)
        self.diamond = self.create_polygon(
            half, 0, size, half, half, size, 0, half,
            fill=self.base_color, outline="white", width=3
        )
        self.label = self.create_text(half, half, text=text, font=("Arial", 16, "bold"), fill="black")

        # Bind events
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

        # Glitter animation
        self.after(500, self.add_glitter)

    def on_click(self, event):
        if self.command:
            self.command()

    def on_hover(self, event):
        self.itemconfig(self.diamond, fill=self.glow_color)

    def on_leave(self, event):
        self.itemconfig(self.diamond, fill=self.base_color)

    def add_glitter(self):
        # Random glitter sparkles
        x = random.randint(10, self.size-10)
        y = random.randint(10, self.size-10)
        sparkle = self.create_oval(x, y, x+3, y+3, fill="yellow", outline="")
        self.after(200, lambda: self.delete(sparkle))
        self.after(500, self.add_glitter)


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Diamond Calculator")
        self.root.configure(bg="black")
        self.root.resizable(False, False)
        self.calculation = ""
        self.display_entry()
        self.display_buttons()
        self.disable_keyboard_input()

    def display_entry(self):
        result_frame = tk.Frame(self.root, bg="black")
        result_frame.pack(padx=10, pady=10)

        self.text_result = tk.Text(result_frame, height=3, width=25, font=("Arial", 24), bg="black", fg="white")
        self.text_result.grid(columnspan=5)

    def display_buttons(self):
        button_frame = tk.Frame(self.root, bg="black")
        button_frame.pack(pady=10)

        # Helper to place diamond buttons
        def make_btn(text, row, col, cmd=None, color="cyan"):
            btn = DiamondButton(button_frame, text=text, command=cmd, base_color=color)
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Digits
        make_btn("1", 2, 1, lambda: self.add_to_calculation(1))
        make_btn("2", 2, 2, lambda: self.add_to_calculation(2))
        make_btn("3", 2, 3, lambda: self.add_to_calculation(3))
        make_btn("4", 3, 1, lambda: self.add_to_calculation(4))
        make_btn("5", 3, 2, lambda: self.add_to_calculation(5))
        make_btn("6", 3, 3, lambda: self.add_to_calculation(6))
        make_btn("7", 4, 1, lambda: self.add_to_calculation(7))
        make_btn("8", 4, 2, lambda: self.add_to_calculation(8))
        make_btn("9", 4, 3, lambda: self.add_to_calculation(9))
        make_btn("0", 5, 2, lambda: self.add_to_calculation(0))

        # Operators
        make_btn("+", 2, 4, lambda: self.add_to_calculation("+"), "magenta")
        make_btn("-", 3, 4, lambda: self.add_to_calculation("-"), "magenta")
        make_btn("*", 4, 4, lambda: self.add_to_calculation("*"), "magenta")
        make_btn("/", 5, 4, lambda: self.add_to_calculation("/"), "magenta")
        make_btn("(", 5, 1, lambda: self.add_to_calculation("("), "orange")
        make_btn(")", 5, 3, lambda: self.add_to_calculation(")"), "orange")

        # Equals and Clear
        make_btn("=", 6, 3, self.evaluate_calculation, "lime")
        make_btn("C", 6, 1, self.clear_field, "red")

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(1.0, self.calculation)

    def evaluate_calculation(self):
        try:
            calculation = str(eval(self.calculation))
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(1.0, calculation)
        except Exception:
            self.clear_field()
            self.text_result.insert(1.0, "Error")

    def clear_field(self):
        self.calculation = ""
        self.text_result.delete(1.0, tk.END)

    def disable_keyboard_input(self):
        self.text_result.bind("<Key>", lambda e: "break")

    def mainloop(self):
        self.root.mainloop()


def main():
    app = Calculator()
    app.mainloop()


if __name__ == "__main__":
    main()
from tkinter import Tk, StringVar, Button
from tkinter.messagebox import showerror
from tkinter.ttk import Label, Frame, Entry, Style
from string_as_a_float import string_as_a_float
from calculate_change import calculate_change


class App:
    def __init__(self):
        self._master = Tk()
        self._init_master_config()
        self._create_widgets()
        self._load_styles()
    
    def _create_widgets(self) -> None:
        win = self._master
        self._field_frame = Frame(win)
        self._coins_frame = Frame(win)
        self._product_value: StringVar = self._make_entry_with_label(
            self._field_frame, "Digite o valor do produto:",
            name="_product_value"
        )
        self._amount_received: StringVar = self._make_entry_with_label(
            self._field_frame, "Digite o valor recebido:",
            name="_amount_received"
        )
        self._calculate_button = Button(self._field_frame, text="Calcular")
        self._calculate_button.bind("<Button>", self._set_coins_label_change)
        self._calculate_button.grid(sticky="W")
        self._label_change = Label(self._field_frame, text="Troco: R$ 0,0")
        self._label_change.grid(sticky="E", column="0", row="5", columnspan="2")
        self._make_coins_labels()
        self._field_frame.grid(sticky="W")
        self._coins_frame.grid(column=0, sticky="W")
    
    def _load_styles(self) -> None:
        self.default_bg_color = "#F3E9D2"
        self.default_fg_color = "#000000"
        self._master.configure(bg=self.default_bg_color)
        s = Style().configure("TFrame",background=self.default_bg_color)
        self._field_frame.configure(style="TFrame")
        self._coins_frame.configure(style="TFrame")
        self._field_frame.grid(padx=5, pady=5)
        self._coins_frame.grid(padx=5, pady=5)
        self._add_padding_in_the_children_frame(self._field_frame, 5, 1)
        self._add_padding_in_the_children_frame(self._coins_frame, 5, 1)
        self._add_style_in_the_children_frame(self._field_frame)
        self._add_style_in_the_children_frame(self._coins_frame)
        self._calculate_button.configure(
            background="#19647E",
            foreground="#F3E9D2",
            activebackground="#731DD8",
            activeforeground="#F3E9D2",
            cursor="hand2"
        )
        self._calculate_button.grid(pady=4)

    def _set_coins_label_change(self, event) -> None:
        prod_value = float(self._product_value.get() or 0)
        received = float(self._amount_received.get() or 0)
        coins_list: list = self.coins_list
        result: list = calculate_change(coins_list, prod_value, received)
        if not result:
            showerror("Operação inválida.", "Valor recebido insuficiente.")
            return
        for index, coins in enumerate(coins_list):
            label = getattr(self, f"_{coins}")
            text = f"\n{result[index]} x R$ {coins:.2f}\n"
            fg = "#F6A23C" if result[index] else "#B497D6"
            label.configure(text=text, foreground=fg)

    def _add_padding_in_the_children_frame(self, frame, padx, pady):
        for children in frame.winfo_children():
            children.grid(padx=padx, pady=pady)

    def _add_style_in_the_children_frame(self, frame):
        for children in frame.winfo_children():
            is_label = True if "label" in str(children) else False
            fg = self.default_fg_color if is_label else "#000000"
            style = {
                 "font": ("Arial", 12, "bold"),
                 "background": self.default_bg_color,
                 "foreground": fg
            }
            style2 = {
                "font": ("Arial", 12, "bold"),
                "background": "#000000",
                "foreground": "#B497D6",
                "width": "16",
                "anchor": "center"
            }
            s = style2 if str(frame.winfo_name()) == "!frame2" else style
            children.configure(**s)

    def _thread_format_fields(self, event) -> None:
        from threading import Thread
        t = Thread(target=self._as_a_floating_value, kwargs={'event': event})
        t.start()
        
    def _as_a_floating_value(self, event) -> None:
        string_var_name: str = event.widget.winfo_name()
        string_var: StringVar = getattr(self, string_var_name)
        value: str = string_var.get()
        value_without_spaces: str = value.strip()
        value_like_float: str = string_as_a_float(value_without_spaces)
        string_var.set(value_like_float)

    def _set_product_value(self, value: str) -> None:
        self._product_value.set(value)
    
    def _get_amount_received(self, value: str) -> None:
        self._amount_received.set(value)

    def _get_product_value(self) -> str:
        value: str = self._product_value.get()
        return value

    def _get_amount_received(self) -> str:
        value: str = self._amount_received.get()
        return value

    def _make_coins_labels(self) -> None:
        self.coins_list = [
            200, 100, 50, 20, 10, 5, 
            2, 1, 0.5, 0.25, 0.10, 0.05, 0.01
        ]
        coins = self.coins_list
        frame = self._coins_frame
        [
            setattr(self,
                f"_{num}",
                self._make_labels(frame, f"0 x R$ {num:.2f}")
            )
            for num in coins
        ]

    def _make_labels(self, frame, text, col=2) -> Label:
        len_= self._lenght_children(frame)
        label = Label(frame, text=f"\n{text}\n")
        row = len_ // col
        column = len_ % col
        label.grid(row=row, column=column, sticky="W")
        return label

    def _make_entry_with_label(self, frame, label_text,name) -> StringVar:
        entry_value = StringVar()
        label = Label(frame, text=label_text)
        entry = Entry(frame, width=9, textvariable=entry_value, name=name)
        label.grid(row=self._lenght_children(frame), column=0, sticky="W")
        entry.grid(row=self._lenght_children(frame), column=1, sticky="W")
        entry.bind("<Any-KeyPress>", self._thread_format_fields)
        entry.bind("<KeyRelease>", self._thread_format_fields)
        return entry_value

    @staticmethod
    def _lenght_children(obj) -> int:
        len_ = len(obj.winfo_children())
        return len_

    def _init_master_config(self) -> None:
        self._master.title("Maquininha de Troco")
        self._set_master_geometry()
        self._master.resizable(width=False, height=False)
    
    def _set_master_geometry(self) -> None:
        width = 330
        height = 560
        x: int = self._get_center_x(width)
        y: int = self._get_center_y(height)
        self._master.geometry(f"{width}x{height}+{x}+{y}")
    
    def _get_center_x(self, width) -> int:
        win = self._master
        system_window_width: int = win.winfo_screenwidth()
        x = system_window_width/2 - width/2
        return round(x)

    def _get_center_y(self, height) -> int:
        win = self._master
        system_window_height: int = win.winfo_screenheight()
        y = system_window_height/2 - height/2
        center_plus_10_percent_up = y - height * 0.1
        return round(center_plus_10_percent_up)

    def run_looping(self) -> None:
        self._master.mainloop()


if __name__ == "__main__":
    app = App()
    app.run_looping()
    
from tkinter import Tk, StringVar
from tkinter.ttk import Label, Frame, Entry
from string_as_a_float import string_as_a_float


class App:
    def __init__(self):
        self._master = Tk()
        self._init_master_config()
        self._create_widgets()
    
    def _create_widgets(self) -> None:
        win = self._master
        master_frame = Frame(win)
        self.coins_frame = Frame(win)
        self._product_value: StringVar = self._make_entry_with_label(
            master_frame, "Digite o valor do produto:",
            name="_product_value"
        )
        self._amount_received: StringVar = self._make_entry_with_label(
            master_frame, "Digite o valor recebido:",
            name="_amount_received"
        )
        self._make_coins_labels()
        master_frame.grid(sticky="W")
        self.coins_frame.grid(column=0, sticky="W")
    
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
        frame = self.coins_frame
        [
            setattr(self,
                f"_{num}",
                self._make_labels(frame, f"0 x R$ {num:.2f}")
            )
            for num in coins
        ]

    def _make_labels(self, frame, text, col=3) -> Label:
        len_= self._lenght_children(frame)
        label = Label(frame, text=text)
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
        width = 400
        height = 400
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
        center_plus_30_percent_up = y - height * 0.3
        return round(center_plus_30_percent_up)

    def run_looping(self) -> None:
        self._master.mainloop()


app = App()
app.run_looping()

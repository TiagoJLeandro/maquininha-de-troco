from tkinter import Tk, DoubleVar
from tkinter.ttk import Label, Frame, Entry


class App:
    def __init__(self):
        self._master = Tk()
        self._init_master_config()
        self._create_widgets()
    
    def _create_widgets(self) -> None:
        win = self._master
        master_frame = Frame(win)
        self.coins_frame = Frame(win)
        self._product_value: DoubleVar = self._make_float_entry_with_label(
            master_frame, "Digite o valor do produto:"
        )
        self._amount_received: DoubleVar = self._make_float_entry_with_label(
            master_frame, "Digite o valor recebido:"
        )
        self._make_coins_labels()
        master_frame.grid(sticky="W")
        self.coins_frame.grid(column=0, sticky="W")
    
    def _get_product_value(self) -> float:
        value: float = self._product_value.get()
        return value

    def _get_amount_received(self) -> float:
        value: float = self._amount_received.get()
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

    def _make_float_entry_with_label(self, frame, label_text) -> DoubleVar:
        entry_value = DoubleVar()
        label = Label(frame, text=label_text)
        entry = Entry(frame, width=7)
        label.grid(row=self._lenght_children(frame), column=0, sticky="W")
        entry.grid(row=self._lenght_children(frame), column=1, sticky="W")
        return entry_value 

    @staticmethod
    def _lenght_children(obj) -> int:
        len_ = len(obj.winfo_children())
        return len_

    def _init_master_config(self) -> None:
        self._master.title("Maquininha de Troco")
        self._set_geometry_to_master()
        self._master.resizable(width=False, height=False)
    
    def _set_geometry_to_master(self) -> None:
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

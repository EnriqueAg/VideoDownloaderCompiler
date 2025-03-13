import customtkinter # cttk_spinbox is a custom widget based on customtkinter
from typing import Union, Callable

class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args, width: int = 100, height: int = 32, step_size: Union[int, float] = 1, command: Callable = None, low_limit: Union[int, int] = None, high_limit: Union[int, int] = None, default_value: Union[int, int] = 0, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.step_size = step_size
        self.command = command
        self.low_limit = low_limit
        self.high_limit = high_limit

        self.configure(fg_color=("gray78", "gray28"))  # Set frame color
        self.grid_columnconfigure((0, 2), weight=0)  # Buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # Entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6, command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6, command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # Set default value
        self.entry.insert(0, str(int(default_value)))

    def add_button_callback(self):
        # Try to increment the value
        try:
            value = int(self.entry.get()) + self.step_size
            # Enforce high limit
            if self.high_limit is not None and value > self.high_limit:
                value = self.high_limit
            self.entry.delete(0, "end")
            self.entry.insert(0, value)

            # Then call the command (if any)
            if self.command is not None:
                self.command()
        except ValueError:
            return

    def subtract_button_callback(self):
        # Try to decrement the value
        try:
            value = int(self.entry.get()) - self.step_size
            # Enforce low limit
            if self.low_limit is not None and value < self.low_limit:
                value = self.low_limit
            self.entry.delete(0, "end")
            self.entry.insert(0, value)

            # Then call the command (if any)
            if self.command is not None:
                self.command()
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        # Try to get the value
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        # Try to set the value
        # Enforce limits when setting the value
        if self.low_limit is not None and value < self.low_limit:
            value = self.low_limit
        if self.high_limit is not None and value > self.high_limit:
            value = self.high_limit
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))
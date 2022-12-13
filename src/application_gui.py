import tkinter
import customtkinter as tk
import gettext
import os

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

LOCALE = os.getenv('LANG', 'de')
_ = gettext.translation('messages', localedir='i18n', languages=[LOCALE]).gettext


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        # variables:
        self.language = "english"

        # configure window
        self.title("GAASP - Audio Analyser Sound Player")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create tabview
        self.tabview = tk.CTkTabview(master=self)
        self.tabview.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.tabview.add(_("ESAAO"))
        self.tabview.add(_("Settings"))
        self.tabview.add(_("About"))

        # ESAAO window
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = tk.CTkLabel(master=self.tabview.tab(_("ESAAO")), text=_("Choose Language:"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = tk.CTkRadioButton(master=self.tabview.tab(_("ESAAO")), value=0, text=_("english")
                                                , variable=self.radio_var, command=self.setLanguageEnglishEvent())
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = tk.CTkRadioButton(master=self.tabview.tab(_("ESAAO")), value=1, text=_("german")
                                                , variable=self.radio_var, command=self.setLanguageGermanEvent())
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # Settings Window
        self.appearance_mode_label_settings1 = tk.CTkLabel(self.tabview.tab(_("Settings")),
                                                           text=_("Appearance Mode:"),
                                                           anchor="w")
        self.appearance_mode_label_settings1.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = tk.CTkOptionMenu(self.tabview.tab(_("Settings")),
                                                           values=["Light", "Dark", "System"],
                                                           command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionmenu.set("System")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        tk.set_appearance_mode(new_appearance_mode)

    def setLanguageEnglishEvent(self):
        self.language = "english"

    def setLanguageGermanEvent(self):
        self.language = "german"

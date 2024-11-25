import customtkinter
from GUIConfig import GUIConfig
from loginGUI import loginGUI

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("customTheme.json")

app = loginGUI()
app.mainloop()

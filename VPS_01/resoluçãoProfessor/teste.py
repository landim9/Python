import customtkinter as ctk

ctk.set_appearance_mode("Dark")

def button_callback():
    print("button clicked")

app = ctk.CTk()
app.title("Teste")
app.geometry("600x400")

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()
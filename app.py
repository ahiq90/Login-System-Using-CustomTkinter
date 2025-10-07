import customtkinter as ctk
from tkinter import messagebox

# ====== USER DATA ======
user = {
    "username": "abohashim",
    "pass": "abohashim",
    "name": "Ahmed Hashim",
    "age": 25,
    "mail": "abohashim@mail.ru"
}

attempts = 3

# ====== LOGIN FUNCTION ======
def login():
    global attempts
    username = entry_user.get()
    password = entry_pass.get()

    if username == user["username"] and password == user["pass"]:
        messagebox.showinfo("Success ✅",
                            f"Welcome, {user['name']}!\n\nAge: {user['age']}\nEmail: {user['mail']}")
        app.destroy()
    else:
        attempts -= 1
        if attempts > 0:
            messagebox.showwarning("Error ❌", f"Wrong credentials! {attempts} attempts left.")
        else:
            messagebox.showerror("Account Locked 🚫", "User data deleted. Account is locked.")
            user.clear()
            app.destroy()

# ====== APP SETTINGS ======
ctk.set_appearance_mode("dark")        # Modes: "dark", "light", "system"
ctk.set_default_color_theme("blue")    # Themes: "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Login System")
app.geometry("350x300")

# ====== TITLE ======
label_title = ctk.CTkLabel(app, text="User Login", font=ctk.CTkFont(size=20, weight="bold"))
label_title.pack(pady=20)

# ====== USERNAME ======
entry_user = ctk.CTkEntry(app, placeholder_text="Username")
entry_user.pack(pady=10)

# ====== PASSWORD ======
entry_pass = ctk.CTkEntry(app, placeholder_text="Password", show="*")
entry_pass.pack(pady=10)

# ====== LOGIN BUTTON ======
btn_login = ctk.CTkButton(app, text="Login", command=login)
btn_login.pack(pady=15)

# ====== FOOTER ======
footer_label = ctk.CTkLabel(app, text="Developed by Abo Hashim",
                            font=ctk.CTkFont(size=12, slant="italic"), text_color="#888")
footer_label.pack(side="bottom", pady=10)

# ====== RUN APP ======
app.mainloop()

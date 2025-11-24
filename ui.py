import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from db import init_db, create_user, get_user
from utils import hash_password, verify_password


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login / Cadastro")
        self.geometry("420x320")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self._create_frames()

    def _create_frames(self):
        self.login_frame = ctk.CTkFrame(self)
        self.register_frame = ctk.CTkFrame(self)

        # --- login ---
        lbl = ctk.CTkLabel(self.login_frame, text="Login", font=ctk.CTkFont(size=20, weight="bold"))
        lbl.pack(pady=(20, 8))

        self.login_user = ctk.CTkEntry(self.login_frame, placeholder_text="Usuário")
        self.login_user.pack(pady=6, padx=20, fill="x")

        self.login_pass = ctk.CTkEntry(self.login_frame, placeholder_text="Senha", show="*")
        self.login_pass.pack(pady=6, padx=20, fill="x")

        btn_login = ctk.CTkButton(self.login_frame, text="Entrar", command=self.login)
        btn_login.pack(pady=10)

        btn_to_reg = ctk.CTkButton(self.login_frame, text="Criar conta", fg_color=None, command=self.show_register)
        btn_to_reg.pack()

        # --- register ---
        lbl2 = ctk.CTkLabel(self.register_frame, text="Cadastro", font=ctk.CTkFont(size=20, weight="bold"))
        lbl2.pack(pady=(20, 8))

        self.reg_user = ctk.CTkEntry(self.register_frame, placeholder_text="Usuário")
        self.reg_user.pack(pady=6, padx=20, fill="x")

        self.reg_pass = ctk.CTkEntry(self.register_frame, placeholder_text="Senha", show="*")
        self.reg_pass.pack(pady=6, padx=20, fill="x")

        self.reg_pass2 = ctk.CTkEntry(self.register_frame, placeholder_text="Confirmar senha", show="*")
        self.reg_pass2.pack(pady=6, padx=20, fill="x")

        btn_create = ctk.CTkButton(self.register_frame, text="Cadastrar", command=self.register)
        btn_create.pack(pady=10)

        btn_back = ctk.CTkButton(self.register_frame, text="Voltar ao login", fg_color=None, command=self.show_login)
        btn_back.pack()

        self.login_frame.pack(fill="both", expand=True)

    def show_register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)

    def show_login(self):
        self.register_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def login(self):
        username = self.login_user.get().strip()
        password = self.login_pass.get()
        if not username or not password:
            messagebox.showerror("Erro", "Preencha usuário e senha")
            return
        user = get_user(username)
        if not user:
            messagebox.showerror("Erro", "Usuário não encontrado")
            return
        if verify_password(password, user["password_hash"]):
            messagebox.showinfo("Sucesso", f"Bem-vindo, {username}!")
            self.login_user.delete(0, tk.END)
            self.login_pass.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Senha incorreta")

    def register(self):
        username = self.reg_user.get().strip()
        p1 = self.reg_pass.get()
        p2 = self.reg_pass2.get()
        if not username or not p1 or not p2:
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        if p1 != p2:
            messagebox.showerror("Erro", "Senhas não conferem")
            return
        password_hash = hash_password(p1)
        ok = create_user(username, password_hash)
        if ok:
            messagebox.showinfo("Sucesso", "Conta criada, faça login.")
            self.show_login()
        else:
            messagebox.showerror("Erro", "Usuário já existe")

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import time
import threading

def gerar_arquivo():
    try:
        quantidade = int(entry_quantidade.get())
        if quantidade <= 0:
            messagebox.showerror("Erro", "Digite um número maior que 0.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números inteiros.")
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt")]
    )

    if not caminho:
        return

    # Executa em thread para não travar a interface
    threading.Thread(target=criar_pedidos, args=(caminho, quantidade)).start()


def criar_pedidos(caminho, quantidade):
    progress["maximum"] = quantidade
    progress["value"] = 0

    with open(caminho, "w", encoding="utf-8") as arquivo:
        for i in range(quantidade):
            if i < 9:
                arquivo.write(f"pedido 0{i + 1}:\n")
            else:
                arquivo.write(f"pedido {i + 1}:\n")

            arquivo.write("Setor >>>\n")
            arquivo.write("Pessoa >>>\n")
            arquivo.write("Conteúdo >>>\n\n")

            time.sleep(0.02)  # Simula carregamento

            progress["value"] += 1
            janela.update_idletasks()

    messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")


# ================= JANELA =================

janela = tk.Tk()
janela.title("Gerador de Pedidos")
janela.geometry("400x220")
janela.resizable(False, False)

tk.Label(janela, text="Quantidade de pedidos:", font=("Arial", 12)).pack(pady=10)

entry_quantidade = tk.Entry(janela, font=("Arial", 12), justify="center")
entry_quantidade.pack()

tk.Button(
    janela,
    text="Gerar Lista",
    font=("Arial", 12),
    command=gerar_arquivo
).pack(pady=15)

progress = Progressbar(janela, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

janela.mainloop()
import tkinter as tk
from tkinter import messagebox

# Função que será chamada quando o botão for clicado
def on_button_click():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

# Define o tamanho da janela
root.geometry("300x200")

# Cria um botão e o posiciona na janela
button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=20)  # 'pady' adiciona um espaçamento vertical

# Inicia o loop principal da interface gráfica
root.mainloop()
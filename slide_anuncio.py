import platform
import tkinter as tk
from screeninfo import get_monitors

import funcionalidades


def iniciar_apresentacao(texto):

    # Funções
    def fechar(event=None):
        janela_slide.destroy()


    # Janela principal
    monitors = get_monitors()

    if len(monitors) == 2:
        second = monitors[1]
    else:
        second = monitors[0]

    janela_slide = tk.Toplevel()
    janela_slide.title("Segunda Tela")
    janela_slide.geometry(f"{second.width}x{second.height}+{second.x}+{second.y}")
    janela_slide.attributes("-fullscreen", True)
    #root.bind("<Escape>", fechar)

    # Maximiza a janela após abrir e remove barra de título
    if not platform.system() == "Windows":
        janela_slide.overrideredirect(True)
    else:
        janela_slide.attributes("-topmost", True)  # força ficar na frente

    if texto == "Fechar":
        janela_slide.destroy()

    # Visualização
    font = ["Arial", 20, "bold"]
    label_title = tk.Label(
        janela_slide,
        text="Anúncios",
        font=(font[0], font[1] * 2, font[2]),
        fg="white",
        bg="black",
        justify="center"
    )
    label_title.pack(expand=True, fill="both")

    label = tk.Label(
        janela_slide,
        text=texto,
        font=(font[0], font[1] * 4, font[2]),
        fg="white",  # cor do texto
        bg="black",  # cor do fundo
        anchor="w",
        justify="left",
        wraplength=second.width - 20,
    )
    label.pack(expand=True, fill="both")
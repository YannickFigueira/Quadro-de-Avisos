import platform
import tkinter as tk
from screeninfo import get_monitors

import funcionalidades


def iniciar_apresentacao(root, texto):

    #Janela
    # Janela principal
    monitors = get_monitors()

    if len(monitors) == 2:
        second = monitors[1]
    else:
        second = monitors[0]

    janela_slide = tk.Toplevel(root)
    janela_slide.title("Segunda Tela")
    janela_slide.geometry(f"{second.width}x{second.height}+{second.x}+{second.y}")

    # Maximiza a janela após abrir e remove barra de título
    if not platform.system() == "Windows":
        janela_slide.overrideredirect(True)
    else:
        janela_slide.attributes("-topmost", True)  # força ficar na frente

    janela_slide.attributes("-fullscreen", True)

    janela_slide.texto_lbl = tk.Label(janela_slide, text=texto[0])
    janela_slide.texto_lbl.grid(row=1, column=1, padx=5, pady=5)
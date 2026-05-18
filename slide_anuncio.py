import platform
import tkinter as tk
from screeninfo import get_monitors


def iniciar_apresentacao(root, arquivo):

    #Janela
    # Janela principal
    monitors = get_monitors()

    if len(monitors) == 2:
        second = monitors[1]
    else:
        second = monitors[0]

    janela_slide = tk.Toplevel()
    janela_slide.title("Segunda Tela")
    janela_slide.geometry(f"{second.width}x{second.height}+{second.x}+{second.y}")

    # Maximiza a janela após abrir e remove barra de título
    if not platform.system() == "Windows":
        janela_slide.overrideredirect(True)
    else:
        janela_slide.attributes("-topmost", True)  # força ficar na frente

    janela_slide.attributes("-fullscreen", True)
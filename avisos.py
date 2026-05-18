import tkinter as tk
import argparse, funcionalidades, slide_anuncio

VERSION='1.0.0'
class Avisos:
    # Principal
    def __init__(self, root):

        # Versão para deb
        parser = argparse.ArgumentParser(prog="avisos")
        parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

        # Janela
        self.root = root
        self.root.title('Anúncios')
        self.root.resizable(False, False)

        # Controle
        linha = 0

        self.selecao_lbl = tk.Label(self.root, text='Selecione o arquivo para anúncio')
        self.selecao_lbl.grid(row=linha, column=1, padx=5, pady=5)
        linha += 1

        self.carregar_arquivo_btn=tk.Button(self.root, text='Carregar Arquivo',
                                            command=lambda: slide_anuncio.iniciar_apresentacao(root, funcionalidades.selecionar_arquivo()))
        self.carregar_arquivo_btn.grid(row=linha, column=1, padx=5, pady=5)


if __name__ == '__main__':
    avisos = tk.Tk()
    app = Avisos(avisos)
    avisos.mainloop()
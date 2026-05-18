import os
from tkinter import filedialog, messagebox

import slide_anuncio


def selecionar_arquivo(root):
    # Define o caminho padrão expandindo o $USER atual do sistema de forma segura
    # No Linux/Mac, isso aponta para /home/usuario/Documentos (ou Documentos com "D" maiúsculo)
    diretorio_padrao = os.path.expanduser("~/Documentos")

    # Se a pasta "Documentos" em português não existir, tenta em inglês ou usa a Home
    if not os.path.exists(diretorio_padrao):
        diretorio_padrao = os.path.expanduser("~/Documents")
    if not os.path.exists(diretorio_padrao):
        diretorio_padrao = os.path.expanduser("~")

    # Abre o seletor focado em arquivos .txt
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo TXT",
        initialdir=diretorio_padrao,
        filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )

    if arquivo:  # Se o usuário não cancelar
        carregar_texto(root, arquivo)
    else:
        carregar_texto(root, "")


def carregar_texto(root, arquivo):

    if os.path.isfile(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            texto = f.read()
            paragrafo = [p.strip() for p in texto.split("\n\n") if p.strip()]
            slide_anuncio.iniciar_apresentacao(root, paragrafo)
    else:
        messagebox.showerror("Erro", f"Arquivo não encontrado: {arquivo}")
import os

from tkinter import filedialog


def selecionar_arquivo():
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
        return arquivo
    else:
        return ""
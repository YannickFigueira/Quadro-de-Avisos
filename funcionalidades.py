import os
import threading
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
        carregar_texto(arquivo)
    else:
        carregar_texto("")


def carregar_texto(arquivo):

    if os.path.isfile(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            texto = f.read()
            #paragrafo = [p.strip() for p in texto.split("\n\n") if p.strip()]
            slide_anuncio.iniciar_apresentacao(texto)
    else:
        messagebox.showerror("Erro", f"Arquivo não encontrado: {arquivo}")

def carrgar_bot(root):
    # Telegram recebendo texto para o slide
    import asyncio
    from telegram import Update
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


    # 1. Função que responde ao comando /start
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Olá! Envie um texto que eu vou processar para o painel de anúncios.")


    # 2. Função que RECEBE e lê qualquer texto enviado
    async def receber_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
        # Aqui capturamos o texto que o usuário digitou
        texto_recebido = update.message.text
        nome_usuario = update.message.from_user.first_name

        print(f"Mensagem recebida de {nome_usuario}: {texto_recebido}")
        slide_anuncio.iniciar_apresentacao(texto_recebido)
    '''
        # Exemplo de lógica integrada ao seu sistema
        if texto_recebido.lower() == "mudar slide":
            # Aqui você chamará a lógica para atualizar seu slide_anuncio.py
            await update.message.reply_text("Comando aceito! Atualizando o painel...")
        else:
            await update.message.reply_text(f"Texto recebido: '{texto_recebido}'")
    '''

    # 3. Configuração e inicialização do Bot
    def iniciar_bot():
        TOKEN = ""

        # Criamos a aplicação com o token do bot
        application = Application.builder().token(TOKEN).build()

        # Dizemos ao bot o que fazer quando receber comandos ou textos
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_texto))


        # Inicia o Polling (fica escutando o Telegram de forma contínua)
        print("Bot do Telegram iniciado e escutando...")
        application.run_polling(close_loop=False, stop_signals=None)

    def executar_bot():
        t = threading.Thread(target=iniciar_bot, args=(), daemon=True)
        t.start()

    executar_bot()

#OBS: No Pycharm é necessário baixar os módulos PILLOW e PILLOW PIL. No terminal instalar o pip install pyinstaller
#OBS.2: Renomear o arquivo main para a extensão .pyw para excluir a janela preta. No terminal criar executável a partir do código: pyinstaller --onefile main.pyw
#Depois de criado, retirar da pasta dist e jogar para a pasta do projeto > ctrl+c, ctrl+v para onde desejado.
#OBS.3: Necessário ter a versão do webbrowser do navegador(baixar a partir do google), vide versão em 'ajuda' > 'sobre o google chrome' - ps: é preciso estar na pasta jupyter do C:.
#OBS.4: O usuário não precisa baixar nada, só extrair as imagens do arquivo zip do programa.

import tkinter as tk
import tkinter.font
import webbrowser
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk



root = tk.Tk() #criação da janela
root.resizable(False, False) #não permite a janela ser redimensionado
root.geometry("557x692+1+1") #tamanho x e y + local fixo que a janela será aberta 
root.title("LIBRARY-LAB") #título da janela
image = Image.open("3.png") #importando a imagem de fundo
photo = ImageTk.PhotoImage(image) #definindo a imagem
label = tk.Label(root, image=photo, bd=0) #definindo a imagem na janela principal
label.image = photo #inserindo a imagem de fundo
label.grid(row=2, column=0)  # posicionamento da imagem 

# ícone
root.iconbitmap("icone.ico")

# fonte do texto
myFont1 = tkinter.font.Font(family='Abril', size=12)  # Abril/Candara

# texto do cabeçalho
texto = tk.Label(root,
                 text='Escolha um livro nas seções abaixo ou\nclique no botão ao lado para ler um livro aleatório.',
                 font=myFont1, bg='black', fg='#FFFFDE')  # fg cor da fonte
texto.place(x=20, y=30)

#função do webbrowser para abrir qualquer link no navegador
def OpenUrl():
    webbrowser.open_new(url)


# site do botão aleatório
url = "https://drive.google.com/file/d/1k1NZAi-jxMmFqyIGfHuDlOPv4vU-hmTc/view?usp=sharing"

# fonte do botão aleatório
myFont = tkinter.font.Font(family='Candara', weight='bold', size=10)

# criação do botão aleatório
button = tk.Button(root, text="QUERO LER UM LIVRO\nALEATÓRIO!", command=lambda aurl=url: OpenUrl(), bg='indigo',
                   borderwidth=5, font=myFont, relief="ridge", fg='#ffffff', cursor="hand2")
#localização do botão aleatório(o place permite ser alocado no local especifícado por x e y)
button.place(x=393, y=30)


# COMBOBOX 01 - SUSPENSE

#função do combobox 01
def livro_selecionado(event):
    dicio = {
        ' Billy Summers - EN ': 'https://www.google.com.br/books/edition/Billy_Summers/L3oXEAAAQBAJ?hl=pt-BR&gbpv=1&dq=billy+summers&printsec=frontcover',
        ' Outsider': 'https://www.google.com.br/books/edition/Outsider/YONaDwAAQBAJ?hl=pt-BR&gbpv=1&dq=outsider&printsec=frontcover'}

    a = escolha1.get()

    msg = f'Você selecionou a pré-visualização do livro{a}\n\n             Não esqueça de deixar seu feedback.\n         Sua opinião é muito importante para mim!'

    webbrowser.open_new(dicio[a])

    showinfo(title='Boa leitura!', message=msg)

#estilo do combobox 01
combo1 = tk.StringVar()
fontStyle = ("Candara", 11, "italic")
escolha1 = ttk.Combobox(root, width=23, textvariable=combo1, state='readonly', font=fontStyle)

# adicionado a lista no combobox 01
escolha1['values'] = (' Billy Summers - EN ',
                      ' Outsider',)

escolha1.place(x=15, y=150)
escolha1.current()

escolha1.bind('<<ComboboxSelected>>', livro_selecionado)

#título do combobox 01
texto1 = tk.Label(root, text='                                      Suspense', font=fontStyle, bg='black', fg='#9B10B0',
                  width=23, height=1)
texto1.place(x=15, y=150)


# COMBOBOX 02 -FICÇÃO CIENTÍFICA

#função do combobox 02
def livro_selecionado2(event):
    dicio2 = {
        ' Flores para Algernon ': 'https://www.google.com.br/books/edition/Flores_Para_Algernon/KBdiDwAAQBAJ?hl=pt-BR&gbpv=1&dq=flores+para+algernon&printsec=frontcover',
        ' Frankstein ': 'https://www.google.com.br/books/edition/Frankenstein/e_JgCwAAQBAJ?hl=pt-BR&gbpv=1&dq=frankenstein+portugues&printsec=frontcover'}

    a2 = escolha2.get()

    msg2 = f'Você selecionou a pré-visualização do livro{a2}\n\n             Não esqueça de deixar seu feedback.\n         Sua opinião é muito importante para mim!'

    webbrowser.open_new(dicio2[a2])

    showinfo(title=' Boa leitura! ', message=msg2)


combo2 = tk.StringVar()
fontStyle2 = ("Candara", 11, "italic")
escolha2 = ttk.Combobox(root, width=23, textvariable=combo1, state='readonly', font=fontStyle2)

# adicionando os livros no combobox 02
escolha2['values'] = (' Flores para Algernon ',
                      ' Frankstein ',)

escolha2.place(x=257, y=150)
escolha2.current()

escolha2.bind('<<ComboboxSelected>>', livro_selecionado2)


# botão feedback
def FeedUrl():
    webbrowser.open_new(urlfeed)


urlfeed = r"https://forms.gle/ZPMuERF2ETsxqy148"

myFontfeed = tkinter.font.Font(family='Candara', weight='bold', size=10)

buttonfeed = tk.Button(root, text="feedback", command=lambda aurl=urlfeed: FeedUrl(), bg='black', borderwidth=4,
                       font=myFontfeed, relief="sunken", fg='#ffffff', cursor="hand2")
buttonfeed.place(x=1, y=661)

# título do combobox 02
texto2 = tk.Label(root, text='                          Ficção Científica', font=fontStyle2, bg='black', fg='#9B10B0',
                  width=23, height=1)
texto2.place(x=257, y=150)

# assinatura
assinatura = tk.Label(root, text='evilly', font=fontStyle2, bg='black', fg='#6C0B7A')
assinatura.place(x=518, y=670)

# mantém a janela aberta
root.mainloop()

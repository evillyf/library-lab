# AQUI
# fazer agora: adicionar imagens no execute https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
# de acordo com o feedback gerar outras seções
# gerar outros livros no botao aleatório
import tkinter as tk
import tkinter.font
import webbrowser
from tkinter import ttk
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk



root = tk.Tk()
root.resizable(False, False)
root.geometry("557x692+1+1")
root.title("LIBRARY-LAB")
image = Image.open("3.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo, bd=0)
label.image = photo
label.grid(row=2, column=0)  # 2

# ícone
root.iconbitmap("icone.ico")

# fonte do texto
myFont1 = tkinter.font.Font(family='Abril', size=12)  # Abril/Candara

# texto do cabeçalho
texto = tk.Label(root,
                 text='Escolha um livro nas seções abaixo ou\nclique no botão ao lado para ler um livro aleatório.',
                 font=myFont1, bg='black', fg='#FFFFDE')  # fg cor da fonte
texto.place(x=20, y=30)


def OpenUrl():
    webbrowser.open_new(url)


# site do botão 1
url = "https://drive.google.com/file/d/1k1NZAi-jxMmFqyIGfHuDlOPv4vU-hmTc/view?usp=sharing"

# fonte do botão
myFont = tkinter.font.Font(family='Candara', weight='bold', size=10)

# botão do cabeçalho
button = tk.Button(root, text="QUERO LER UM LIVRO\nALEATÓRIO!", command=lambda aurl=url: OpenUrl(), bg='indigo',
                   borderwidth=5, font=myFont, relief="ridge", fg='#ffffff', cursor="hand2")
button.place(x=393, y=30)


# combobox 01

def livro_selecionado(event):
    dicio = {
        ' Billy Summers - EN ': 'https://www.google.com.br/books/edition/Billy_Summers/L3oXEAAAQBAJ?hl=pt-BR&gbpv=1&dq=billy+summers&printsec=frontcover',
        ' Outsider': 'https://www.google.com.br/books/edition/Outsider/YONaDwAAQBAJ?hl=pt-BR&gbpv=1&dq=outsider&printsec=frontcover'}

    a = escolha1.get()

    msg = f'Você selecionou a pré-visualização do livro{a}\n\n             Não esqueça de deixar seu feedback.\n         Sua opinião é muito importante para mim!'

    webbrowser.open_new(dicio[a])

    showinfo(title='Boa leitura!', message=msg)


combo1 = tk.StringVar()
fontStyle = ("Candara", 11, "italic")
escolha1 = ttk.Combobox(root, width=23, textvariable=combo1, state='readonly', font=fontStyle)

# Adding combobox drop down list
escolha1['values'] = (' Billy Summers - EN ',
                      ' Outsider',)

escolha1.place(x=15, y=150)
escolha1.current()

escolha1.bind('<<ComboboxSelected>>', livro_selecionado)

texto1 = tk.Label(root, text='                                      Suspense', font=fontStyle, bg='black', fg='#9B10B0',
                  width=23, height=1)
texto1.place(x=15, y=150)


# combobox 02
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

# adicionando os livros a lista
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

# título do combobox2
texto2 = tk.Label(root, text='                          Ficção Científica', font=fontStyle2, bg='black', fg='#9B10B0',
                  width=23, height=1)
texto2.place(x=257, y=150)

# assinatura
assinatura = tk.Label(root, text='evilly', font=fontStyle2, bg='black', fg='#6C0B7A')
assinatura.place(x=518, y=670)

# mantém aberta a janela
root.mainloop()
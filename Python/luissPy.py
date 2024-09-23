'''
peso= float(input("coloque o valor do seu peso(kg): "))
altura= float(input("coloque a sua altura(m): "))

imc= peso/altura**2

if(imc<18.5):
    print("abaixo do peso",imc)

elif(imc>=18.5 and imc<24.9):
    print("normal",imc)


elif(imc>= 25 and imc< 29.9):
    print("sobrepeso",imc)

elif(imc>=30 and imc<34.9):
    print("obesidade",imc)

elif(imc>=35 and imc<=39.9):
    print("obesidade mórbida",imc)
'''
#fazer uma lista de items
'''
import tkinter as tk

from tkinter import font, Listbox

tela = tk.Tk()
tela.title("pyhton")
tela.geometry("700x380")

listbox = Listbox(tela)
listbox.pack()
listbox.insert(tk.END," item 1 ","item 2","item 3","item 4","item 5")
tela.mainloop()
'''
''''
import tkinter as tk

from tkinter import font, Listbox


def hello():
    print("Olá")

tela = tk.Tk()

menu_bar = tk.Menu(tela)
tela.config(menu= menu_bar)

file_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="arquivo",menu=file_menu)
menu_bar.add_cascade(label="novo projeto",menu=file_menu)
file_menu.add_command(label="saudar", command= hello )
tela.mainloop()
'''

import tkinter as tk
from PIL import Image, ImageTk

import requests
from io import BytesIO
''''
def imagem_internet(link_da_imagem):
    resposta_do_site = requests.get(link_da_imagem)
    imagem_site = BytesIO(resposta_do_site.content)
    imagem = Image.open(imagem_site)
    imagem = imagem.convert('RGB')
    return imagem

def converter_imagem(imagem):
    with BytesIO() as output :
        imagem.save(output, format = "PPM")
        ppm_imagem = output.getvalue()
    return ppm_imagem

imagem_Url = "https://br.pinterest.com/pin/710654016196180866/"
imagem = imagem_internet(imagem_Url)

tela = bebelly.Tk 

imagem = tk.PhotoImage(data=imagem_ppm)

canvas.create_image(300,400,image=imagem)
'''
'''
import tkinter as tk
from PIL import Image
import requests
from io import BytesIO



def abrir_imagem(img_Url, imagem_canvas):
    nova_imagem = pegaImagemNet(img_Url)
    nova_imagem_ppm = converterImagem(nova_imagem)

    nova_imagem = tk.PhotoImage(data=nova_imagem_ppm)
    canvas.itemconfig(imagem_canvas)

def pegaImagemNet(linkImagem):
    respostaSite = requests.get(linkImagem)
    imagemSite = BytesIO(respostaSite.content)
    imagem = Image.open(imagemSite)
    imagem = imagem.convert('RGB')
    return imagem

def converterImagem(imagem):
    with BytesIO() as output:
        imagem.save(output, format='PPM')
        ppmImagem = output.getvalue()
    return ppmImagem

imgUrl = "https://bit.ly/3ZpyzVB"
imagem1 = pegaImagemNet(imgUrl)

tela = tk.Tk()
tela.title('Phyton')
canvas = tk.Canvas(tela, width=800, height=800)
canvas.pack()

imagem = pegaImagemNet(imgUrl)
imagemPPM = converterImagem(imagem)
imagem = tk.PhotoImage(data=imagemPPM)

canvas.create_image(300, 400,image=imagem)

tela.mainloop()
'''

import tkinter as tk
from PIL import Image
import requests
from io import BytesIO

def pegaImagemNet(linkImagem):
    respostaSite = requests.get(linkImagem)
    imagemSite = BytesIO(respostaSite.content)
    imagem = Image.open(imagemSite)
    imagem = imagem.convert('RGB')
    return imagem

def converterImagem(imagem):
    with BytesIO() as output:
        imagem.save(output, format='PPM')
        ppmImagem = output.getvalue()
    return ppmImagem

def abrirImagem1(imgUrl):
    novaImg = pegaImagemNet(imgUrl)
    novaImgPPM = converterImagem(novaImg)
    novaImg = tk.PhotoImage(data=novaImgPPM)
    canvas.itemconfig(imgCanvas, image=novaImg)

    canvas.image = novaImg

def bosch():
    imgUrl1 = "https://thumbs.dreamstime.com/z/sargento-de-broca-do-emoticon-de-emoji-80531031.jpg?ct=jpeg"
    abrirImagem1(imgUrl1)

imgUrl = "https://www.shutterstock.com/shutterstock/photos/587613737/display_1500/stock-vector-knight-emoticon-holding-a-sword-and-shield-587613737.jpg"
imagem1 = pegaImagemNet(imgUrl)



tela = tk.Tk()
tela.title('Phyton')
canvas = tk.Canvas(tela, width=800, height=800)
canvas.pack()

imagem = pegaImagemNet(imgUrl)
imagemPPM = converterImagem(imagem)
imagem = tk.PhotoImage(data=imagemPPM)

imgCanvas = canvas.create_image(300, 400,image=imagem)

menuBar = tk.Menu(tela)
tela.config(menu=menuBar)

fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Imagem', menu=fileMenu)
fileMenu.add_command(label='Imagem1', command=bosch)
fileMenu.add_command(label='Imagem2')
fileMenu.add_command(label='Imagem3')
fileMenu.add_command(label='Imagem4')


tela.mainloop()
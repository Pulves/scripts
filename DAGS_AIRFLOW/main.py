from PyPDF2 import PdfReader, PdfWriter
import os

diretorios = []


def dirs():
    pasta = './arquivos'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            diretorios.append(os.path.join(diretorio, arquivo))
dirs()

def files_temp(lista):

    for file in lista:
        print(file)
        reader = PdfReader(file)

        meta = reader.metadata

        print(len(reader.pages))

        # All of the following could be None!
        with open('temporario.pdf', 'w') as f:
            print(reader.getDocumentInfo())
            f.write(file)
            f.write("\nAutor: " + str(meta.author) + '\n')
            f.write("Creator: " + str(meta.creator) +'\n')
            f.write("Producer: " + str(meta.producer)+ '\n')
            f.write('Subject: ' + str(meta.subject)+ '\n')
            f.write('Title: ' + str(meta.title) + "\n")


files_temp(diretorios)


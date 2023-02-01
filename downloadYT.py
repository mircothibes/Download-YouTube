import PySimpleGUI as sg
from pytube import YouTube

def executar_download(link, path):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)

layout = [[sg.Text('Informe o link do video: '), sg.InputText()],
          [sg.Text('Informe o diretório para salvar: '), sg.InputText(), 
           sg.FolderBrowse()],
          [sg.Button('Download'), sg.Button('Cancelar')]
         ]

janela = sg.Window('Python Video Downloader', layout)

while True:
    event, values = janela.read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Download':
        executar_download(values[0], values[1])
        sg.popup_ok('Download is complete!')

janela.close()









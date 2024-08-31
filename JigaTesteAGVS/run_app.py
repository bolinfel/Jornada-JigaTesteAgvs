import subprocess
import webview
from threading import Thread
import time

def start_django():
    global server_process
    # Inicia o servidor Django usando subprocess
    server_process = subprocess.Popen(["python", "manage.py", "runserver"])
    server_process.wait()

def on_closed():
    # Função chamada quando a janela PyWebView é fechada
    print("Fechando o servidor Django...")
    server_process.terminate()  # Encerra o servidor Django
    server_process.wait()  # Aguarda o encerramento do processo

if __name__ == '__main__':
    # Inicia o servidor Django em uma thread separada
    django_thread = Thread(target=start_django)
    django_thread.start()

    # Aguarda alguns segundos para garantir que o servidor tenha iniciado
    time.sleep(2)

    # Cria a janela PyWebView
    window = webview.create_window('Main', 'http://127.0.0.1:8000')

    # Associa a função on_closed ao evento de fechamento da janela
    webview.start(on_closed)

import subprocess
import os
from wand.image import Image

# Função para instalar as dependências
def instalar_dependencias():
    subprocess.run(['sudo', 'apt-get', 'install', 'imagemagick', 'libmagickwand-dev', '-y'])
    subprocess.run(['sudo', 'pip', 'install', 'Wand'])

# Função para converter arquivos
def converter(arquivo_entrada, arquivo_saida):
    extensao_entrada = arquivo_entrada.split('.')[-1].lower()
    extensao_saida = arquivo_saida.split('.')[-1].lower()

    if extensao_entrada == 'pdf':
        with Image(filename=arquivo_entrada, resolution=300) as img:
            img.save(filename=arquivo_saida)
        print("Conversão de PDF para imagem concluída!")

    elif extensao_entrada in ('docx', 'doc'):
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', f"{os.path.dirname(arquivo_saida)}", arquivo_entrada])
        print("Conversão de DOCX/DOC para PDF concluída!")

    elif extensao_entrada == 'mp3':
        subprocess.run(['sudo', 'ffmpeg', '-i', arquivo_entrada, arquivo_saida])
        print("Conversão de MP3 para WAV concluída!")

    elif extensao_entrada in ('mp4', 'avi'):
        subprocess.run(['sudo', 'ffmpeg', '-i', arquivo_entrada, '-vf', 'fps=10,scale=320:-1:flags=lanczos', '-c:v', 'gif', arquivo_saida])
        print("Conversão de MP4/AVI para GIF concluída!")

    elif extensao_entrada in ('jpg', 'jpeg', 'png', 'gif'):
        subprocess.run(['sudo', 'convert', arquivo_entrada, arquivo_saida])
        print("Conversão de imagem para PDF concluída!")

    elif extensao_entrada == 'txt':
        subprocess.run(['sudo', 'cp', arquivo_entrada, arquivo_saida])
        print("Cópia do arquivo de texto concluída!")

    elif extensao_entrada == 'flac':
        subprocess.run(['sudo', 'ffmpeg', '-i', arquivo_entrada, arquivo_saida])
        print("Conversão de FLAC concluída!")

    # Adicione mais casos para outros tipos de arquivo conforme necessário

    else:
        print("Tipo de arquivo não suportado. Saindo.")

# Instala as dependências
instalar_dependencias()

# Exemplo de uso
arquivo_entrada = input("Digite o nome do arquivo de entrada (com extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com extensão): ")

converter(arquivo_entrada, arquivo_saida)

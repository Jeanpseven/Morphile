import subprocess
import os

def instalar_imagemagick():
    try:
        subprocess.run(['convert', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        subprocess.run(['sudo', 'apt-get', 'install', 'imagemagick'])

def converter(arquivo_entrada, arquivo_saida):
    extensao_entrada = arquivo_entrada.split('.')[-1].lower()
    extensao_saida = arquivo_saida.split('.')[-1].lower()

    instalar_imagemagick()  # Verifica e instala o ImageMagick se necessário

    if extensao_entrada in ('jpg', 'jpeg', 'png', 'gif'):
        subprocess.run(['convert', arquivo_entrada, arquivo_saida])
        print(f"Conversão de {extensao_entrada.upper()} para {extensao_saida.upper()} concluída!")

    # Adicione mais casos para outros tipos de arquivo conforme necessário

    else:
        print("Tipo de arquivo não suportado. Saindo.")

# Exemplo de uso
arquivo_entrada = input("Digite o nome do arquivo de entrada (com extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com extensão): ")

converter(arquivo_entrada, arquivo_saida)

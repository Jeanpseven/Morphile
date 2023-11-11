import subprocess

def instalar_dependencias():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'imagemagick'])
    subprocess.run(['sudo', 'apt', 'install', 'ffmpeg'])
    subprocess.run(['sudo', 'apt', 'install', 'pandoc'])

def converter(arquivo_entrada, arquivo_saida):
    extensao_entrada = arquivo_entrada.split('.')[-1].lower()
    extensao_saida = arquivo_saida.split('.')[-1].lower()

    if extensao_entrada == 'pdf':
        subprocess.run(['convert', '-density', '300', arquivo_entrada, '-quality', '100', arquivo_saida])
        print(f"Conversão de PDF para imagem concluída: {arquivo_saida}")

    elif extensao_entrada in ('docx', 'doc'):
        subprocess.run(['pandoc', arquivo_entrada, '-o', arquivo_saida])
        print(f"Conversão de DOCX/DOC para PDF concluída: {arquivo_saida}")

    elif extensao_entrada == 'mp3':
        subprocess.run(['ffmpeg', '-i', arquivo_entrada, arquivo_saida])
        print(f"Conversão de MP3 para WAV concluída: {arquivo_saida}")

    elif extensao_entrada in ('mp4', 'avi'):
        subprocess.run(['ffmpeg', '-i', arquivo_entrada, '-vf', 'fps=10,scale=320:-1:flags=lanczos', '-c:v', 'gif', arquivo_saida])
        print(f"Conversão de MP4/AVI para GIF concluída: {arquivo_saida}")

    elif extensao_entrada in ('jpg', 'jpeg', 'png', 'gif'):
        subprocess.run(['convert', arquivo_entrada, arquivo_saida])
        print(f"Conversão de imagem para PDF concluída: {arquivo_saida}")

    elif extensao_entrada == 'txt':
        subprocess.run(['cp', arquivo_entrada, arquivo_saida])
        print(f"Cópia do arquivo de texto concluída: {arquivo_saida}")

    elif extensao_entrada == 'flac':
        subprocess.run(['ffmpeg', '-i', arquivo_entrada, arquivo_saida])
        print(f"Conversão de FLAC concluída: {arquivo_saida}")

    # Adicione mais casos para outros tipos de arquivo conforme necessário

    else:
        print("Tipo de arquivo não suportado. Saindo.")

# Exemplo de uso
instalar_dependencias()
arquivo_entrada = input("Digite o nome do arquivo de entrada (com extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com extensão): ")

converter(arquivo_entrada, arquivo_saida)

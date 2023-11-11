import subprocess
import glob

# Função para instalar as dependências
def instalar_dependencias():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'imagemagick'])
    subprocess.run(['sudo', 'apt', 'install', 'libreoffice'])
    subprocess.run(['sudo', 'apt', 'install', 'ffmpeg'])

# Função para converter os arquivos
def converter(arquivo_entrada, arquivo_saida):
    # Verificar se as dependências estão instaladas
    try:
        subprocess.run(['convert', '--version'], check=True)
        subprocess.run(['libreoffice', '--version'], check=True)
        subprocess.run(['ffmpeg', '-version'], check=True)
    except subprocess.CalledProcessError:
        print("Instalando dependências...")
        instalar_dependencias()

    # Expandir curingas no arquivo de entrada
    arquivos_encontrados = glob.glob(arquivo_entrada)

    # Verificar se há arquivos encontrados
    if not arquivos_encontrados:
        print("Nenhum arquivo encontrado. Saindo.")
        return

    # Loop sobre os arquivos encontrados
    for arquivo in arquivos_encontrados:
        extensao_entrada = arquivo.split('.')[-1].lower()

        if extensao_entrada == 'pdf':
            subprocess.run(['convert', '-density', '300', arquivo, '-quality', '100', arquivo_saida])
            print(f"Conversão de PDF para imagem concluída para {arquivo}!")

        # Adicione mais casos conforme necessário
        else:
            print(f"Tipo de arquivo não suportado para {arquivo}. Ignorando.")

# Exemplo de uso
arquivo_entrada = input("Digite o padrão do nome do arquivo de entrada (com extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com extensão): ")

converter(arquivo_entrada, arquivo_saida)

import subprocess

def configurar_permissao():
    # Configuração automática das permissões para o ImageMagick
    magick_configure_path = "/etc/ImageMagick-6/policy.xml"
    subprocess.run(["sed", "-i", "s/<policymap>/$POLICY <policymap>/g", magick_configure_path])

def restaurar_permissao():
    # Restauração das permissões originais do ImageMagick
    magick_configure_path = "/etc/ImageMagick-6/policy.xml"
    subprocess.run(["sed", "-i", "s/$POLICY <policymap>/<policymap>/g", magick_configure_path])

def converter(arquivo_entrada, arquivo_saida):
    extensao_entrada = arquivo_entrada.split('.')[-1].lower()
    extensao_saida = arquivo_saida.split('.')[-1].lower()

    if extensao_entrada == 'pdf':
        subprocess.run(['convert', '-density', '300', arquivo_entrada, '-quality', '100', arquivo_saida])
        print("Conversão de PDF para imagem concluída!")

    elif extensao_entrada in ('jpg', 'jpeg', 'png', 'gif'):
        subprocess.run(['convert', arquivo_entrada, arquivo_saida])
        print("Conversão de imagem para JPG concluída!")

    # Adicione mais casos conforme necessário

    else:
        print(f"Tipo de arquivo não suportado: {extensao_entrada}. Saindo.")
        return

    restaurar_permissao()

# Exemplo de uso
configurar_permissao()
arquivo_entrada = input("Digite o nome do arquivo de entrada (com extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com extensão): ")

converter(arquivo_entrada, arquivo_saida)

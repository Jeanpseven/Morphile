import subprocess

def converter(arquivo_entrada, arquivo_saida):
    extensao_entrada = arquivo_entrada.split('.')[-1]
    extensao_saida = arquivo_saida.split('.')[-1]

    if extensao_entrada == 'pdf':
        subprocess.run(['convert', '-density', '300', arquivo_entrada, '-quality', '100', arquivo_saida])
        print("Conversão de PDF para imagem concluída!")

    # Adicione mais casos para outros tipos de arquivo conforme necessário

    else:
        print("Tipo de arquivo não suportado. Saindo.")

# Exemplo de uso
arquivo_entrada = input("Digite o nome do arquivo de entrada (com extensão): ")
arquivo_saida = input("Digite o nome do arquivo de saída (com extensão): ")

converter(arquivo_entrada, arquivo_saida)

#!/bin/bash

# Ajuste de permissões temporárias
POLICY="PDF"
MAGICK_CONFIGURE_PATH="/etc/ImageMagick-6/policy.xml"
sed -i "s/$POLICY none/$POLICY read|write/g" $MAGICK_CONFIGURE_PATH

# Função para converter os arquivos
converter() {
    arquivo_entrada=$1
    arquivo_saida=$2

    extensao_entrada="${arquivo_entrada##*.}"
    extensao_saida="${arquivo_saida##*.}"

    case "$extensao_entrada" in
        pdf)
            convert -density 300 "$arquivo_entrada" -quality 100 "$arquivo_saida"
            echo "Conversão de PDF para imagem concluída!"
            ;;
        jpg|jpeg|png|gif)
            convert "$arquivo_entrada" "$arquivo_saida"
            echo "Conversão de imagem para JPG concluída!"
            ;;
        # Adicione mais casos conforme necessário

        *)
            echo "Tipo de arquivo não suportado. Saindo."
            exit 1
            ;;
    esac
}

# Exemplo de uso
read -p "Digite o nome do arquivo de entrada (com extensão): " arquivo_entrada
read -p "Digite o nome do arquivo de saída (com extensão): " arquivo_saida

converter "$arquivo_entrada" "$arquivo_saida"

# Ajuste de permissões de volta ao normal
sed -i "s/$POLICY read|write/$POLICY none/g" $MAGICK_CONFIGURE_PATH

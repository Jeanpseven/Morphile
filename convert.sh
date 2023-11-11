#!/bin/bash

echo "Bem-vindo ao Script de Conversão!"
read -p "Digite o caminho completo do arquivo de entrada: " caminho_entrada
read -p "Digite o caminho completo ou apenas o nome com extensão do arquivo de saída: " caminho_saida

# Extrai o tipo de entrada e saída
tipo_entrada="${caminho_entrada##*.}"
tipo_saida="${caminho_saida##*.}"

# Se o caminho de saída não contiver '/', então adiciona o diretório atual
if [[ ! "$caminho_saida" =~ '/' ]]; then
    caminho_saida="./$caminho_saida"
fi

# Verifica se o arquivo de entrada existe
if [ ! -f "$caminho_entrada" ]; then
    echo "Erro: Arquivo de entrada não encontrado."
    exit 1
fi

# Criação do diretório de saída se não existir
mkdir -p "$(dirname "$caminho_saida")"

case "$tipo_entrada" in
    pdf)
        convert -density 300 "$caminho_entrada" -quality 100 "$caminho_saida"
        echo "Conversão de PDF para imagem concluída!"
        ;;
    docx|doc)
        libreoffice --headless --convert-to pdf --outdir "$(dirname "$caminho_saida")" "$caminho_entrada"
        echo "Conversão de DOCX/DOC para PDF concluída!"
        ;;
    mp3)
        ffmpeg -i "$caminho_entrada" "$caminho_saida"
        echo "Conversão de MP3 para WAV concluída!"
        ;;
    mp4|avi)
        ffmpeg -i "$caminho_entrada" -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif "$caminho_saida"
        echo "Conversão de MP4/AVI para GIF concluída!"
        ;;
    jpg|jpeg|png|gif)
        # Adiciona a extensão correta na saída, caso não tenha sido fornecida
        if [[ ! "$caminho_saida" =~ \. ]]; then
            caminho_saida="$caminho_saida.jpg"
        fi
        convert "$caminho_entrada" "$caminho_saida"
        echo "Conversão de imagem para JPG concluída!"
        ;;
    txt)
        cp "$caminho_entrada" "$caminho_saida"
        echo "Cópia do arquivo de texto concluída!"
        ;;
    flac)
        ffmpeg -i "$caminho_entrada" -c:a flac "$caminho_saida"
        echo "Conversão para FLAC concluída!"
        ;;
    folder)
        read -p "Digite o caminho da pasta contendo imagens: " pasta_entrada
        read -p "Digite a duração de cada imagem em segundos: " duracao
        read -p "Digite o caminho completo do arquivo de saída (com extensão): " arquivo_saida

        if [ ! -d "$pasta_entrada" ]; then
            echo "Erro: Pasta de entrada não encontrada."
            exit 1
        fi

        if [ -z "$arquivo_saida" ]; then
            echo "Erro: Caminho de saída inválido."
            exit 1
        fi

        ffmpeg -framerate 1/"$duracao" -pattern_type glob -i "$pasta_entrada/*.png" -c:v libx264 -r 30 "$arquivo_saida"
        echo "Conversão de imagens para vídeo concluída!"
        ;;
    *)
        echo "Tipo de arquivo não suportado. Saindo."
        exit 1
        ;;
esac

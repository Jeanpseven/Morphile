#!/bin/bash

echo "Bem-vindo ao Script de Conversão!"
read -p "Digite o nome do arquivo de entrada (com extensão): " arquivo_entrada
read -p "Digite o nome do arquivo de saída (com extensão): " arquivo_saida

extensao_entrada=$(echo "$arquivo_entrada" | awk -F'.' '{print tolower($NF)}')
extensao_saida=$(echo "$arquivo_saida" | awk -F'.' '{print tolower($NF)}')

case "$extensao_entrada" in
    pdf)
        convert -density 300 "$arquivo_entrada" -quality 100 "$arquivo_saida"
        echo "Conversão de PDF para imagem concluída!"
        ;;
    docx|doc)
        libreoffice --headless --convert-to pdf --outdir $(dirname "$arquivo_saida") "$arquivo_entrada"
        echo "Conversão de DOCX/DOC para PDF concluída!"
        ;;
    mp3)
        ffmpeg -i "$arquivo_entrada" "$arquivo_saida"
        echo "Conversão de MP3 para WAV concluída!"
        ;;
    mp4|avi)
        ffmpeg -i "$arquivo_entrada" -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif "$arquivo_saida"
        echo "Conversão de MP4/AVI para GIF concluída!"
        ;;
    jpg|jpeg|png|gif)
        convert "$arquivo_entrada" "$arquivo_saida"
        echo "Conversão de imagem para PDF concluída!"
        ;;
    txt)
        cp "$arquivo_entrada" "$arquivo_saida"
        echo "Cópia do arquivo de texto concluída!"
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
    flac)
        ffmpeg -i "$arquivo_entrada" "$arquivo_saida"
        echo "Conversão de FLAC concluída!"
        ;;
    *)
        echo "Tipo de arquivo não suportado. Saindo."
        exit 1
        ;;
esac

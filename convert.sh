#!/bin/bash

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
            echo "Conversão de imagem concluída!"
            ;;
        txt)
            cp "$arquivo_entrada" "$arquivo_saida"
            echo "Cópia do arquivo de texto concluída!"
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
}

# Exemplo de uso
read -p "Digite o nome do arquivo de entrada (com extensão): " arquivo_entrada
read -p "Digite o nome do arquivo de saída (com extensão): " arquivo_saida

converter "$arquivo_entrada" "$arquivo_saida"

#!/bin/bash

echo "Bem-vindo ao Script de Conversão!"
read -p "Digite o caminho do arquivo de entrada: " input_path
read -p "Digite o caminho do arquivo de saída: " output_path

# Remover as aspas simples dos caminhos, se presentes
input_path="${input_path/'/'/}"
output_path="${output_path/'/'/}"

filename=$(basename -- "$input_path")
extension="${filename##*.}"

case "$extension" in
    pdf)
        convert -density 300 "$input_path" -quality 100 "$output_path"
        echo "Conversão de PDF para imagem concluída!"
        ;;
    docx|doc)
        libreoffice --headless --convert-to pdf --outdir $(dirname "$output_path") "$input_path"
        echo "Conversão de DOCX/DOC para PDF concluída!"
        ;;
    mp3)
        ffmpeg -i "$input_path" "$output_path"
        echo "Conversão de MP3 para WAV concluída!"
        ;;
    mp4|avi)
        ffmpeg -i "$input_path" -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif "$output_path"
        echo "Conversão de MP4/AVI para GIF concluída!"
        ;;
    jpg|jpeg|png|gif)
        convert "$input_path" "$output_path"
        echo "Conversão de imagem para JPG concluída!"
        ;;
    txt)
        cp "$input_path" "$output_path"
        echo "Cópia do arquivo de texto concluída!"
        ;;
    flac)
        # Lógica específica para conversão de FLAC
        # Adicione sua lógica aqui
        ;;
    *)
        echo "Tipo de arquivo não suportado. Saindo."
        exit 1
        ;;
esac

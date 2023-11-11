#!/bin/bash

echo "Bem-vindo ao Script de Conversão!"
read -p "Digite o caminho do arquivo de entrada (com extensão): " input_path
read -p "Digite o caminho do arquivo de saída (com extensão ou nome se for salvar no repo local): " output_path

# Remover aspas, se presentes
input_path="${input_path//\"/}"
input_path="${input_path//\'/}"
output_path="${output_path//\"/}"
output_path="${output_path//\'/}"

# Verificar se a saída é um diretório
if [ -d "$output_path" ]; then
    output_path="$output_path/$(basename "$input_path")"
fi

extension="${input_path##*.}"

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
        echo "Conversão de imagem para PDF concluída!"
        ;;
    txt)
        cp "$input_path" "$output_path"
        echo "Cópia do arquivo de texto concluída!"
        ;;
    flac)
        ffmpeg -i "$input_path" -c:a flac "$output_path"
        echo "Conversão de FLAC concluída!"
        ;;
    folder)
        read -p "Digite o caminho da pasta contendo imagens: " folder_path
        read -p "Digite a duração de cada imagem em segundos: " duration
        read -p "Digite o caminho completo do arquivo de saída (com extensão): " output_path_folder

        if [ ! -d "$folder_path" ]; then
            echo "Erro: Pasta de entrada não encontrada."
            exit 1
        fi

        if [ -z "$output_path_folder" ]; then
            echo "Erro: Caminho de saída inválido."
            exit 1
        fi

        ffmpeg -framerate 1/"$duration" -pattern_type glob -i "$folder_path/*.png" -c:v libx264 -r 30 "$output_path_folder"
        echo "Conversão de imagens para vídeo concluída!"
        ;;
    *)
        echo "Tipo de arquivo não suportado. Saindo."
        exit 1
        ;;
esac

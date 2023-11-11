import os

def pdf_to_image(input_file, output_file):
    # Lógica para converter PDF para imagem usando imagemagick
    os.system(f"convert -density 300 {input_file} -quality 100 {output_file}")
    print(f"Conversão de PDF para imagem concluída: {input_file} -> {output_file}")

def doc_to_pdf(input_file, output_file):
    # Lógica para converter DOCX/DOC para PDF usando LibreOffice
    os.system(f"libreoffice --headless --convert-to pdf --outdir $(dirname {output_file}) {input_file}")
    print(f"Conversão de DOCX/DOC para PDF concluída: {input_file} -> {output_file}")

def mp3_to_wav(input_file, output_file):
    # Lógica para converter MP3 para WAV usando ffmpeg
    os.system(f"ffmpeg -i {input_file} {output_file}")
    print(f"Conversão de MP3 para WAV concluída: {input_file} -> {output_file}")

def mp4_to_gif(input_file, output_file):
    # Lógica para converter MP4/AVI para GIF usando ffmpeg
    os.system(f"ffmpeg -i {input_file} -vf 'fps=10,scale=320:-1:flags=lanczos' -c:v gif {output_file}")
    print(f"Conversão de MP4/AVI para GIF concluída: {input_file} -> {output_file}")

def image_to_pdf(input_file, output_file):
    # Lógica para converter imagem para PDF usando imagemagick
    os.system(f"convert {input_file} {output_file}")
    print(f"Conversão de imagem para PDF concluída: {input_file} -> {output_file}")

def copy_text_file(input_file, output_file):
    # Lógica para copiar arquivo de texto
    os.system(f"cp {input_file} {output_file}")
    print(f"Cópia do arquivo de texto concluída: {input_file} -> {output_file}")

def convert_images_to_video(image_folder, output_file, duration):
    # Lógica para converter imagens para vídeo usando ffmpeg
    os.system(f"ffmpeg -framerate 1/{duration} -pattern_type glob -i {image_folder}/*.png -c:v libx264 -r 30 {output_file}")
    print(f"Conversão de imagens para vídeo concluída: {image_folder} -> {output_file}")

def main():
    print("Bem-vindo ao Script de Conversão!")

    input_file = input("Digite o nome do arquivo de entrada (com extensão): ")
    output_file = input("Digite o nome do arquivo de saída (com extensão): ")

    extensao_entrada = input_file.split('.')[-1]

    if extensao_entrada == "pdf":
        pdf_to_image(input_file, output_file)
    elif extensao_entrada in ["docx", "doc"]:
        doc_to_pdf(input_file, output_file)
    elif extensao_entrada == "mp3":
        mp3_to_wav(input_file, output_file)
    elif extensao_entrada in ["mp4", "avi"]:
        mp4_to_gif(input_file, output_file)
    elif extensao_entrada in ["jpg", "jpeg", "png", "gif"]:
        image_to_pdf(input_file, output_file)
    elif extensao_entrada == "txt":
        copy_text_file(input_file, output_file)
    elif extensao_entrada == "folder":
        image_folder = input("Digite o caminho da pasta contendo imagens: ")
        duration = input("Digite a duração de cada imagem em segundos: ")
        convert_images_to_video(image_folder, output_file, duration)
    else:
        print("Tipo de arquivo não suportado. Saindo.")

if __name__ == "__main__":
    main()

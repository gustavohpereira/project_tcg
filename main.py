import os
import glob
from classes.Card_image import CardImage
from classes.OCRProcessor import OCRProcessor

def process_images_in_directory(directory_path):
    image_extensions = ['*.png', '*.jpg', '*.jpeg','*.webp']
    images = []

    for ext in image_extensions:
        images.extend(glob.glob(os.path.join(directory_path, ext)))


    ocr = OCRProcessor()

    for image_path in images:
        print(f"Processando imagem: {image_path}")
        
        # Cria o objeto CardImage com a imagem
        card = CardImage(image_path)

        # Realiza o corte das imagens
        title_crop = card.crop_title()
        code_crop = card.crop_code()

        # Processa as imagens com OCR
        title_text = ocr.extract_text(title_crop)
        code_text = ocr.extract_text(code_crop)

        # Obtém o título e o código
        title = ocr.get_title(title_text)
        code = ocr.get_code(code_text)

        # Exibe os resultados
        print("Título detectado:", title)
        print("Código detectado:", code)


def main(directory_path):
    process_images_in_directory(directory_path)

# Caminho para a pasta com as imagens
if __name__ == "__main__":
    directory_path = './cardImages'  # Altere para o caminho correto
    main(directory_path)

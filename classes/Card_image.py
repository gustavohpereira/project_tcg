import cv2
import matplotlib.pyplot as plt

class CardImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        # Converte para escala de cinza
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def crop_title(self):
        """Corta a parte superior da imagem para o título."""
        height, width = self.gray_image.shape[:2]
        return self.gray_image[0:int(height * 0.2), 0:width]

    def crop_code(self):
        """Corta a parte inferior esquerda da imagem para o código."""
        height, width = self.gray_image.shape[:2]
        return self.gray_image[int(height * 0.9):height, 0:int(width * 0.5)]

    def show_images(self, title_crop, code_crop):
        """Exibe as imagens cortadas de título e código."""
        plt.figure(figsize=(10, 5))

        # Exibir o título
        plt.subplot(1, 2, 1)
        plt.imshow(title_crop, cmap='gray')
        plt.title("Título")
        plt.axis("off")

        # Exibir o código
        plt.subplot(1, 2, 2)
        plt.imshow(code_crop, cmap='gray')
        plt.title("Código")
        plt.axis("off")

        plt.show()

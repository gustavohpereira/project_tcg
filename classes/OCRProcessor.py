import easyocr
import re

class OCRProcessor:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image):
        """Extrai texto da imagem usando EasyOCR."""
        return self.reader.readtext(image, detail=0)


    def treatEX(self, text):
        if text[-2:].lower() == "ex":
            return text[:-2].strip() + " " + text[-2:].lower()
        else:
            return text

    def get_title(self, title_text):
        """Obtém o segundo item (título) do texto detectado."""
        if len(title_text) > 1:
            treated_ex = self.treatEX(title_text[1])
            return treated_ex
        return title_text[0] if title_text else ""

    def get_code(self, code_text):

        print(code_text)

        """Extrai o código com o formato xxx/xxx usando regex."""
        code_string = " ".join(code_text)

        match = re.search(r'\d{3}/\d{3}', code_string)
        if match:
            return match.group(0)
        return ""

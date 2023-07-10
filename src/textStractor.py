import cv2
import pytesseract


def extrair_numero_imagem(caminho_imagem):
    # Carrega a imagem usando o OpenCV
    imagem = cv2.imread(caminho_imagem)
    
    # Redimensiona a imagem para aumentar a resolução
    largura = imagem.shape[1] * 3
    altura = imagem.shape[0] * 3
    imagem_redimensionada = cv2.resize(imagem, (largura, altura))
    
    # Converte a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)
    
    # Aplica o OCR usando o Tesseract
    numero = pytesseract.image_to_string(imagem_cinza, config='--psm 6')
    
    # Retorna o número extraído
    return numero



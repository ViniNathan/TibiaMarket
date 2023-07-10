from PIL import Image, ImageChops

def compare_images(image1_path, image2_path):
    # Abrir as imagens
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Calcular a diferença entre as imagens
    diff = ImageChops.difference(image1, image2)

    # Verificar se as imagens são iguais
    if diff.getbbox() is None:
        return True  # As imagens são idênticas
    else:
        return False  # As imagens são diferentes

# # Exemplo de uso
# image1_path = "images/depotImages/blankTemplate.png"
# image2_path = "images/itemsPhoto/itemPhoto.png"

# are_equal = compare_images(image1_path, image2_path)
# if are_equal:
#     print("As imagens são iguais.")
# else:
#     print("As imagens são diferentes.")
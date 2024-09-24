import os
import shutil
from PIL import Image


def saveFiles(files, filesFolder):
    uploads_dir = os.path.join(filesFolder)
    os.makedirs(uploads_dir, exist_ok=True)

    for emphasisFile in files:
        name = emphasisFile['name']
        file = emphasisFile['file']

        # Abre a imagem usando Pillow
        with Image.open(file) as img:
            # Converte a imagem para RGB (para garantir que funcione com JPG)
            rgb_image = img.convert('RGB')

            # Define o caminho para salvar a imagem como JPG
            jpg_filename = f"{name}.jpg"
            rgb_image.save(os.path.join(uploads_dir, jpg_filename), format='JPEG')


def removeFiles(filesFolder):
    uploads_dir = os.path.join(filesFolder)
    shutil.rmtree(uploads_dir)

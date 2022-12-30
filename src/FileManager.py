import os

class FileManager:
  # Devuelve una lista con los nombres de las fotos del directorio /img
  def get_photos_name(self):
    photos_name = []
    for file in os.listdir(os.getcwd() + "\\img\\"):
      photos_name.append(file)
    return photos_name
  def remove_photos(self, photos_name):
    for photo in photos_name:
      os.remove(os.getcwd() + "\\img\\" + photo)
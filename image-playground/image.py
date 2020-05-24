from PIL import Image, ImageFilter
from pathlib import Path 

images_folder = Path("d:\\OneDrive - SQLI\\Perso\\Code\\python\\image-playground\\Pokedex\\")
image_to_open = images_folder / "pikachu.jpg"

img = Image.open(image_to_open)
print(img)
print(img.format)
print(img.size)
print(img.mode)
#print(dir(img)) 

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png","png")

rotated_image = img.rotate(90)
rotated_image.save("rotaded.png","png")
#filtered_image.show()

converted_image = img.convert('L')
converted_image.save("grey.png","png")

resized_image = img.resize((300,300))
resized_image.save("resized.png","png")

resized_image = img.resize((300,300))
resized_image.save("resized.png","png")

box = (100,100,400,400)
cropped_image = img.crop(box)
cropped_image.save("cropped.png","png")




import sys
import os
from PIL import Image
from pathlib import Path

def readParametersFromConsole (list):
    parameters = []
    for param in list:
        parameters.append(param)
    return parameters



# with sys grab first and second argument
source_folder = ''
destanation_folder = ''
parameters = readParametersFromConsole(sys.argv)

current_folder = Path("d:\\OneDrive - SQLI\\Perso\\Code\\python\\image-playground\\")

if len(parameters) == 3:
    print("We have enough information to work")
    source_folder = parameters[1]
    destination_folder = parameters[2]
    #print(f"source: {source_folder} destination: {destination_folder}")

    # check if second parameter exist if not creat it
    print ("source exists: "+str(os.path.exists(source_folder)))
    print ("destination exists: "+str(os.path.exists(destination_folder)))

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # look through the folder and onvert images to PNG

    for file_name in os.listdir(source_folder):
       
        image = Image.open(f'{source_folder}{file_name}')
        print(f'working with; {file_name} Data:{image}')
        clean_name= os.path.splitext(file_name)[0]
        # save them to the new folder
        print(destanation_folder)
        image.save(f'{destination_folder}{clean_name}.png','png')
    print('All done!')
else:
    print("You have to provide at least 2 parameters")









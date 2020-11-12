import os
import glob
import argparse

from zipfile import ZipFile, ZipInfo

#Parse Arguments
parser = argparse.ArgumentParser(description="Automatizare pentru export fotografii Canva")
parser.add_argument('--source', default="C:/vsphotos", help="Path-ul catre directorul cu fisierele .zip / .rar (necesar)")
parser.add_argument('--dest', default="", help="Numele folderului destinatie (optional)")
args = parser.parse_args()

#Source path
SOURCE_FOLDER_PATH = args.source

#Destination name and path (default at ./proccessed)
DESTINATION_FOLDER_NAME = "proccessed"
DESTINATION_FOLDER_PATH = SOURCE_FOLDER_PATH + '/' + DESTINATION_FOLDER_NAME

def proccess(dir_path):
    #Creates appdata dir if it doesen't exist
    tempdir = os.path.join(SOURCE_FOLDER_PATH, 'temp')
    print(tempdir + '\n')
    if not os.path.exists(tempdir):
        os.mkdir(tempdir)

    #Change dir to SOURCE_PATH_FOLDER
    os.chdir(dir_path)
    #Create dest dir if it doesen't exist
    if not os.path.exists(DESTINATION_FOLDER_PATH):
        os.makedirs(DESTINATION_FOLDER_NAME)

    #Foreach zip file unpack it in the dest dir
    for file in glob.glob("*.zip"):
        print(f"Found file {file}")
        print("-------------------")

        with ZipFile(file, 'r') as zip:
            zip.extractall(os.path.join(tempdir, file))

        for photo in os.listdir(os.path.join(tempdir, file)):
            print(photo)

        print("\n")


proccess(SOURCE_FOLDER_PATH)
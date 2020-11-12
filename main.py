import argparse

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
    print(dir_path)

proccess(SOURCE_FOLDER_PATH)
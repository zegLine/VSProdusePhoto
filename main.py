import os
import glob
import argparse
import shutil

from zipfile import ZipFile

#Parse Arguments
parser = argparse.ArgumentParser(description="Automatizare pentru export fotografii Canva")
parser.add_argument('--source', default="C:/vsphotos", help="Path-ul catre directorul cu fisierele .zip / .rar (necesar)")
parser.add_argument('--dest', default="proccessed", help="Numele folderului destinatie (optional)")
parser.add_argument('--use-appdata-temp', dest="use_appdata", action="store_true")
parser.add_argument('--use-local-temp', dest="use_appdata", action="store_false")
parser.set_defaults(use_appdata=True)
args = parser.parse_args()

#Source path
SOURCE_FOLDER_PATH = args.source

#Destination name and path (default at ./proccessed)
DESTINATION_FOLDER_NAME = args.dest
DESTINATION_FOLDER_PATH = SOURCE_FOLDER_PATH + '/' + DESTINATION_FOLDER_NAME

def proccess(dir_path):
    #Creates temp dir if it doesen't exist
    if args.use_appdata:
        tempdir = os.path.join(os.getenv("LOCALAPPDATA"), "VSProdusePhoto")
    else:
        tempdir = os.path.join(SOURCE_FOLDER_PATH, 'temp')

    print(f'Working with temp dir {tempdir} \n')
    if not os.path.exists(tempdir):
        os.mkdir(tempdir)

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    #Change dir to SOURCE_PATH_FOLDER
    os.chdir(dir_path)
    #Create dest dir if it doesen't exist
    if not os.path.exists(DESTINATION_FOLDER_PATH):
        os.makedirs(DESTINATION_FOLDER_NAME)

    #Foreach zip file unpack it in the dest dir
    for file in glob.glob("*.zip"):
        print(f"Found file {file}")
        print("-------------------")

        filetempdir = os.path.join(tempdir, file)

        with ZipFile(file, 'r') as zip:
            zip.extractall(filetempdir)

        for photo in os.listdir(filetempdir):
            photopath = os.path.join(filetempdir, photo)

            filefinalname = f'{file[:-4]} ({photo[:-4]}).{photo[-3:]}'
            filefinalpath = os.path.join(DESTINATION_FOLDER_PATH, filefinalname)


            try:
                shutil.copy(photopath, filefinalpath)
                print(f"Renamed and moved {photopath} to {filefinalpath}")
            except:
                print(f"There has been an error while trying to copy file {photo}")


        print("\n")


proccess(SOURCE_FOLDER_PATH)
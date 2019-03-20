import wget
import zipfile


def extract(file, target):
    z = zipfile.ZipFile(file, 'r')
    z.extractall(target)
    z.close()


FILE_URL = 'http://download.geonames.org/export/zip/US.zip'
FILE_ZIP = 'us.zip'
DATA_PATH = 'data'
wget.download(FILE_URL, FILE_ZIP)
extract(FILE_ZIP, DATA_PATH)

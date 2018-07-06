import argparse
import os


def tileTiff(tiff_file, directory_name):

    command0 = "mkdir " + directory_name
    command1 = "gdal_retile.py -v -r bilinear -ps 2048 2048 -co TILED=YES -co COMPRESS=JPEG -targetDir image_tiles " + tiff_file

    os.system(command0)
    os.system(command1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('tiff')
    parser.add_argument('directory')

    args = parser.parse_args()

    tiff = args.tiff
    directory = args.directory

    tileTiff(tiff, directory)


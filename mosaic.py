
import glob
import os
import argparse

def gdalmergeMosaic(directory_name):
    file_list = glob.glob(directory_name + "/*.tif")
    files_string = " ".join(file_list)

    #command = "gdal_merge.py --config CHECK_DISK_FREE_SPACE NO -o mosaic.tif -of gtiff " + files_string
    #command = "gdal_merge.py -co COMPRESS=LZW -co PREDICTOR=2 -co TILED=YES -co BIGTIFF=YES -o mosaic.tif -of gtiff " + files_string
    #command0 = "gdalbuildvrt mosaic.vrt " + files_string
    #command1 = "gdal_translate -of GTiff -co COMPRESS=JPEG -co TILED=YES -co BIGTIFF=YES mosaic.vrt mosaic.tif"

    command0 = "echo " + files_string + " > list.txt"
    command1 = "gdalwarp --config GDAL_CACHEMAX 95% -multi -overwrite -wm 200000 -r max -srcnodata None -dstnodata None -wo BIGTIFF=YES --optfile list.txt  mosaic.tif"

    os.system(command0)
    os.system(command1)

if __name__ == "__main__":


    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    args = parser.parse_args()

    directory_name = args.directory

    gdalmergeMosaic(directory_name)

import os
import argparse


def compressTIF(original_tif, compression_method="JPEG", predictors=2, new_directory="compressed/"):
    '''
    This function takes an uncompressed GeoTIFF and compresses it with one of four compression methods: Packbits,
    JPEG, Deflate, or LZW. For LZW and Deflate, you can choose the number of predictors.
    :param original_tif: The uncompressed GeoTIFF to be compressed
    :param new_tif: The new compressed GeoTIFF
    :param compression_method: Packbits, JPEG, Deflate, or LZW
    :param predictors: Default is 2
    :return: Creates a new compressed TIF in directory folder
    '''

    if os.path.exists(new_directory) is False:
        os.mkdir(new_directory)
    else:
        pass

    new_tif_base = original_tif.split('.')[0]
    packbit_base = "_packbit_compressed.tif"
    jpeg_base = "_jpeg_compressed.tif"
    deflate_base = "_deflate_compressed.tif"
    lzw_base = "_lzw_compressed.tif"


    command_packbits = "gdal_translate -of GTiff -co COMPRESS=PACKBITS -co TILED=YES " + original_tif + " " + new_tif_base + packbit_base
    command_jpeg = "gdal_translate -co COMPRESS=JPEG -co TILED=YES " + original_tif + " " + new_tif_base + jpeg_base
    command_deflate = "gdal_translate -of GTiff -co COMPRESS=DEFLATE -co PREDICTOR=" + str(predictors) + " -co TILED=YES " + original_tif + " " + new_tif_base + deflate_base
    command_lzw = "gdal_translate -of GTiff -co COMPRESS=LZW -co PREDICTOR=" + str(predictors) + " -co TILED=YES " + original_tif + " " + new_tif_base + lzw_base

    command_mv = "mv " + new_tif_base

    if compression_method == "JPEG":
        os.system(command_jpeg)
        os.system(command_mv + jpeg_base + " " + new_directory)
    elif compression_method == "Packbits":
        os.system(command_packbits)
        os.system(command_mv + packbit_base + " " + new_directory)
    elif compression_method == "Deflate":
        os.system(command_deflate)
        os.system(command_mv + deflate_base + " " + new_directory)
    elif compression_method == "LZW":
        os.system(command_lzw)
        os.system(command_mv + lzw_base + " " + new_directory)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in the file you want to compress.')
    parser.add_argument('file', help='Tif file you want to compress')
    parser.add_argument('method', default='JPEG')
    parser.add_argument('predictors', default=2)
    args = parser.parse_args()

    tif_file = args.file
    compression_method = args.method
    predictors = args.predictors

    compressTIF(tif_file, compression_method, predictors)

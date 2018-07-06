# get coordinate ranges of catalog ids and tiffs
import gdal
import os
import csv

def get_range_tif(tif):
    print(tif)
    ds = gdal.Open(tif)
    width = ds.RasterXSize
    height = ds.RasterYSize
    gt = ds.GetGeoTransform()
    minx = gt[0]
    miny = gt[3] + width*gt[4] + height*gt[5]
    # from http://gdal.org/gdal_datamodel.html
    maxx = gt[0] + width*gt[1] + height*gt[2]
    # from http://gdal.org/gdal_datamodel.html
    maxy = gt[3]
    range = ((minx, miny), (maxx, maxy))
    return range

# Will loop through tifs found in the folders and append the csv file with the folder, file, min, and max values
with open('tifRange-tiles-run-1.csv', 'w') as myFile:
    writer = csv.writer(myFile)
    for file in os.listdir('image_tiles/'):
        if file.endswith('.tif'):
            try:
                temp = [file]
                minmax = get_range_tif('image_tiles/' + file)
                temp.append(minmax[0])
                temp.append(minmax[1])
                writer.writerow(temp)
            except Exception:
                print (file + ' failed')
                pass

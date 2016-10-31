#!/usr/bin/python
#coding: utf-8

import pyexiv2
import sys
#import glob
#import getopt
from shutil import copyfile
import os

def main(argv):
    JPG('.jpg')
    JPG('.JPG')
    JPG('.Jpg')
    JPG('.JPg')
    JPG('.jPg')
    JPG('.jpeg')
    JPG('.JPEG')
    JPG('.Jpeg')


def JPG(endung):
    # for inputfile in glob.glob(endung):
    for root, dirs, files in os.walk('.'):
        for inputfile in files:
            if inputfile.endswith(endung):
                path = os.path.join(root, inputfile)
                ifile = os.path.basename(inputfile)
                try:
                    metadata = pyexiv2.ImageMetadata(path)
                    metadata.read()
                    metadata.exif_keys
                except:
                    exif_dat='NONE'
                try:
                    tag = metadata['Exif.Image.DateTime']
                    exif_dat = tag.raw_value
                    date, time = exif_dat.split()
                    date = date.replace(":", "-")
                    time = time.replace(":", "-")
                    filename = date + '_' + time + '_' + ifile
                    print ('EXIF: ' + ifile + ' -> ' + filename)
                except:
                    exif_dat = 'None None'

                # Jolla-EXIF-bugaround by date in filename!
                if exif_dat == ('None None'):
                    try:
                        tag = metadata['Exif.Image.Model']
                        exif_dat = tag.raw_value
                        if exif_dat == ('Jolla'):
                            year = inputfile[0:4]
                            month = inputfile[4:6]
                            day = inputfile[6:8]
                            time = inputfile[9:12]
                            time = ('0' + time)
                            exif_dat = (year + '-' + month + '-' + day + ' ' + time)
                            filedat = exif_dat.replace(' ', '_')
                            print ('Jolla: ' + inputfile + '->' + filedat + '_' + inputfile)
                        else:
                            exif_dat = 'None None'
                    except:
                        exif_dat = 'None None'

                date, time = exif_dat.split()
                date = date.replace(":", "-")
                time = time.replace(":", "-")
                filename = date + '_' + time + '_' + ifile
                if date == 'None':
                    if not os.path.exists('UNSORTIERT'):
                        os.mkdir('UNSORTIERT')
                    if path == ('./UNSORTIERT/' + ifile):
                         print('./UNSORTIERT/' + ifile + ' gibt es schon!')
                    else:
                         copyfile(path, 'UNSORTIERT/' + ifile)
                    print ('UNSORTIERT (Kein EXIF, kein Jolla): ' + ifile)
                else:
                    jahr = date[0:4]
                    monat = date[5:7]
                    if not os.path.exists('SORTIERT'):
                        os.mkdir('SORTIERT')
                    if not os.path.exists('SORTIERT/' + jahr):
                        os.mkdir('SORTIERT/' + jahr)
                    if not os.path.exists('SORTIERT/' + jahr + '/' + monat):
                        os.mkdir('SORTIERT/' + jahr + '/' + monat)
                    dpfad  = ('SORTIERT/' + jahr + '/' + monat + '/' + filename)
                    if path == dpfad:
                        print('SORTIERT/' + jahr + '/' + monat + '/' + filename + ' gibt es schon!')
                    elif path == ('./SORTIERT/' + jahr + '/' + monat + '/' + ifile):
                        print('./SORTIERT/' + jahr + '/' + monat + '/' + ifile + ' wurde anscheinend schon sortiert.')
                        
                    else: 
                        copyfile(path, 'SORTIERT/' + jahr + '/' + monat + '/' + filename)


if __name__ == "__main__":
    main(sys.argv[1:])

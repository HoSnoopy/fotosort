#!/usr/bin/python

import pyexiv2
import sys
import glob
import os
import getopt
from shutil import copyfile

def main(argv):
 JPG('*.jpg')
 JPG('*.JPG')
 JPG('*.Jpg')
 JPG('*.JPg')
 JPG('*.jPg')
 JPG('*.jpeg')
 JPG('*.JPEG')
 JPG('*.Jpeg')

def JPG(endung):
 for inputfile in glob.glob(endung):
   ifile = os.path.basename(inputfile)
   metadata = pyexiv2.ImageMetadata(inputfile)
   metadata.read()
   metadata.exif_keys
   try: 
      tag = metadata['Exif.Image.DateTime']
      exif_dat=tag.raw_value
   except:
      exif_dat = 'None None'
   date, time = exif_dat.split()
   date = date.replace(":", "-")
   time = time.replace(":", "-")
   filename = date + '_' + time + '_' + ifile
   if date == 'None':
      if not os.path.exists('UNSORTIERT'):
         os.mkdir('UNSORTIERT')
      copyfile(inputfile, 'UNSORTIERT/'+ifile)
   else: 
      monat=date[0:7]    
      if not os.path.exists('SORTIERT'):
         os.mkdir('SORTIERT')
      if not os.path.exists('SORTIERT/'+monat):
         os.mkdir('SORTIERT/'+monat)
      copyfile(inputfile, 'SORTIERT/'+monat+'/'+filename)

if __name__ == "__main__":
   main(sys.argv[1:])


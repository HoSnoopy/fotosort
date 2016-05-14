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
      date, time = exif_dat.split()
      date = date.replace(":", "-")
      time = time.replace(":", "-")
      filename = date + '_' + time + '_' + ifile
      print ('EXIF: ' + ifile + '->' + filename)
   except:
      exif_dat = 'None None'

#Jolla-EXIF-bugaround by date in filename!
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
            filedat=exif_dat.replace(' ', '_')
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
      copyfile(inputfile, 'UNSORTIERT/'+ifile)
      print ('UNSORTIERT (Kein EXIF, kein Jolla): ' + ifile)
   else: 
      monat=date[0:7]    
      if not os.path.exists('SORTIERT'):
         os.mkdir('SORTIERT')
      if not os.path.exists('SORTIERT/'+monat):
         os.mkdir('SORTIERT/'+monat)
      copyfile(inputfile, 'SORTIERT/'+monat+'/'+filename)

if __name__ == "__main__":
   main(sys.argv[1:])


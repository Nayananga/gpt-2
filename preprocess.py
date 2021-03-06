#!/usr/bin/python

import sys, getopt
import json
import re

def main(argv):
   inputfile = ''
   outputfile = ''

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])

   except getopt.GetoptError:
      print ('preprocess.py -i <inputfile> -o <outputfile>')
      sys.exit(2)

   for opt, arg in opts:

      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()

      elif opt in ("-i", "--ifile"):
         inputfile = arg

      elif opt in ("-o", "--ofile"):
         outputfile = arg

   if (inputfile == '' or outputfile == ''):
      print ('preprocess.py -i <inputfile> -o <outputfile>')

   else:
      preprocess_data(inputfile, outputfile)

def preprocess_data(inputfile, outputfile):
   data = ''

   with open(inputfile) as f:
      data = f.read()
      f.close

   data = re.sub(r'(\[{"type":"Module","children")', r'<|endoftext|>\1', data)

   with open(outputfile, 'w') as e:
      e.write(data)
      e.close

if __name__ == "__main__":
   main(sys.argv[1:])
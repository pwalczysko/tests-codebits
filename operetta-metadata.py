import os
import argparse
import xml.etree.ElementTree as ET
import csv

tree = ET.parse("Index2.xml")
root = tree.getroot()

def show_data_well_based (plate, well):
    # need to parse the well value to get the numerical value
    column = well[1:]
    letter = well[0]
    ordinal = ord(letter)-64
    if int(ordinal) > 9:
        well_num = "r"+str(ordinal)+"c"+column
    else:
        well_num = "r0"+str(ordinal)+"c"+column
    print ("Images in the Well:", well)
    for item in root.iter('Images'):
        for URL in item.iter("URL"):
            if well_num in URL.text:
                print (URL.text)

    with open("ML-BE001-kvp.csv", "r") as f:
        f = csv.DictReader(f)
        data = [row for row in f]
        for csv_row in data:
            if (well == csv_row['Well']) and (plate == csv_row['Plate']):
                print ("These are the metadata associated with the images in this Well")
                print (csv_row)

def run(plate, well, imagename):

    if well != "":
       show_data_well_based (plate, well) 
    
    if (imagename != "") and (well == ""):
        well_num = imagename[0:6]
        column = well_num[5:6]
        if int(well_num[1:2]) > 9:
            row = chr (int (well_num[1:2])+64)
            well = row+column
        else:
            row = chr (int (well_num[2])+64)
            well = row+"0"+column

        print (row)
        print (column)
        print (well_num)

        print (well)
        print ("Images in the Well with image:", imagename)
        for item in root.iter('Images'):
            for URL in item.iter("URL"):
                if well_num in URL.text:
                    print (URL.text)
        with open("ML-BE001-kvp.csv", "r") as f:
            f = csv.DictReader(f)
            data = [row for row in f]
            for csv_row in data:
                if (well == csv_row['Well']) and (plate == csv_row['Plate']):
                    print ("These are the metadata associated with the images in this Well")
                    print (csv_row)

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--plate', default="",
                        help="Plate name")
    parser.add_argument('--well', default="",
                        help="Well name")
    parser.add_argument('--imagename',
                        default="",
                        help="Image name")
    args = parser.parse_args(args)
    run(args.plate, args.well, args.imagename)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
'''
Simple script opens images and displays associated metadata based on the 
Index.xml and ML-BE001-kvp.csv files
'''

path = "./data"



def main():
    open 

if __name__ == "__main__":
    main()